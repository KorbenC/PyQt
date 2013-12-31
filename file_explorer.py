#!/usr/bin/env python

from PyQt4 import QtCore, QtGui

#MainWindow class 
class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()

		widget = QtGui.QWidget()
		self.setCentralWidget(widget)

		topFiller = QtGui.QWidget()
		topFiller.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

		bottomFiller = QtGui.QWidget()
		bottomFiller.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

		vbox = QtGui.QVBoxLayout()
		vbox.setMargin(5)
		vbox.addWidget(topFiller)
		vbox.addWidget(bottomFiller)
		widget.setLayout(vbox)

		self.createActions()
		self.createMenus()

		message = 'Status text'
		self.statusBar().showMessage(message)

		self.setWindowTitle("File Explorer")
		self.setMinimumSize(160,160)
		self.resize(480,320)
	#Actions for menu buttons	
	def createActions(self):
		self.newAct = QtGui.QAction("&New", self, shortcut=QtGui.QKeySequence.New, statusTip="Create a new file")
	#Menus 
	def createMenus(self):
		self.fileMenu = self.menuBar().addMenu("&File")
		self.fileMenu.addAction(self.newAct)



#main
if __name__ == '__main__':
	import sys

	app = QtGui.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
