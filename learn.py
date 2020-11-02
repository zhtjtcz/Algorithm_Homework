import sys
from PyQt5.QtWidgets import *

class Windows(QMainWindow):
	def __init__(self):
		super().__init__()
		self.resize(500,500)
		self.setWindowTitle("SeeGrary")
		self.menu=self.menuBar()
		#Init

		Filemenu=self.menu.addMenu('File')
		# Add a new root menu

		New=QAction('New',self)
		Filemenu.addAction(New)
		#Simple action

		Open=QMenu('Open',self)
		History=QAction('History',self)
		Open.addAction(History)
		Filemenu.addMenu(Open)
		# Son menu

		ExitMenu=self.menu.addMenu('Exit')

app=QApplication(sys.argv)
w=Windows()
w.show()
app.exec_()