#!/usr/bin/python3

from PySide import QtGui, QtCore
import mydao

class StatWindow(QtGui.QWidget):

    def __init__(self, current_userid, current_ex_id):
        super(StatWindow, self).__init__()

        self.current_userid = current_userid
        self.current_ex_id = current_ex_id

        self.initUI()

    def initUI(self):

        #forming content
        self.okButton = QtGui.QPushButton('Ok', self)

        self.exNumber = QtGui.QLabel('Exercise: '.join(self.current_ex_id), self)
        self.bestNote = QtGui.QLabel('Best note: '.join(mydao.dbp.getStatData('best_note', self.current_userid,
            self.current_ex_id)), self)
        self.speed = QtGui.QLabel('Speed: '.join(mydao.dbp.getStatData('speed', self.current_userid,
            self.current_ex_id)), self)
        self.time = QtGui.QLabel('Time: '.join(mydao.dbp.getStatData('time', self.current_userid, self.current_ex_id)),
                self)
        self.lastDate = QtGui.QLabel('Last date: '.join(mydao.dbp.getStatData('last_date', self.current_userid,
            self.current_ex_id)),self)
        self.tryies = QtGui.QLabel('Tryies: '.join(mydao.dbp.getStatData('tryies', self.current_userid,
            self.current_ex_id)), self)

        #layout management
        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.okButton)
        self.hbox.addStretch(1)

        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.exNumber)
        self.vbox.addWidget(self.bestNote)
        self.vbox.addWidget(self.speed)
        self.vbox.addWidget(self.time)
        self.vbox.addWidget(self.lastDate)
        self.vbox.addWidget(self.tryies)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

        #send signal
        self.okButton.clicked.connect(self.close())

        self.resize(500, 300)
        self.show()

    



