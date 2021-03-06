import sys
from graph import *
import networkx as nx
from PyQt5 import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

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

	def ShortPath(self):
		self.map.ShortestPath()
		self.info.setText("The shortest path length from 0 to " + str(self.map.n-1) + " is " + str(self.map.dis))
		self.mappic.clear()
		self.map.Draw()
		self.mappic.setPixmap(QPixmap('b.png'))

	def Tree(self):
		self.map.CreateTree()
		self.info.setText("The edge weight of the lowest spanning tree is " + str(self.map.weight))
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

		FindPathAct=QAction('Find Shortest Path',self)
		Icon_Path=QIcon('Icon/shortpath.png')
		FindPathAct.setIcon(Icon_Path)
		FindPathAct.triggered.connect(lambda : self.ShortPath())

		TreeAct=QAction('Find Spanning Tree',self)
		Icon_Tree=QIcon('Icon/tree.png')
		TreeAct.setIcon(Icon_Tree)
		TreeAct.triggered.connect(lambda : self.Tree())

		ExitAct=QAction('Exit',self)
		Icon_Exit=QIcon('Icon/close.png')
		ExitAct.setIcon(Icon_Exit)

		ExitAct.triggered.connect(lambda : self.close())
		
		self.toolbar.addAction(WatchAct)
		self.toolbar.addAction(SettingAct)
		self.toolbar.addAction(FindPathAct)
		self.toolbar.addAction(TreeAct)
		self.toolbar.addAction(ExitAct)

	def empty(self):
		print('2333')
		pass

	def btn_click(self):
		n=(int)(self.nodesnum.text().strip())
		m=(int)(self.edgesnum.text().strip())
		self.map=Map(n,m)

		for i in range(0,5):
			if (self.RadioButton[i].isChecked() == True):
				self.map.node_col=self.cols[i]
		
		for i in range(5,10):
			if (self.RadioButton[i].isChecked() == True):
				self.map.edge_col=self.cols[i%5]
		
		for i in range(10,15):
			if (self.RadioButton[i].isChecked() == True):
				self.map.path_col=self.cols[i%5]
		
		self.map.CreateNolmalMap()

		#TODO Button set
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
		self.main_layout.addWidget(self.left_widget,0,0,12,2)
		self.main_layout.addWidget(self.right_widget,0,3,12,9)

		self.mappic=QLabel()
		self.right_layout.addWidget(self.mappic,0,4,12,12)
		self.info=QLabel()
		self.info.setText("")
		self.right_layout.addWidget(self.info,0,3,1,7)

		self.nodesnum=QLineEdit()
		self.nodesnum.setPlaceholderText("Nodes sum")
		self.nodesnum.returnPressed.connect(self.empty)
		self.left_layout.addWidget(self.nodesnum,1,0,1,5)

		self.edgesnum=QLineEdit()
		self.edgesnum.setPlaceholderText("Edges sum")
		self.edgesnum.returnPressed.connect(self.empty)
		self.left_layout.addWidget(self.edgesnum,2,0,1,5)
		self.Addbox()
		self.left_layout.addWidget(self.Box[0],3,0,1,5)
		self.left_layout.addWidget(self.Box[1],4,0,1,5)
		self.left_layout.addWidget(self.Box[2],5,0,1,5)

		self.button=QPushButton("Submit")
		self.button.clicked.connect(self.btn_click)
		self.left_layout.addWidget(self.button,6,0,1,5)

	def __init__(self):
		super().__init__()
		self.resize(1200,800)
		self.setWindowTitle("Simple Map")
		self.setWindowIcon(QIcon('Icon/main.png'))
		self.center()
		self.setWindowOpacity(0.9)
		self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

		self.cols=["Red","Blue","Yellow","Green","Black"]
		self.map=Map(5,6)
		self.map.CreateNolmalMap()

		self.AddToolbar()
		self.SetLayout()

		# self.Addbox()