import sys
from PyQt5.QtWidgets import *
from graph import *
from PyQt5.QtGui import *

class WatchWindows(QMainWindow):
	def Watch(self):
		self.map.Draw()

	def AddToolbar(self):
		self.toolbar=self.addToolBar('Tools')
		
		WatchAct=QAction('Watch',self)
		Icon_Watch=QIcon('a.png')
		WatchAct.setIcon(Icon_Watch)
		WatchAct.triggered.connect(lambda : self.Watch())

		SettingAct=QAction('Setting',self)
		Icon_Setting=QIcon('a.png')
		SettingAct.setIcon(Icon_Setting)

		ExitAct=QAction('Exit',self)
		Icon_Exit=QIcon('a.png')
		ExitAct.setIcon(Icon_Exit)
		ExitAct.triggered.connect(lambda : self.close())
		
		self.toolbar.addAction(WatchAct)
		self.toolbar.addAction(SettingAct)
		self.toolbar.addAction(ExitAct)
	
	def __init__(self):
		super().__init__()
		self.map=Map(5,0.5)
		self.map.CreateNolmalMap()
		self.resize(800,800)
		self.setWindowTitle("Simple Map")
		self.AddToolbar()