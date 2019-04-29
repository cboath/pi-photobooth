import tweepy
import os
import shutil
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def backupphotos():
    file1 = time.strftime("%Y%m%d%H%M%S-img1.jpg")
    file2 = time.strftime("%Y%m%d%H%M%S-img2.jpg")
    file3 = time.strftime("%Y%m%d%H%M%S-mergedimg.jpg")
    
    shutil.copy('/home/pi/ttr/Projects/Python/photobooth/img(0).jpg', '/home/pi/ttr/Projects/Python/photobooth/photoarchive/' + file1)
    shutil.copy('/home/pi/ttr/Projects/Python/photobooth/img(1).jpg', '/home/pi/ttr/Projects/Python/photobooth/photoarchive/' + file2)
    shutil.copy('/home/pi/ttr/Projects/Python/photobooth/imgmerge.jpg', '/home/pi/ttr/Projects/Python/photobooth/photoarchive/' + file3)

def postTweets(photos, message):
    photo_path = '/home/pi/ttr/Projects/Python/photobooth/' + photos
    #photo_path1 = '/home/pi/ttr/Projects/Python/photobooth/img(1).jpg'
    status = message

    api.update_with_media(photo_path, status=status)
    
    backupphotos()
    