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
		self.mappic.clear()
		self.map.Draw()
		self.mappic.setPixmap(QPixmap('b.png'))

	def AddToolbar(self):
		self.toolbar=self.addToolBar('Tools')
		
		WatchAct=QAction('Watch',self)
		Icon_Watch=QIcon('Icon/test.png')
		WatchAct.setIcon(Icon_Watch)
		WatchAct.triggered.connect(lambda : self.Watch())

		SettingAct=QAction('Refresh',self)
		Icon_Setting=QIcon('Icon/refresh.png')
		SettingAct.setIcon(Icon_Setting)
		SettingAct.triggered.connect(lambda : self.Watch())

		ExitAct=QAction('Exit',self)
		Icon_Exit=QIcon('Icon/close.png')
		ExitAct.setIcon(Icon_Exit)

		ExitAct.triggered.connect(lambda : self.close())
		
		self.toolbar.addAction(WatchAct)
		self.toolbar.addAction(SettingAct)
		self.toolbar.addAction(ExitAct)

	def empty(self):
		print('123')
		pass

	def Addbox(self):
		self.Box=[]
		self.Vbox=[]
		self.RadioButton=[]
		self.Box.append(QGroupBox("Node Color Settings"))
		self.Vbox.append(QVBoxLayout())
		for i in self.cols:
			self.RadioButton.append(QRadioButton(i))
			self.Vbox[0].addWidget(self.RadioButton[len(self.RadioButton)-1])
		self.Vbox[0].addStretch(1)
		self.Box[0].setLayout(self.Vbox[0])

		self.Box.append(QGroupBox("Edge Color Settings"))
		self.Vbox.append(QVBoxLayout())
		for i in self.cols:
			self.RadioButton.append(QRadioButton(i))
			self.Vbox[1].addWidget(self.RadioButton[len(self.RadioButton)-1])
		self.Vbox[1].addStretch(1)
		self.Box[1].setLayout(self.Vbox[1])

		self.Box.append(QGroupBox("Path Color Settings"))
		self.Vbox.append(QVBoxLayout())
		for i in self.cols:
			self.RadioButton.append(QRadioButton(i))
			self.Vbox[2].addWidget(self.RadioButton[len(self.RadioButton)-1])
		self.Vbox[2].addStretch(1)
		self.Box[2].setLayout(self.Vbox[2])

	def SetLayout(self):
		self.main_widget=QWidget()
		self.main_layout=QGridLayout()
		self.main_widget.setLayout(self.main_layout)
		# Main layout set

		self.right_widget=QWidget()
		self.right_layout=QGridLayout()
		self.right_widget.setLayout(self.right_layout)
		#Right layout set

		self.left_widget=QWidget()
		self.left_layout=QGridLayout()
		self.left_widget.setLayout(self.left_layout)
		#Left layout set

		self.setCentralWidget(self.main_widget)
		self.main_layout.addWidget(self.left_widget,0,0,12,5)
		self.main_layout.addWidget(self.right_widget,0,5,12,7)

		self.mappic=QLabel()
		self.right_layout.addWidget(self.mappic,1,6,4,7)

		self.nodenum=QLineEdit()
		self.nodenum.setPlaceholderText("Nodes sum")
		self.nodenum.returnPressed.connect(self.empty)
		self.left_layout.addWidget(self.nodenum,1,0,1,5)

		self.edgesnum=QLineEdit()
		self.edgesnum.setPlaceholderText("Edges sum")
		self.edgesnum.returnPressed.connect(self.empty)
		self.left_layout.addWidget(self.edgesnum,2,0,1,5)
		self.Addbox()
		self.left_layout.addWidget(self.Box[0],3,0,1,5)
		self.left_layout.addWidget(self.Box[1],4,0,1,5)
		self.left_layout.addWidget(self.Box[2],5,0,1,5)

		

	def __init__(self):
		super().__init__()
		self.resize(1200,800)
		self.setWindowTitle("Simple Map")
		self.setWindowIcon(QIcon('Icon/main.png'))
		self.center()
		self.setWindowOpacity(0.9)
		self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

		self.cols=["Red","Blue","Yellow","Green","Black"]
		self.map=Map(5,0.5)
		self.map.CreateNolmalMap()

		self.AddToolbar()
		self.SetLayout()

		# self.Addbox()