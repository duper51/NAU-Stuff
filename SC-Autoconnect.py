#!/usr/bin/env python
import urllib
import urllib2
import json

'''Garbage Python 2 script to login to NAU's ResNet. I just copied some of the headers from my Kali VM's authentication and
pasted them in here. Honestly not my best work, but hey, it gets the job done. I'm actually fairly certain that SC will take ANY
value for USERNAME and PASSWORD, so you might try it without modification.
'''

url = "https://safeconnect.resnet.nau.edu:9443/api/authRest"
postData = { "platform": "Linux x86_64", "appversion": "5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36", "username": "USERNAME", "password": "PASSWORD" }
data = json.dumps(postData)
req = urllib2.Request(url, data, headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"})
try:
  response = urllib2.urlopen(req)
  # Should print something like {"error: null"} if successful
  print response.read()
except urllib2.HTTPError as e:
  print e
  print e.read()
