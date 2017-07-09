
# Hack-Day instructions

The hack-Day is intended to be a lightly structured event designed to allow hackers to explore, innovate and learn. The following instructions are provided as general roadmap to provide some structure.

## Getting help
* Google and YouTube are your best friends. If you have a question, are getting an error message, or need to learn something, then google first
* If you then get stuck, ask your teammates
* If you are still stuck, ask a hack-Day lead for help

## Hack-Day Steps

As with any tech challenge proceed in steps and verify all is well (including your knowledge) before continuing. 

### Setup your infrastructure

1. Build your Raspberry Pi and access it via SSH.  What linux does it run?  Is your internet access working?  Use `curl` to read `http://www.google.com`, what is the hostname? 

### Install and configure Minio Docker for S3 bucket
1. Install all dependencies for running Docker on Raspberry 
2. search for Minio docker on Raspbeery (Hint : Minio on ARM)
3. install Minio Docker
4. configure new bucket via web access and provide read-write permissions.
5. save you credentials 

### Setup the camera-webservice on the Raspberry Pi
1. Find the steps here: [camera-webservice/](camera-webservice/)

> Can you take photos from your camera using the webapp and see the results?  Yes, Success!

### Setup Node-Red flow to Tweet your photos
1. run nod-red service (configure it to run as a service - systemctl enable ) 
2. Open web browser and connect to node-red
2. configure your flow to get tweet trigers and send tweet with link for you Team member photo. 

> Can you see you tweets on the screen?  yes, Yes, Success!

