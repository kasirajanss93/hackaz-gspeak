# Gesture Speak @ Hack Arizona

This application was presented for #HackArizona 2017, held at University of Arizona, Tuscon from 13th to 15th of January 2017.

We have developed an application to recognize gestures, translate them to text and use this text to be voiced over by alexa, as a mechanism to help those with disablity speaking to communicate better.


#### Hardware Requirements:

* Leap Motion Device
* Amazon Echo
* A desktop/laptop/raspberry pi to interface Leap Motion and communicate with the server.

#### Software Requirements:

* Python 2.7
* NodeJS 6.0+
* ExpressJS 4.0+
* Amazon Lambda
* Alexa API
* Leap Motion SDK
* sign-language-tutor library by https://github.com/ssaamm/
* Memcached

#### Workflow:

The gesture identification module is present under the `leap-motion-client`, it HTTP Posts the data to the `memcache-and-controller` module which resides on a remote server. After relaying the information the `leap-motion-client` activates the Amazon Echo by a pre-recorded voice command. This command is intended to make alexa request data from the `aws-lambda` module which in turn requests the data from the `memcache-and-controller` module.

This recorded voice work-around is required as Amazon Echo is yet to receive a Push Notification API.


#### Deployment Instructions:

Please note that the IP address of the `memcache-and-controller` mentioned within the `leap-motion-client` and `aws-lambda` need to filled in `app.py` and `api.js` under the respective directories. 

* Deploy the `api.js` file present under the `aws-lambda` in a aws lambda instance
* Deploy the `index.js` file present under the `memcache-and-controller` on a linux VPS that has NodeJS, ExpressJS and Memcached installed on it.
* Deploy the `app.py` file present under the `leap-motion-client` on a raspberry pi board or equivalent, connected to a speaker and Leap Motion device.
* Have an Amazon Echo device with our skill activated so that it will be able to retrieve the information from AWS Lambda.


#### Team Members:

* Manoj Balasubramaniam Senguttuvan - man0j@asu.edu
* Kasirajan Selladurai Sellakumari - kselladu@asu.edu
* Deepak Soundararajan - dsounda2@asu.edu
* Gautham Adhithya - gadhithy@asu.edu
