#!/usr/bin/python
# pip install flask flask-restful pillow boto3 json elasticsearch
from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Api, Resource, reqparse, fields, marshal
import time, socket, uuid, os, boto3, json, sys, threading
from datetime import datetime
if os.name == 'nt':
	from PIL import Image

# Supress SSL cert errors
import botocore.vendored.requests
from botocore.vendored.requests.packages.urllib3.exceptions import InsecureRequestWarning
botocore.vendored.requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Get own IP address
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

# Create index with specific field settings

class RootAPI(Resource):

	def get(self):
		return make_response(jsonify({'status': 200, 'message' : "camera-webservice is running"}), 200)

class TakePhotoAPI(Resource):

	# route GET requests to POST (for debugging only)
	def get(self):
		return self.post()

	def post(self):
		# Maybe do something with post variables later...
		try:
			req = request.get_json(force=True)
		except:
			req = dict()
			pass

		# Take photo
		filename = str(uuid.uuid4())
		if os.name == 'nt':
			os.system(conf['camera_command'] + ' ' + filename)
			im = Image.open(filename)
			im.save(filename + '.jpg', 'JPEG')
			os.remove(filename)
			filename += '.jpg'
		else:
			filename += '.jpg'
			os.system(conf['camera_command'] + ' ' + filename)

		# Save filesize for metadata posted to ES
		filesize = os.path.getsize(filename)

		# For testing to avoid S3 and ES posting
		#  curl -s -H "Content-Type: application/json" -X POST -d '{"test":true}' http://localhost:8080/take_photo
		try:
			if req['test'] is True:
				print ('## Photo saved locally at: ' + filename)
				return make_response(jsonify({'filesize': filesize, 'filename': filename}))
		except:
			pass

		# Upload to S3 endpoint
		session = boto3.session.Session(aws_access_key_id=conf['access_key'], aws_secret_access_key=conf['secret_access_key'])
		s3 = session.resource(service_name='s3', endpoint_url=conf['endpoint'], verify=False)
		obj = s3.Object(conf['bucket'], filename)
		data = open(filename, 'rb')
		obj.put(Body=data, ContentType='image/jpeg')
		data.close()
		os.remove(filename)
		url = conf['endpoint'] + "/" + conf['bucket'] + "/" + filename
		print ('## Photo saved at: ' + url)

		# Post image taken to ES; let id be completed by ES
		#es = Elasticsearch([conf['elasticsearch_host']])
		## Create special datetime format that ES expects
		now = datetime.utcnow()
		ts = now.strftime("%Y-%m-%dT%H:%M:%S") + ".%03d" % (now.microsecond / 1000) + "Z"
		res_body = { "timestamp": ts, "url": url, "filesize": filesize, "camera_name": conf['camera_name'], "camera_ip": ip_address}

		# Return success	
		return make_response(jsonify(res_body), 200)

# Setup Flask and REST Endpoint
app = Flask(__name__, static_url_path="")
api = Api(app)

api.add_resource(RootAPI, '/')
api.add_resource(TakePhotoAPI, '/take_photo')

if __name__ == '__main__':

	print ('## Starting camera-webservice')
	try:
		with open('config.json') as data_file:
			conf = json.load(data_file)
			conf['camera_name']
			conf['endpoint']
			conf['bucket']
			conf['access_key']
			conf['secret_access_key']
			conf['camera_command']
	except Exception as e:
		sys.stderr.write('FATAL: Cannot open or parse configuration file : ' + str(e) + '\n\n')
		exit()

	ip_address = get_ip_address()
	#ip_address = '1.2.3.4'
	print ('## camera-webservice will be reachable at http://'+ ip_address + ':8080')
	app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)
