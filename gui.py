# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../c++/qttest2/mainwindow.ui'
#
# Created: Thu Jan 17 19:28:00 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(625, 486)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.goto_channel_0 = QtGui.QPushButton(self.centralWidget)
        self.goto_channel_0.setObjectName(_fromUtf8("goto_channel_0"))
        self.gridLayout.addWidget(self.goto_channel_0, 0, 1, 1, 1)
        self.sinks = QtGui.QListWidget(self.centralWidget)
        self.sinks.setObjectName(_fromUtf8("sinks"))
        self.gridLayout.addWidget(self.sinks, 0, 0, 1, 1)
        self.goto_channel1 = QtGui.QPushButton(self.centralWidget)
        self.goto_channel1.setObjectName(_fromUtf8("goto_channel1"))
        self.gridLayout.addWidget(self.goto_channel1, 1, 1, 1, 1)
        self.channel0 = QtGui.QListWidget(self.centralWidget)
        self.channel0.setObjectName(_fromUtf8("channel0"))
        self.gridLayout.addWidget(self.channel0, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 178, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 2, 1)
        self.channel1 = QtGui.QListWidget(self.centralWidget)
        self.channel1.setObjectName(_fromUtf8("channel1"))
        self.gridLayout.addWidget(self.channel1, 1, 2, 2, 1)
        self.create_null = QtGui.QPushButton(self.centralWidget)
        self.create_null.setObjectName(_fromUtf8("create_null"))
        self.gridLayout.addWidget(self.create_null, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 625, 20))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.goto_channel_0.setText(QtGui.QApplication.translate("MainWindow", "->", None, QtGui.QApplication.UnicodeUTF8))
        self.goto_channel1.setText(QtGui.QApplication.translate("MainWindow", "->", None, QtGui.QApplication.UnicodeUTF8))
        self.create_null.setText(QtGui.QApplication.translate("MainWindow", "create null", None, QtGui.QApplication.UnicodeUTF8))

