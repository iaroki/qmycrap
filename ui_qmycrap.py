# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qmycrap.ui'
#
# Created: Fri Sep 12 12:03:08 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(798, 444)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeView = QtGui.QTreeView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QtCore.QSize(20, 0))
        self.treeView.setBaseSize(QtCore.QSize(0, 0))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.horizontalLayout.addWidget(self.treeView)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setMovable(True)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 798, 26))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuInsert = QtGui.QMenu(self.menuBar)
        self.menuInsert.setObjectName(_fromUtf8("menuInsert"))
        self.menuRun = QtGui.QMenu(self.menuInsert)
        self.menuRun.setObjectName(_fromUtf8("menuRun"))
        self.menuPlatform = QtGui.QMenu(self.menuInsert)
        self.menuPlatform.setObjectName(_fromUtf8("menuPlatform"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/save.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/exit.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setIconVisibleInMenu(True)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionDate = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/date.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDate.setIcon(icon2)
        self.actionDate.setIconVisibleInMenu(True)
        self.actionDate.setObjectName(_fromUtf8("actionDate"))
        self.actionFirstrun = QtGui.QAction(MainWindow)
        self.actionFirstrun.setObjectName(_fromUtf8("actionFirstrun"))
        self.actionRerun = QtGui.QAction(MainWindow)
        self.actionRerun.setObjectName(_fromUtf8("actionRerun"))
        self.actionPS1 = QtGui.QAction(MainWindow)
        self.actionPS1.setObjectName(_fromUtf8("actionPS1"))
        self.actionPS2 = QtGui.QAction(MainWindow)
        self.actionPS2.setObjectName(_fromUtf8("actionPS2"))
        self.actionPS3 = QtGui.QAction(MainWindow)
        self.actionPS3.setObjectName(_fromUtf8("actionPS3"))
        self.actionPSP = QtGui.QAction(MainWindow)
        self.actionPSP.setObjectName(_fromUtf8("actionPSP"))
        self.actionPC = QtGui.QAction(MainWindow)
        self.actionPC.setObjectName(_fromUtf8("actionPC"))
        self.actionNDS = QtGui.QAction(MainWindow)
        self.actionNDS.setObjectName(_fromUtf8("actionNDS"))
        self.actionGBA = QtGui.QAction(MainWindow)
        self.actionGBA.setObjectName(_fromUtf8("actionGBA"))
        self.actionSNES = QtGui.QAction(MainWindow)
        self.actionSNES.setObjectName(_fromUtf8("actionSNES"))
        self.actionNES = QtGui.QAction(MainWindow)
        self.actionNES.setObjectName(_fromUtf8("actionNES"))
        self.actionWII = QtGui.QAction(MainWindow)
        self.actionWII.setObjectName(_fromUtf8("actionWII"))
        self.actionGC = QtGui.QAction(MainWindow)
        self.actionGC.setObjectName(_fromUtf8("actionGC"))
        self.actionGENESIS = QtGui.QAction(MainWindow)
        self.actionGENESIS.setObjectName(_fromUtf8("actionGENESIS"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/preferences.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon3)
        self.actionPreferences.setIconVisibleInMenu(True)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionTop = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/top.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTop.setIcon(icon4)
        self.actionTop.setIconVisibleInMenu(True)
        self.actionTop.setObjectName(_fromUtf8("actionTop"))
        self.actionBottom = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons/bottom.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBottom.setIcon(icon5)
        self.actionBottom.setIconVisibleInMenu(True)
        self.actionBottom.setObjectName(_fromUtf8("actionBottom"))
        self.actionNew = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icons/new.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon6)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionRemove = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("icons/remove.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove.setIcon(icon7)
        self.actionRemove.setIconVisibleInMenu(True)
        self.actionRemove.setObjectName(_fromUtf8("actionRemove"))
        self.actionImport = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("icons/import.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport.setIcon(icon8)
        self.actionImport.setIconVisibleInMenu(True)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionExport = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("icons/export.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport.setIcon(icon9)
        self.actionExport.setIconVisibleInMenu(True)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("icons/info.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon10)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionImport)
        self.toolBar.addAction(self.actionExport)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTop)
        self.toolBar.addAction(self.actionBottom)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDate)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPreferences)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionRemove)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionTop)
        self.menuEdit.addAction(self.actionBottom)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menuRun.addAction(self.actionFirstrun)
        self.menuRun.addAction(self.actionRerun)
        self.menuPlatform.addAction(self.actionPS1)
        self.menuPlatform.addAction(self.actionPS2)
        self.menuPlatform.addAction(self.actionPS3)
        self.menuPlatform.addAction(self.actionPSP)
        self.menuPlatform.addAction(self.actionPC)
        self.menuPlatform.addAction(self.actionNDS)
        self.menuPlatform.addAction(self.actionGBA)
        self.menuPlatform.addAction(self.actionSNES)
        self.menuPlatform.addAction(self.actionNES)
        self.menuPlatform.addAction(self.actionWII)
        self.menuPlatform.addAction(self.actionGC)
        self.menuPlatform.addAction(self.actionGENESIS)
        self.menuInsert.addAction(self.actionDate)
        self.menuInsert.addAction(self.menuPlatform.menuAction())
        self.menuInsert.addAction(self.menuRun.menuAction())
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuInsert.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "qmycrap", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuInsert.setTitle(_translate("MainWindow", "Insert", None))
        self.menuRun.setTitle(_translate("MainWindow", "Run", None))
        self.menuPlatform.setTitle(_translate("MainWindow", "Platform", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionDate.setText(_translate("MainWindow", "Date", None))
        self.actionFirstrun.setText(_translate("MainWindow", "Firstrun", None))
        self.actionRerun.setText(_translate("MainWindow", "Rerun", None))
        self.actionPS1.setText(_translate("MainWindow", "PS1", None))
        self.actionPS2.setText(_translate("MainWindow", "PS2", None))
        self.actionPS3.setText(_translate("MainWindow", "PS3", None))
        self.actionPSP.setText(_translate("MainWindow", "PSP", None))
        self.actionPC.setText(_translate("MainWindow", "PC", None))
        self.actionNDS.setText(_translate("MainWindow", "NDS", None))
        self.actionGBA.setText(_translate("MainWindow", "GBA", None))
        self.actionSNES.setText(_translate("MainWindow", "SNES", None))
        self.actionNES.setText(_translate("MainWindow", "NES", None))
        self.actionWII.setText(_translate("MainWindow", "WII", None))
        self.actionGC.setText(_translate("MainWindow", "GC", None))
        self.actionGENESIS.setText(_translate("MainWindow", "GENESIS", None))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences", None))
        self.actionTop.setText(_translate("MainWindow", "Top", None))
        self.actionBottom.setText(_translate("MainWindow", "Bottom", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionRemove.setText(_translate("MainWindow", "Remove", None))
        self.actionImport.setText(_translate("MainWindow", "Import", None))
        self.actionExport.setText(_translate("MainWindow", "Export", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

