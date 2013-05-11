#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import auth
import apiclient

class CalendarList():
	def __init__(self, page_token=None):
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

	def insert(self, calendarId=None, method=None):
		calendarid = calendarId or self.calendarId
		if not calendarid:
			print 'You must special your calendarId,default:yourname@gmail.com or\
				   somehashstring@group.calendar.google.com'
			raise
		
		calendar_list_entry = {'id': calendarid}
		created_calendar_list_entry = self.service.calendarList()\
			.insert(body=calendar_list_entry).execute()
		print created_calendar_list_entry

	def update(self,calendarId=None,colorId=None):
		# Why didn't this take effect?
		#calendar_list_entry = self.get(calendarId=calendarId)
		calendar_list_entry = self.service.calendarList()\
			.get(calendarId=calendarId).execute()
		calendar_list_entry['colorId'] = colorId
		try:
			update_calendar_list_entry = self.service.calendarList().update(
					calendarId=calendar_list_entry['id'],
					body=calendar_list_entry
				).execute()
		except apiclient.errors.HttpError as e:
			print e
		# We could get the etag of color
		#print update_calendar_list_entry['etag']

	def delete(self,calendarId=None):
		calendarid = calendarId or self.calendarId
		try:
			self.service.calendarList().delete(calendarId=calendarid).execute()
		except apiclient.errors.HttpError as e:
			print e
			print 'calendarId not found.'
			print 'you may retrieve it in "My calendars -> calendar setting:"' + \
				  '"Calendar Address"'

if __name__ == '__main__':
		calendarList = CalendarList()
		calendarList.list()
		calendarList.get('somewhere@group.calendar.google.com')
		#calendarList.insert(calendarId='somewhere@group.calendar.google.com')
		#calendarList.delete('somewhere@group.calendar.google.com')
		calendarList.update(
			calendarId='somewhere@group.calendar.google.com',
			colorId=12
			)
