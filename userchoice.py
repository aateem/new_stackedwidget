#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui


class ChoiceUser(QtGui.QWidget):

    def __init__(self, mainwindow):
        super(ChoiceUser, self).__init__()

        # every page saves a reference to the mainwindow
        # because it's the only way to get the 'stack' widget reference
        self.mainwindow = mainwindow

        self.initUI()

    def initUI(self):
        #forming content
        confirmButton = QtGui.QPushButton('Enter', self)
        createNewProfileButton = QtGui.QPushButton('Create new profile', self)

        confLabel = QtGui.QLabel('Enter your name', self)
        passLabel = QtGui.QLabel('Enter your password', self)

        userName = QtGui.QLineEdit(self)
        password = QtGui.QLineEdit(self)

        password.setEchoMode(QtGui.QLineEdit.Password)

        #fill widget with content
        vlayout = QtGui.QVBoxLayout()

        vlayout.addWidget(confLabel)
        vlayout.addWidget(userName)
        vlayout.addWidget(passLabel)
        vlayout.addWidget(password)
        vlayout.addStretch(1)
        vlayout.addWidget(confirmButton)
        vlayout.addWidget(createNewProfileButton)
        vlayout.addStretch(1)

        self.setLayout(vlayout)

        #send signals
        confirmButton.clicked.connect(self.forward)

    #create slots
    def forward(self):
        # for the next page widget do (don't forget to pass the mainwindow reference):
        # self.mainwindow.stack.addWidget(NextPageWidget(self.mainwindow))
        # self.mainwindow.stack.currentWidget().resize()
        pass

    def resize(self):
        # note that you should resize the mainwindow and not this widget
        self.mainwindow.resize(200, 300)