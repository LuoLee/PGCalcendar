#!/usr/bin/python
# -*- coding: UTF-8 -*-

import auth

class CalendarSettings():
	def __init__(self):
		#pass
		self.service = auth.Oauth().oauth()

	def list(self):
		'''List all of your calendar settings.
		'''
		settings = self.service.settings().list().execute()
		
		for setting in settings['items']:
			print '%s: %s' % (setting['id'], setting['value'])
	
	def get(self, settingId=None):
		'''What did you want get from me?
		   Mybe you want call list?
		   \nAcceptable variable:\nformat24HourTime\ndefaultEventLength\ntimezone
		   \ncountry\nhideWeekends\ndefaultCalendarMode\ndisplayAllTimezones
		   \nshowDeclinedEvents\nremindOnRespondedEventsOnly\nhideInvitations
		   \nweather\nuserLocation\ndateFieldOrder\ntimezoneLabel
		   \nalternateCalendar\nlocale\ncustomCalendarMode\nweekStart
		'''
		setting = self.service.settings().get(setting=settingId).execute()
		print '%s %s' % (setting['id'], setting['value'])
		

if __name__ == '__main__':
	settings = CalendarSettings()
	#settings.list()
	settings.get('timezone')
