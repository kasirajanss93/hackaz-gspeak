# Gesture Speak @ Hack Arizona

This application was presented for #HackArizona 2017, held at University of Arizona, Tuscon from 13th to 15th of January 2017.

We have developed an application to recognize gestures, translate them to text and use this text to be voiced over by alexa, as a mechanism to help those with disablity speaking to communicate better.


#### Hardware Requirements:

* Leap Motion Device
* Amazon Echo

#### Software Requirements:

* Python 2.7
* NodeJS 6.0+
* ExpressJS 4.0+
* Amazon Lambda
* Alexa API
* Leap Motion SDK
* sign-language-tutor library by https://github.com/ssaamm/
* Memcached

The gesture identification module is present under the `leap-motion-client`, it HTTP Posts the data to the `memcache-and-controller` module which resides on a remote server. After relaying the information the `leap-motion-client` activates the Amazon Echo by a pre-recorded voice command. This command is intended to make alexa request data from the `aws-lambda` module which in turn requests the data from the `memcache-and-controller` module.

This recorded voice work-around is required as Amazon Echo is yet to receive a Push Notification API.
