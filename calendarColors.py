#!/usr/bin/python
# -*- coding: UTF-8 -*-

import auth

class Colors():
	
	def __init__(self,service=None):
		self.service = service or auth.Oauth().oauth()
		self.colors = self.service.colors().get().execute()

	def get(self):

		print "\tCalendar Colors:"
		for id, color in self.colors['calendar'].iteritems():
			# Attention,the official using iteritem(),it fall.
			print 'colorId: %s' % id
			print 'Background: %s' % color['background']
			print 'Foreground: %s' % color['foreground']
		
		print "\tEvent Colors:"
		for id, color in self.colors['event'].iteritems():
			print 'colorId: %s' % id
			print 'Background: %s' % color['background']
			print 'Foreground: %s' % color['foreground']

if __name__ == '__main__':
	colors = Colors()
	colors.get()
