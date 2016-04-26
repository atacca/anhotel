# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:15:58 2016
@author: danielmorgan

Twitter StreamListener for search terms 'an hotel' and 'an hospital'
Outputs results to a text file
"""

import tweepy
import json
import codecs

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret =  ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
file = codecs.open("an_hotel.txt", "w", "utf-8")


#Classes

class MyStreamListener(tweepy.StreamListener):
    """ StreamListener to find 'an hotel' and 'an hospital' """
    
    def on_status(self, status):
        print(status.text.encode('utf-8'))
    
    def on_data(self, data):
        json_data = json.loads(data)
        file.write(str(json_data))
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

myStream = tweepy.Stream(auth, MyStreamListener())
myStream.filter(track=["an hotel", "an hospital"], async=True)

