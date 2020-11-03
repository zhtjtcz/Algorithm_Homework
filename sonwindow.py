import sys
from PyQt5.QtWidgets import *
from graph import *
from PyQt5.QtGui import *

class WatchWindows(QMainWindow):
	def __init__(self):
		super().__init__()
		self.resize(500,500)
		self.setWindowTitle("Simple Map")
		self.toolbar=self.addToolBar('Exit')
		
		ExitAct=QAction('Exit',self)
		Icon_Exit=QIcon('a.png')
		ExitAct.setIcon(Icon_Exit)
		
		SettingAct=QAction('Setting',self)
		Icon_Setting=QIcon('a.png')
		SettingAct.setIcon(Icon_Setting)

		self.toolbar.addAction(ExitAct)
		self.toolbar.addAction(SettingAct)