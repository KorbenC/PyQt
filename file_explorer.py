#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

#MainWindow class
class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)

		widget = QtGui.QWidget()
		self.setCentralWidget(widget)

		self.setWindowTitle("File Explorer")
		self.setMinimumSize(160,160)
		self.resize(700,600)

		#create File System tree
		self.treeView = QTreeView()
		self.fileSystemModel = QFileSystemModel(self.treeView)
		self.fileSystemModel.setReadOnly(False)
		root = self.fileSystemModel.setRootPath("/")
		self.treeView.setModel(self.fileSystemModel)
		self.treeView.setRootIndex(root)
		#Create Layout
		Layout = QtGui.QVBoxLayout()
		Layout.addWidget(self.treeView)
		widget.setLayout(Layout)

		self.createActions()
		self.createMenus()
		self.createStatusBar()


	def createStatusBar(self):
	    self.statusBar().showMessage("Ready")

	def about(self):
		QtGui.QMessageBox.about(self, "About File Explorer",
			"Version 1.0\n"
			"Copyright 2014 Korben Carreno\n"
			"Example of a File Explorer")

	#Actions for menu buttons
	def createActions(self):
		self.newAct = QtGui.QAction("&New", self, shortcut=QtGui.QKeySequence.New, statusTip="Create a new file")
		self.exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q", statusTip="Exit the application", triggered=self.close)
		self.aboutAct = QtGui.QAction("&About", self,statusTip="About File Explorer", triggered=self.about)
		self.aboutQtAct = QtGui.QAction("About &Qt", self,statusTip="About Qt library", triggered=QtGui.qApp.aboutQt)
	#Menus
	def createMenus(self):
		self.fileMenu = self.menuBar().addMenu("&File")
		self.fileMenu.addAction(self.newAct)
		self.fileMenu.addSeparator()
		self.fileMenu.addAction(self.exitAct)

		self.helpMenu = self.menuBar().addMenu("&Help")
		self.helpMenu.addAction(self.aboutAct)
		self.helpMenu.addAction(self.aboutQtAct)


#main
if __name__ == '__main__':
	import sys

	app = QtGui.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
