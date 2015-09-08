import sys
from PyQt4 import QtGui
from webSearch import Ui_Dialog
import pyWeb


class searchWindow(QtGui.QDialog):
    def __init__(self, parent= None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #search button
        self.searchButton = QtGui.QPushButton()
        self.searchButton.clicked.connect(self.Searcher)


    def Searcher(self):
        searchString =  str(self.lineEdit.currentText())
        myEngine = str(self.comboBox.currentText())
        pyWeb.searchFor(str(pyWeb.getEngine(myEngine)), searchString)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = searchWindow()
    myapp.show()
    app.exec_()
