#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Luo Lee'

import gflags
import httplib2
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client.tools import run
from apiclient.discovery import build

class Oauth():
	'''Authorize for you!'''
	def __init__(self):
		self.FLAGS = gflags.FLAGS

		fd = open('./consumer.txt')
		self.client_id = fd.readline().split('\n')[0]
		self.client_secret = fd.readline().split('\n')[0]
		self.scope	= fd.readline().split('\n')[0]
		self.developerKey = fd.readline().split('\n')[0]

		self.FLOW = OAuth2WebServerFlow(
    		client_id = self.client_id,
    		client_secret = self.client_secret,
    		scope = self.scope,
    		user_agent = 'PGCalendar/V0.1'
			)

	def oauth(self):
		# Comment this line?
		self.FLAGS.auth_local_webserver = False
		storage = Storage('calendar.dat')
		credentials = storage.get()
		if credentials is None or credentials.invalid == True:
			credentials = run(self.FLOW,storage)

		http = httplib2.Http()
		http = credentials.authorize(http)

		service = build(serviceName='calendar', version='v3',
                http=http, developerKey=self.developerKey)
		
		return service

if __name__ == '__main__':
	you = Oauth()
	service = you.oauth()
	print service,type(service)
