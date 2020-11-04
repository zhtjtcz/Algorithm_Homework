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

from pyqtgraph import GraphicsLayoutWidget
import pyqtgraph as pg
import qdarkstyle

class WatchWindows(QtWidgets.QMainWindow):
	def center(self):
		screen=QDesktopWidget().screenGeometry()
		size=self.geometry()
		self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

	def Watch(self):
		# self.mappic.clear()
		self.mappic.clear()
		self.map.Draw()
		self.mappic.setPixmap(QPixmap('b.png'))

		'''
		fig=plt.figure()
		self.map.Draw()
		self.pm=QPixmap(fig)
		'''
		# self.plt=self.mappic.addPlot(fig)

		# self.plt.addItem(fig)

		'''
		plt.cla()
		fig=plt.figure()
		self.map.Draw()
		cavans=FigureCanvas(fig)
		'''
		# cavans.resize(50,50)
		# cavans.move(100,100)
		# self.setCentralWidget(cavans)
		
		# self.wid.setLayout(fig)

		# self.grid.addWidget(cavans,0,1)

		# self.grid.addWidget(cavans)

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

	def Addbox(self):
		self.box1=QGroupBox("Parameter Settings")
		a=QRadioButton("Hello")
		b=QRadioButton("World")
		vbox=QVBoxLayout()
		vbox.addWidget(a)
		vbox.addWidget(b)
		vbox.addStretch(1)
		self.box1.setLayout(vbox)
		self.grid.addWidget(self.box1,0,0)

		self.wid=QWidget(self)
		self.setCentralWidget(self.wid)
		self.wid.setLayout(vbox)

	def __init__(self):
		super().__init__()
		self.resize(800,800)
		self.setWindowTitle("Simple Map")
		self.center()
		self.setWindowOpacity(0.9)
		self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

		self.map=Map(5,0.5)
		self.map.CreateNolmalMap()
		
		self.AddToolbar()
		self.main_widget=QWidget()
		self.main_layout=QGridLayout()
		self.main_widget.setLayout(self.main_layout)
		
		self.right_widget=QWidget()
		self.right_layout=QGridLayout()
		self.right_widget.setLayout(self.right_layout)

		self.setCentralWidget(self.main_widget)
		self.main_layout.addWidget(self.right_widget, 0, 5, 12, 7)

		self.mappic=QLabel()
		self.right_layout.addWidget(self.mappic,1,6,4,7)

		# self.Addbox()