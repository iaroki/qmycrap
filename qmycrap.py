#!/usr/bin/env python

import os
import sys
import base64
import hashlib
import datetime
from Crypto import Random
from Crypto.Cipher import AES
from PyQt4 import QtCore, QtGui
from ui_qmycrap import Ui_MainWindow

class MyCrap_Window(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.initPreferences()
        self.initRootTree()

#        key = self.getKey()
#        self.decrypt(key, aes_filename, zip_filename)
#        self.decompress(zip_filename, txt_filename)
#        self.load()

        self.connect(self.treeView, QtCore.SIGNAL('clicked(QModelIndex)'), self.selectFile)
        self.connect(self.actionSave, QtCore.SIGNAL('triggered()'), self.save)
        self.connect(self.actionPswd, QtCore.SIGNAL('triggered()'), self.pswd)
        self.connect(self.actionTop, QtCore.SIGNAL('triggered()'), self.goTop)
        self.connect(self.actionBottom, QtCore.SIGNAL('triggered()'), self.goBottom)
        self.connect(self.actionDate, QtCore.SIGNAL('triggered()'), self.insertDate)
        self.connect(self.actionExit, QtCore.SIGNAL('triggered()'), self.exit)

    def initPreferences(self):
        self.preferences = QtCore.QSettings("preferences.cfg", QtCore.QSettings.IniFormat)  # reading cfg ini file
        self.preferences.setIniCodec('UTF-8')

    def initRootTree(self):
        self.treeFSM = QtGui.QFileSystemModel()
        self.treeMI = QtCore.QModelIndex()
        rootPath = self.preferences.value('files')
        rootPath = rootPath.toString()
        self.treeFSM.setRootPath(rootPath)
        self.treeMI = self.treeFSM.index(rootPath)

        self.treeView.setModel(self.treeFSM)
        for i in range(1, 4):
            self.treeView.hideColumn(i)
        self.treeView.setRootIndex(self.treeMI)

    def selectFile(self):
        currentIndex = self.treeView.currentIndex()
        filePath = self.treeFSM.filePath(currentIndex)
        self.statusbar.showMessage(filePath)
        self.preferences.setValue('current', filePath)
        self.preferences.sync()
        key = self.getKey()
        with open(filePath, 'rb') as f:
            data = f.read()
        decData = self.decrypt(key, data)

        self.textEdit.setPlainText(decData.decode('utf-8'))

    def pswd(self):
        pass

    def goTop(self):
        self.textEdit.verticalScrollBar().setValue(0)

    def goBottom(self):
        self.textEdit.verticalScrollBar().setValue(self.textEdit.verticalScrollBar().maximum())

    def insertDate(self):
        date = datetime.datetime.now().strftime("[%d/%m/%y]")
        self.textEdit.insertPlainText(date)

    def decrypt(self, key, data):
        unpad = lambda s: s[0:-ord(s[-1])]
        enc = data
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))

    def encrypt(self, key, data):
        BLOCK_SIZE = 16
        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
        raw = pad(data)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def load(self):
        f = open(txt_filename, 'r')
        data = f.read()
        f.close()
        self.textEdit.setPlainText(data.decode('utf-8'))
        self.clean()

    def save(self):
        key = self.getKey()
        data = self.textEdit.toPlainText()
        data = data.toUtf8()
        data = str(data)
        encData = self.encrypt(key, data)
        filePath = self.preferences.value('current')
        filePath = filePath.toString()
        with open(filePath, 'wb') as f:
            f.write(encData)
        self.statusbar.showMessage('Saved!')

    def clean(self):
        os.remove(zip_filename)
        os.remove(txt_filename)

    def exit(self):
        QtGui.qApp.quit()

    def getKey(self):
        with open(passkey, 'r') as f:
            data = f.read()
            key = hashlib.sha256(data).digest()
        return key

passkey = '/home/max/passkey.aes'
aes_filename = 'mycrap.aes'
zip_filename = 'mycrap.zip'
txt_filename = 'mycrap.txt'


app = QtGui.QApplication(sys.argv)

window = MyCrap_Window()
window.show()

sys.exit(app.exec_())
