# import the necessary packages
from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngine  # modules from PyQt5 we will use
import sys  # we will use sys to exit the application


class MainWindow(QtWidgets.QMainWindow):  # create a class for the main window

    def __init__(self):  # create a method to initialize the main window
        super().__init__()  # initialize the basic window


App = QtWidgets.QApplication(sys.argv)  # create an application
window = MainWindow()  # create a main window
window.show()  # display the main window
sys.exit(App.exec_())  # execute the application and exite the program when the window is closed
