import sys
from PyQt5.QtWidgets import *
from graph import *
from sonwindow import *
from PyQt5.QtGui import *

class MainWindows(QMainWindow):
	def Simple(self):
		self.simmap=WatchWindows()
		self.simmap.map=Map(5,0.5)
		self.simmap.map.CreateNolmalMap()
		self.simmap.show()
		self.close()
		# self.map.Draw()

	def Flow(self):
		#TODO max-flow
		pass

	def __init__(self):
		super().__init__()
		self.resize(500,500)
		self.setWindowTitle("SeeGrary")
		self.menu=self.menuBar()
		#Init
		#TODO icon setting

		Newmenu=self.menu.addMenu('New')
		# Add a new root menu

		SimpleGraph=QAction('SimpleGraph',self)
		SimpleGraph.triggered.connect(lambda : self.Simple())
		FlowGraph=QAction('FlowGraph',self)
		FlowGraph.triggered.connect(lambda : self.Flow())
		Newmenu.addAction(SimpleGraph)
		Newmenu.addAction(FlowGraph)

		'''
		Open=QMenu('Open',self)
		History=QAction('History',self)
		Open.addAction(History)
		Newmenu.addMenu(Open)
		'''
		# Son menu

		ExitMenu=self.menu.addAction('Exit')
		ExitMenu.triggered.connect(lambda : self.close())