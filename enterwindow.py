#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui

class EnterWindow(QtGui.QWidget):

    def __init__(self, mainwindow, backwardwidg):
        super(EnterWindow, self).__init__()

        self.mainwindow = mainwindow
        self.backwardwidg = backwardwidg

        self.initUI()

    def initUI(self):

        #create content
        nextButton = QtGui.QPushButton('Next')
        backButton = QtGui.QPushButton('Back')
        statButton = QtGui.QPushButton('Statistics')

        #fill widget with content
        hlayout1 = QtGui.QHBoxLayout()
        hlayout2 = QtGui.QHBoxLayout()
        vlayout = QtGui.QVBoxLayout()

        hlayout1.addWidget(backButton)
        hlayout1.addStretch(1)
        hlayout1.addWidget(nextButton)

        hlayout2.addStretch(1)
        hlayout2.addWidget(statButton)
        hlayout2.addStretch(1)

        vlayout.addStretch(1)
        vlayout.addLayout(hlayout1)
        vlayout.addStretch(1)
        vlayout.addLayout(hlayout2)

        self.setLayout(vlayout)

        #send signals
        backButton.clicked.connect(self.backward)

    #create slots
    def backward(self):
        
        self.mainwindow.stack.removeWidget(self)
        self.mainwindow.stack.setCurrentWidget(self.backwardwidg)
        self.mainwindow.stack.currentWidget().resize()

    def resize(self):

        self.mainwindow.resize(500, 300)
    




