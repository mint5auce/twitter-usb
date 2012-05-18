import serial
import time
import twitterkeys as twitter

# Last import is private keys, moved to seperate file for privacy, but in the form: api = twitter.Api(consumer_key='your key here', consumer_secret='your key here', access_token_key='your key here', access_token_secret='your key here') 

arduino = serial.Serial('/dev/cu.usbserial-A9007Rsx', 9600)

status = arduino.readline()

# import pdb
# pdb.set_trace()

twitter.api.PostUpdate(status)
