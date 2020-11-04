import sys
from graph import *
import networkx as nx
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class WatchWindows(QtWidgets.QMainWindow):
	def Watch(self):
		plt.cla()
		fig=plt.figure()
		self.map.Draw()
		cavans=FigureCanvas(fig)
		self.setCentralWidget(cavans)


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
		#TODO icon beautify

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
		self.setCentralWidget(QtWidgets.QWidget())