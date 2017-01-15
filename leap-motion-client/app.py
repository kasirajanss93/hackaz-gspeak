# from __future__ import print_function
from classifier import clf
from hand_data import get_hand_position
from lib import Leap
import warnings
import time
import httplib,urllib
import vlc
warnings.filterwarnings("ignore")

controller = Leap.Controller()
controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)
prev_prediction = None
word = []

dictmapping={}
dictmapping['a']='The weather is nice today.'
dictmapping['b']='How are you?'
dictmapping['c']='Hello'
dictmapping['d']='Nice to meet you'
dictmapping['e']='Good Morning'
dictmapping['f']='Good Afternoon'
dictmapping['g']='Good Night'
dictmapping['h']='Happy Pongal'
dictmapping['i']='Would you like a cup of coffee?'
dictmapping['j']='Good Bye'
dictmapping['k']='Would you like to go for a walk?'
dictmapping['l']='I am having a great time'
dictmapping['m']='Have you eaten yet?'
dictmapping['n']='I am going out'
dictmapping['o']='How was school today?'
dictmapping['p']='Talk to you later'
dictmapping['q']='Where are you going?'
dictmapping['r']='Close the door'
dictmapping['s']='Food is ready'
dictmapping['t']='Time to go to bed.'
dictmapping['u']='Turn the lights off'
dictmapping['v']='Come here.'
dictmapping['w']='Help me find my glasses.'
dictmapping['x']='Do your chores'
dictmapping['y']='What a lovely view.'
dictmapping['z']='Let us go out for a movie'

IP_ADDR = "138.197.222.95:8080"; #DB SERVER IP COMES HERE

def send_data(data):
    print data
    h = httplib.HTTPConnection(IP_ADDR)
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    h.request('POST', '/', urllib.urlencode({'data':data}), headers)
    r = h.getresponse()
    time.sleep(2)
    p = vlc.MediaPlayer("file:///home/gautham/temp/sign-language-tutor/alexa_call.m4a")
    p.play()
while True:
    try:
        hand_pos = get_hand_position(controller)
        if hand_pos is None:
            continue
        features = [v for k, v in hand_pos.iteritems()]
        prediction = ''.join(clf.predict(features))
        time.sleep(1)
        if prediction != prev_prediction:
            prev_prediction = prediction
            send_data(dictmapping[prediction])
            time.sleep(10)
            # print dictmapping[prediction]
    except Exception as ex:
        print(ex.message)    
        continue
