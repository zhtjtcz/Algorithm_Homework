import sys
from PyQt5.QtWidgets import *
from mainwin import *

def main():
	app=QApplication(sys.argv)
	windows=MainWindows()
	windows.show()
	app.exec_()

if __name__ == '__main__':
	main()