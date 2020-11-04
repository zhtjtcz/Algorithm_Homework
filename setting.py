from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import networkx as nx
import sys

class PrettyWidget(QWidget):
	NumButtons=['plot1','plot2', 'plot3']
	def __init__(self):
		super().__init__()
		font=QFont()
		font.setPointSize(16)
		self.initUI()

	def initUI(self):
		self.setGeometry(100, 100, 800, 600)
		self.center()
		self.setWindowTitle('S Plot')
		grid=QGridLayout()
		self.setLayout(grid)
		
		self.createVerticalGroupBox()

		buttonLayout=QVBoxLayout()
		buttonLayout.addWidget(self.verticalGroupBox)

		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		grid.addWidget(self.canvas, 0, 1, 9, 9)		  
		grid.addLayout(buttonLayout, 0, 0)

		self.show()

	def createVerticalGroupBox(self):
		self.verticalGroupBox = QGroupBox()
		layout=QVBoxLayout()
		for i in  self.NumButtons:
				button = QPushButton(i)
				button.setObjectName(i)
				layout.addWidget(button)
				layout.setSpacing(10)
				self.verticalGroupBox.setLayout(layout)
				button.clicked.connect(self.submitCommand)

	def submitCommand(self):
		eval('self.' + str(self.sender().objectName()) + '()')

	def plot1(self):
		self.figure.clf()
		ax1 = self.figure.add_subplot(211)
		x1 = [i for i in range(100)]
		y1 = [i**0.5 for i in x1]
		ax1.plot(x1, y1, 'b.-')

		ax2 = self.figure.add_subplot(212)
		x2 = [i for i in range(100)]
		y2 = [i for i in x2]
		ax2.plot(x2, y2, 'b.-')
		self.canvas.draw_idle()

	def plot2(self):
		self.figure.clf()
		ax3 = self.figure.add_subplot(111)
		x = [i for i in range(100)]
		y = [i**0.5 for i in x]
		ax3.plot(x, y, 'r.-')
		ax3.set_title('Square Root Plot')
		self.canvas.draw_idle()

	def plot3(self):
		self.figure.clf()
		B = nx.Graph()
		B.add_nodes_from([1, 2, 3, 4], bipartite=0)
		B.add_nodes_from(['a', 'b', 'c', 'd', 'e'], bipartite=1)
		B.add_edges_from([(1, 'a'), (2, 'c'), (3, 'd'), (3, 'e'), (4, 'e'), (4, 'd')])

		X = set(n for n, d in B.nodes(data=True) if d['bipartite'] == 0)
		Y = set(B) - X

		X = sorted(X, reverse=True)
		Y = sorted(Y, reverse=True)

		pos = dict()
		pos.update( (n, (1, i)) for i, n in enumerate(X) ) # put nodes from X at x=1
		pos.update( (n, (2, i)) for i, n in enumerate(Y) ) # put nodes from Y at x=2
		nx.draw(B, pos=pos, with_labels=True)
		self.canvas.draw_idle()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.aboutToQuit.connect(app.deleteLater)
	app.setStyle(QStyleFactory.create("gtk"))
	screen = PrettyWidget() 
	screen.show()
	sys.exit(app.exec_())