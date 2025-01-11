# import the necessary packages
from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngine  # modules from PyQt5 we will use
import sys  # we will use sys to exit the application


class MainWindow(QtWidgets.QMainWindow):  # create a class for the main window

    def __init__(self):  # create a method to initialize the main window
        super().__init__()  # initialize the basic window

        # organizing the basic window
        self.mainWidget = QtWidgets.QWidget()  # create an empty widget
        self.setCentralWidget(self.mainWidget)  # set it as the main widget
        self.mainLayout = QtWidgets.QHBoxLayout()  # create the main horizontal layout
        self.mainWidget.setLayout(self.mainLayout)  # set the layout to the main widget

        # creating the left and right widgets
        self.leftWidget = QtWidgets.QWidget()  # left widget
        self.leftLayout = QtWidgets.QVBoxLayout()  # vertical layout
        self.leftWidget.setLayout(self.leftLayout)  # applying layout
        self.mainLayout.addWidget(self.leftWidget)  # adding to the main layout

        self.rightWidget = QtWidgets.QWidget()  # right widget
        self.rightLayout = QtWidgets.QVBoxLayout()
        self.rightWidget.setLayout(self.rightLayout)
        self.mainLayout.addWidget(self.rightWidget)

        # now creating the interactive widgets
        # line text input widget
        self.heroName = QtWidgets.QLineEdit()  # create a QLineEdit widget
        self.heroName.setPlaceholderText("Enter hero name")  # text to show in grey when empty
        self.leftLayout.addWidget(self.heroName)

        self.fontType = QtWidgets.QComboBox()  # create a QComboBox widget
        self.fontType.addItems(["Arial", "Verdana", "Times New Roman", "Courier New", "Georgia",
                                "Comic Sans MS", "Trebuchet MS", "Arial Black", "Impact"])  # add items to the combo box
        self.leftLayout.addWidget(self.fontType)



App = QtWidgets.QApplication(sys.argv)  # create an application
window = MainWindow()  # create a main window
window.setWindowTitle("Tale Maker")  # set the title of the window
window.show()  # display the main window
sys.exit(App.exec_())  # execute the application and exit the program when the window is closed
