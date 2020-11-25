from distutils.core import setup
import py2exe

setup(windows=["main.py","sonwindow.py","graph.py","test.py"])

#setup(console=["main.py","sonwindow.py","graph.py","test.py"])