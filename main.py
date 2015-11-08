from pyWeb import*
import sys
from PyQt4 import QtCore, QtGui
from webSearch import *

class MyApp(QtGui.QD):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    app.exec_()
