# Hack-Day: Suggested Pre-work

If you are a beginner or some of these topics are new to you, then you should take some time prior to the DevOps Day event to prepare yourself.

## UNIX Terminal
The RaspberryPI will be accessed using SSH which is typically run from a UNIX command line. 
On a Mac, you can simply open a 'Terminal' window which provides you with a UNIX command line.  From there you can type 'ssh pi@<ip address>' to access your RaspberryPI.
On a PC, you will need to install a tool like PuTTy (Google "putty download windows")
For instructions on how to use PuTTY with the RaspberryPI Youtube.com "how to ssh with putty raspberry pi".

### Basic UNIX Commands
You will be expected to have basic UNIX command line knowledge.  If this is going to be a challenge, please let your SE manager and/or Hack-Day lead know, so they can pair you up with someone who does have UNIX skills.

### UNIX Editor
The activity requires basic text file editing.  The RaspberryPI has the 'nano' and 'vim' editors pre-installed.  If you are not familiar with one of these editors, you might want to either install your own favorite UNIX editor or learn one of the provided editors.

### SSH and SCP Commands
In module 1, you will be asked to SSH into the RaspberryPI, take a picture, then copy the picture back to your laptop using SCP.  Make sure you know how to use the ssh and scp commands.  

## Basic Git/GitHub Tutorial
If this is your first time using Git or GitHub (or any source control tool for that matter), I recommend watching a Git/GitHub tutorial. There are many good videos on Youtube.com, here is one example: [https://www.youtube.com/watch?v=0fKg7e37bQE](https://www.youtube.com/watch?v=0fKg7e37bQE)
The hack-Day instructions will ask you to `clone` a GitHub repository.  

## Using Git/GitHub as a Developer
You will also be asked to perform basic developer tasks such as:

1. Clone a GitHub repository
1. Create a feature/change branch
1. Implement a new feature or code change (fix a bug) and then commit the change to the branch
1. Implement a 'pull' request and sub the change to GitHub for review

Watch the following Youtube.com video to learn about each of these steps.[https://www.youtube.com/watch?v=oFYyTZwMyAg](https://www.youtube.com/watch?v=oFYyTZwMyAg)

## What is a RaspberryPI
If you don't know what a RaspberryPI is then you might want to learn a little bit before the hack-Day. Here is a couple excellent video overviews.
* What is RaspberryPI: [https://www.youtube.com/watch?v=ZYPATphfGY4](https://www.youtube.com/watch?v=ZYPATphfGY4)
* RaspPI Camera Service: [https://www.youtube.com/watch?v=WNKbZsrsKVs](https://www.youtube.com/watch?v=WNKbZsrsKVs)
The labs will use the following RaspberryPI hardware. If you already have a RaspberryPI you should be able to use an older device as well.  The following items were ordered from Amazon.com.

1. Raspberry Pi 3 Basic Starter Kit
1. Cheap USB Webcam
1. Mirco SD Card for storage

## Installing UNIX packages and tools
You will be asked to install various development tools, libraries and applications on the RaspberryPI. If you are not familiar with tools like 'apt-get', 'yum', 'pip', and 'gem' do a little Google searching to learn how these are used.
The hack-Day activity will specifically ask you to install Python packages using apt-get and pip. If you don't know how to install packages like 'fswebcam', then you might want to do a little pre-work.  

## Python languages
The Hack-Day is built on Pythoncoding examples. You are not expected to know these programming languages.. What you are expected to know is that these are the tools the modern software developer uses so it can't hurt to know a little about them.
There are numerous getting started guides and training video on the web for those who are interested in learning.

## S3 Object storage and Minio storage
You will be asked to configure the RaspberryPI web service to upload images to minio (object storage - S3 like). Three key S3 terms should be understood:
* configure Minio on Raspberry
* S3 Endpoint - What is a S3 endpoint?
* S3 Bucket - What is a bucket and how do I create a bucket?
* S3 Access Key and Secret Access Key - what are they how, how do you get one?
* S3 Bucket Policies

### Searching Hack-Day data
Consider how you might use the hack-Day data, what searches you might apply and what data you might want or need to collect to generate interesting search results.

## Docker / Containers / Micro-services
During the hack-Day activity you will use a docker container to run a microservice. If you have not familiar with Docker and containers, it is strongly suggested that you do some pre-work.  
There will not be enough time on hack-Day to learn Docker from scratch, so it is recommended you come in with some basic Docker knowledge.

### Docker Pre-Work (tutorial and installation)
There are many Docker tutorials on YouTube. I would recommend setting aside 1-2 hours to go thru the tutorials as well as installing and running Docker on your own laptop.    

### Docker on RaspberryPI
Docker enjoys only limited support on RaspberryPI, it's recommended to understand the limitation prior the Hack-Day. 

### Node-Red
During the hack-Day activity you will use a Node-Red for flow and coding, so it is recommended you come in with some basic Node-red knowledge on Docker.
