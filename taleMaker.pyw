# import the necessary packages
from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets  # modules from PyQt5 we will use
import sys  # we will use sys to exit the application


class MainWindow(QtWidgets.QMainWindow):  # create a class for the main window

    def __init__(self):  # create a method to initialize the main window
        """initialize the main window"""
        super().__init__()  # initialize the basic window

        # gather the content of the story from the file
        with open("story.txt", "r", encoding="utf-8") as file:  # open the file in read mode
            self.story = file.read()  # read the content of the file as a string

        # organizing the basic window
        self.mainWidget = QtWidgets.QWidget()  # create an empty widget
        self.setCentralWidget(self.mainWidget)  # set it as the main widget
        self.mainLayout = QtWidgets.QHBoxLayout()  # create the main horizontal layout
        self.mainWidget.setLayout(self.mainLayout)  # set the layout to the main widget

        # creating the left and right widgets
        self.leftWidget = QtWidgets.QWidget()  # left widget
        self.leftWidget.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)  # prevent from expanding horizontally
        self.leftLayout = QtWidgets.QVBoxLayout()  # vertical layout
        self.leftLayout.setAlignment(QtCore.Qt.AlignCenter)  # align to the center
        self.leftWidget.setLayout(self.leftLayout)  # applying layout
        self.mainLayout.addWidget(self.leftWidget)  # adding to the main layout

        self.rightWidget = QtWidgets.QWidget()  # right widget
        self.rightLayout = QtWidgets.QVBoxLayout()
        self.rightLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.rightWidget.setLayout(self.rightLayout)
        self.mainLayout.addWidget(self.rightWidget)

        # now creating the interactive widgets for the left side
        # line text input widget
        self.heroName = QtWidgets.QLineEdit()  # create a QLineEdit widget
        self.heroName.setPlaceholderText("Enter hero name")  # text to show in grey when empty
        self.heroName.textChanged.connect(self.updateStory)  # update the story when the name is changed in live
        self.leftLayout.addWidget(self.heroName)

        self.fontType = QtWidgets.QComboBox()  # create a QComboBox widget
        self.fontType.addItems(["Arial", "Verdana", "Times New Roman", "Courier New", "Georgia",
                                "Comic Sans MS", "Trebuchet MS", "Arial Black", "Impact"])  # add items to the combo box
        self.fontType.setCurrentText("Comic Sans MS")  # set the default selected item
        self.fontType.currentIndexChanged.connect(self.updateStory)  # update the story when the font is changed
        self.leftLayout.addWidget(self.fontType)

        # create a stretch to push the widgets to the bottom
        self.leftLayout.addStretch()

        # create an export button
        self.exportButton = QtWidgets.QPushButton("Write to file")
        self.exportButton.clicked.connect(self.exportStory)  # execute the method when the button is clicked
        self.leftLayout.addWidget(self.exportButton)

        # we will now create the widgets for the right side
        # create a title label with an icon
        self.titleWidget = QtWidgets.QWidget()
        self.titleLayout = QtWidgets.QHBoxLayout()
        self.titleLayout.setAlignment(QtCore.Qt.AlignCenter)  # align the layout to the center
        self.titleWidget.setLayout(self.titleLayout)
        self.rightLayout.addWidget(self.titleWidget)

        self.imageLabel = QtWidgets.QLabel()  # create a QLabel widget for the image
        self.imageLabel.setPixmap(QtGui.QPixmap("image.png").scaled(50, 50, QtCore.Qt.KeepAspectRatio))  # set the image in the label and scale it
        self.titleLayout.addWidget(self.imageLabel)

        self.titleLabel = QtWidgets.QLabel("My Amazing Tale")  # create a QLabel widget for the title
        self.titleLabel.setFont(QtGui.QFont("Arial", 20))  # set the font and font size
        self.titleLayout.addWidget(self.titleLabel)

        # create a text browser
        self.storyBrowser = QtWidgets.QTextBrowser()
        self.storyBrowser.setStyleSheet("background: transparent;")  # set specific styling with css, in this case, the background color
        self.storyBrowser.setMinimumHeight(300)  # set the minimum height of the text browser
        self.rightLayout.addWidget(self.storyBrowser)

        # create a web page to display a video
        self.videoWidget = QtWebEngineWidgets.QWebEngineView()  # webpage viewer widget, this uses local HTML
        self.videoWidget.setFixedSize(576, 324)  # set the size of the widget
        htmlString = '<style> body{margin:0px} </style> <iframe width="100%" height="100%" src="https://www.youtube-nocookie.com/embed/bOBLKHx7E5U" frameborder="0"></iframe>'  # HTML content to display a video
        self.videoWidget.setHtml(htmlString)  # set the HTML content
        self.videoWidget.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)  # prevent the widget from expanding in both directions
        self.rightLayout.addWidget(self.videoWidget)

        self.updateStory()  # update the story once when the window is created
    

    def updateStory(self):
        """method to update the story based on the inputs"""
        # replace the placeholders with the actual values
        heroName = self.heroName.text()  # get the text from the QLineEdit widget
        if heroName:  # if the hero name is not empty, change the story
            newStory = self.story.replace("[name]", heroName)  # replace the placeholder with the actual hero name
        else:  # if the hero name is empty, keep the original story with the placeholder
            newStory = self.story

        # select the font
        fontType = self.fontType.currentText()  # get the selected font type
        self.storyBrowser.setFont(QtGui.QFont(fontType, 14))  # apply ther font to the text browser

        self.storyBrowser.setText(newStory)  # write the story in the text browser widget
    
    def exportStory(self):
        """method to export the story to a text file"""
        story = self.storyBrowser.toPlainText()  # get the content from the text browser
        exportPath, fileType = QtWidgets.QFileDialog.getSaveFileName(self, "Export story", filter="TEXT files (*.txt)")  # open a dialog to select the path to save the text file
        if exportPath:  # if the user chose a path
            with open(exportPath, "w", encoding="utf-8") as file:  # open the file in write mode
                file.write(story)  # write the story in the file


App = QtWidgets.QApplication(sys.argv)  # create an application
window = MainWindow()  # create a main window
window.setWindowTitle("Tale Maker")  # set the title of the window
window.setWindowIcon(QtGui.QIcon("icon.png"))  # set the window icon
window.show()  # display the main window
sys.exit(App.exec_())  # execute the application and exit the program when the window is closed
