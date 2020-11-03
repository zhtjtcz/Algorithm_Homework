import sys
from PyQt5.QtWidgets import *
from mainwin import *
from sonwindow import *
from PyQt5.QtGui import *

def WatchWindows_test():
	app=QApplication(sys.argv)
	w=WatchWindows()
	w.show()
	app.exec_()

def main():
	app=QApplication(sys.argv)
	windows=MainWindows()
	windows.show()
	app.exec_()

if __name__ == '__main__':
	main()
	# WatchWindows_test()