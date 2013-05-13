#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from PyQt4 import QtGui


class PGCWindow(QtGui.QWidget):

	def __init__(self):

		super(PGCWindow, self).__init__()

		self.initUI()

	def initUI(self):
		'''Init the window by the size of half of width and height.
		'''
		screen = QtGui.QDesktopWidget().screenGeometry()
		self.resize(screen.width()/2, screen.height()/2)
		self.center()

		self.setWindowTitle('Center')
		self.show()

	def center(self):
		'''Put the window to the center of your screen.
		'''
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def closeEvent(self, event):
		'''Give you a choice?
		'''
		reply = QtGui.QMessageBox.question(self, 'Message',
					'Are you sure to quit?',
					QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
					QtGui.QMessageBox.No)

		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	
def main():

	app = QtGui.QApplication(sys.argv)
	ex = PGCWindow()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
