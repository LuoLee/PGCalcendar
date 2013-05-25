#!/usr/bin/python
# -*- coding: utf-8 -*-

import auth
import json


class Events():

	def __init__(self):
		
		self.service = auth.Oauth().oauth()

	def list(self,calendarid='primary'):	# Default

		page_token = None
		while True:
			events = self.service.events().list(calendarId=calendarid).execute()
			if events['items']:
				for event in events['items']:
					try:
						print event['start']['dateTime'],event['id'],event['summary']
					except KeyError as e:	# KeyError: 'summary'
						#print e
						continue
			page_token = events.get('nextPageToken')
			if not page_token:
				break
	def instances(self,calendarid='primary',eventid=None):

		events = self.service.events().instances(calendarId=calendarid,\
				eventId=eventid).execute()
		#for event in events['items']:
		try:
			print 'Updated:%s\tSummary:%s\n' %\
				(events['updated'].decode('utf-8'),\
				events['summary'].decode('utf-8'))
		except KeyError as e:	# Refer above
			pass
	def get(self,calendarid='primary',eventid=None):

		event = self.service.events().get(calendarId=calendarid,\
				eventId=eventid).execute()
		print event['summary']

	def quickAdd(self,calendarid='primary',text=None):

		created_event = self.service.events().quickAdd(calendarId=calendarid,
				text=text).execute()
		print created_event['id'],created_event['start']['dateTime'],\
				created_event['summary']
	
	def insert(self,calendarid='primary',maxattendees=None,
			sendnotifications=False,event=None):
		'''event must be a event formated by makeBody()
		'''
		#pass
		created_event = self.service.events().insert(calendarId=calendarid,
											body=event).execute()
		print created_event['id']
		
		
	def makeBody(self,summary=None,location='where',start='1970-01-01T00:00:00+08:00',
			end='1970-01-01T00:00:00+08:00',description=None,method='email',
			minutes=15):
		'''summary is the title of this event;
		   location is somewhere this event will ocur;
		   start or end is the time of this event will ocur,the string format of
		   this parameter refering the RFC-3339,you can assign `yyyy-mm-dd` for
		   all day event;
		   method is how do you receive your event notifications, it could be
		   `sms`,`email` or `popup`;
		   description is optical, it's may the detial of this event;
		'''
		print description
		JSON = json.dumps({'summary':summary,'location':location,
				'start':{'dateTime':start},
				'end':{'dateTime':end},
				'description':description},ensure_ascii=False,encoding='utf-8')
		# Better to use loads()
		#return ast.literal_eval(JSON)
		return json.loads(JSON,encoding='utf-8')

		

if __name__ == '__main__':
	events = Events()
	#events.list(calendarid='yourCalendarId@group.calendar.google.com')
	#events.list()
	#events.instances(eventid='entdfrj3jkvadhuiri3j2mdoto')
	#events.get(eventid='hashString')
	#events.quickAdd(text='这是一个来自PGCalendar的测试')
	#events.quickAdd(text='This is a second test from PGCalendar.')
	js = events.makeBody(summary='PGCalendar新建事件测试',location='Home',
		start='2013-05-25T22:55:00.000+08:00',end='2013-05-25T23:30:00.000+08:00',
		description='将事件的各个字段整合成JSON格式输出，再转换为dict格式insert'
		,method='sms')
	print type(js)
	print js
	events.insert(calendarid='your@gmail.com', event=js)
