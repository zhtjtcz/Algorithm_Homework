import sys
from mainwin import *
from sonwindow import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pyqtgraph import GraphicsLayoutWidget
import pyqtgraph as pg

def main():
	app=QApplication(sys.argv)
	w=WatchWindows()
	w.show()
	app.exec_()

if __name__ == '__main__':
	main()