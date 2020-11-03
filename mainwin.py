import sys
from PyQt5.QtWidgets import *

class MainWindows(QMainWindow):
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
		FlowGraph=QAction('FlowGraph',self)
		Newmenu.addAction(SimpleGraph)
		Newmenu.addAction(FlowGraph)

		'''
		Open=QMenu('Open',self)
		History=QAction('History',self)
		Open.addAction(History)
		Newmenu.addMenu(Open)
		'''
		# Son menu

		ExitMenu=self.menu.addMenu('Exit')