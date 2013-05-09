#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import auth

class CalendarList():
	def __init__(self, page_token=None):
		#pass
		self.service = auth.Oauth().oauth()

	def list(self, page_token=None):
		while True:
			calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
			if calendar_list['items']:
				for calendar_list_entry in calendar_list['items']:
					print calendar_list_entry['summary']
			try:
				page_token = calendar_list.get['nextPageToken']
			except TypeError as e:
				#print e
				'''OK?'''
				pass

			if not page_token:
				break
	
	def get(self, calendarId=None):
		'''Get your calendar.
		'''
		if calendarId is None:
			print "You must give your calendarId:yourname@gmail.com"
			sys.exit(-1)
		calendar_list_entry = self.service.calendarList().get(calendarId=calendarId).execute()
		print calendar_list_entry['summary']

if __name__ == '__main__':
		calendarList = CalendarList()
		calendarList.list()
		#calendarList.get('yourname@gmail.com')
