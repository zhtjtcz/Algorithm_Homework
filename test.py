from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import networkx as nx
import sys

class Test(QWidget):
	def __init__(self):
		super().__init__()
		font=QFont()
		font.setPointSize(16)
		self.initUI()
	
	def center(self):
		qr=self.frameGeometry()
		cp=QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def initUI(self):
		self.setGeometry(100, 100, 800, 600)
		self.center()
		self.setWindowTitle('S Plot')

		grid=QGridLayout()
		self.setLayout(grid)

		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		grid.addWidget(self.canvas, 0, 1, 9, 9)

	def Show(self):
		self.figure.clf()
		B=nx.Graph()
		B.add_nodes_from([1, 2, 3, 4], bipartite=0)
		B.add_nodes_from(['a', 'b', 'c', 'd', 'e'], bipartite=1)
		B.add_edges_from([(1, 'a'), (2, 'c'), (3, 'd'), (3, 'e'), (4, 'e'), (4, 'd')])
		nx.draw(B)
		self.canvas.draw_idle()
		self.show()

if __name__ == '__main__':
	app=QApplication(sys.argv)
	a=Test()
	a.Show()
	# a.show()
	sys.exit(app.exec_())