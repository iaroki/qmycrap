#!/usr/bin/env python

import os
import sys
import base64
import hashlib
import datetime
import subprocess
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

        self.connect(self.treeView, QtCore.SIGNAL('clicked(QModelIndex)'), self.selectFile)
        self.connect(self.treeView, QtCore.SIGNAL('entered(QModelIndex)'), self.selectFile)
        self.connect(self.actionSave, QtCore.SIGNAL('triggered()'), self.saveFile)
        self.connect(self.actionNew, QtCore.SIGNAL('triggered()'), self.newFile)
        self.connect(self.actionImport, QtCore.SIGNAL('triggered()'), self.importFile)
        self.connect(self.actionExport, QtCore.SIGNAL('triggered()'), self.exportFile)
        self.connect(self.actionRemove, QtCore.SIGNAL('triggered()'), self.removeFile)
        self.connect(self.actionSync, QtCore.SIGNAL('triggered()'), self.syncFiles)
        self.connect(self.actionTop, QtCore.SIGNAL('triggered()'), self.goTop)
        self.connect(self.actionBottom, QtCore.SIGNAL('triggered()'), self.goBottom)
        self.connect(self.actionDate, QtCore.SIGNAL('triggered()'), self.insertDate)
        self.connect(self.actionPS1, QtCore.SIGNAL('triggered()'), self.insertPlatformPS1)
        self.connect(self.actionPS2, QtCore.SIGNAL('triggered()'), self.insertPlatformPS2)
        self.connect(self.actionPS3, QtCore.SIGNAL('triggered()'), self.insertPlatformPS3)
        self.connect(self.actionPSP, QtCore.SIGNAL('triggered()'), self.insertPlatformPSP)
        self.connect(self.actionPC, QtCore.SIGNAL('triggered()'), self.insertPlatformPC)
        self.connect(self.actionNES, QtCore.SIGNAL('triggered()'), self.insertPlatformNES)
        self.connect(self.actionSNES, QtCore.SIGNAL('triggered()'), self.insertPlatformSNES)
        self.connect(self.actionGC, QtCore.SIGNAL('triggered()'), self.insertPlatformGC)
        self.connect(self.actionWII, QtCore.SIGNAL('triggered()'), self.insertPlatformWII)
        self.connect(self.actionGBA, QtCore.SIGNAL('triggered()'), self.insertPlatformGBA)
        self.connect(self.actionNDS, QtCore.SIGNAL('triggered()'), self.insertPlatformNDS)
        self.connect(self.actionGENESIS, QtCore.SIGNAL('triggered()'), self.insertPlatformGENESIS)
        self.connect(self.actionFirstrun, QtCore.SIGNAL('triggered()'), self.insertFirstrun)
        self.connect(self.actionRerun, QtCore.SIGNAL('triggered()'), self.insertRerun)
        self.connect(self.actionAbout, QtCore.SIGNAL('triggered()'), self.about)
        self.connect(self.actionExit, QtCore.SIGNAL('triggered()'), self.exit)

    def initPreferences(self):
        self.preferences = QtCore.QSettings("preferences.cfg", QtCore.QSettings.IniFormat)  # reading cfg ini file
        self.preferences.setIniCodec('UTF-8')

        state = self.preferences.value('state')
        state = state.toByteArray()
        self.restoreState(state)

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

        currentIndex = self.preferences.value('current')
        currentIndex = currentIndex.toString()
        currentIndex = currentIndex.toUtf8()
        currentIndex = str(currentIndex)
        if os.path.isfile(currentIndex):
            if self.checkLastLoad():
                self.treeView.setCurrentIndex(self.treeFSM.index(currentIndex.decode('utf-8')))
                self.loadFile(currentIndex)

    def selectFile(self):
        currentIndex = self.treeView.currentIndex()
        filePath = self.treeFSM.filePath(currentIndex)
        self.preferences.setValue('current', filePath)
        self.preferences.sync()
        filePath = filePath.toUtf8()
        filePath = str(filePath)
        self.loadFile(filePath)

    def newFile(self):
        selectDialog = QtGui.QFileDialog()
        newFilePath = selectDialog.getSaveFileName(self, 'Name of a new file:', 'crap', 'AES Files (*.aes)')
        newFilePath = newFilePath.toUtf8()
        newFilePath = str(newFilePath)
        if not newFilePath.endswith('.aes'):
            newFilePath = newFilePath + '.aes'
        newData = '<new file>'
        key = self.getKey()
        encData = self.encrypt(key, newData)
        with open(newFilePath, 'wb') as f:
            f.write(encData)
        self.preferences.setValue('current', newFilePath)
        self.preferences.sync()
        self.initRootTree()

    def importFile(self):
        homeDir = os.path.expanduser('~')
        filesDir = self.preferences.value('files')
        filesDir = filesDir.toString()
        filesDir = filesDir.toUtf8()
        filesDir = str(filesDir)
        key = self.getKey()
        selectDialog = QtGui.QFileDialog()
        filePath = selectDialog.getOpenFileName(self, 'Select file:', homeDir, 'TXT Files (*.txt)')
        filePath = filePath.toUtf8()
        filePath = str(filePath)
        fileName = os.path.splitext(filePath)[0]    # path without extension
        fileName = os.path.basename(fileName)       # file name without extension
        fileName = fileName + '.aes'
        fullPath = os.path.join(filesDir, fileName)
        with open(filePath, 'rb') as f:
            data = f.read()
        encData = self.encrypt(key, data)
        with open(fullPath, 'wb') as f:
            f.write(encData)

        self.preferences.setValue('current', fullPath.decode('utf-8'))
        self.preferences.sync()
        self.initRootTree()
        self.statusbar.showMessage('Imported!')

    def exportFile(self):
        homeDir = os.path.expanduser('~')
        data = self.textEdit.toPlainText()
        data = data.toUtf8()
        data = str(data)
        selectDialog = QtGui.QFileDialog()
        filePath = selectDialog.getSaveFileName(self, 'Name of the file:', homeDir, 'TXT Files (*.txt)')
        filePath = filePath.toUtf8()
        filePath = str(filePath)
        if not filePath.endswith('.txt'):
            filePath = filePath + '.txt'
        with open(filePath, 'wb') as f:
            f.write(data)
        self.statusbar.showMessage('Exported!')

    def removeFile(self):
        filePath = self.preferences.value('current')
        filePath = filePath.toString()
        reply = QtGui.QMessageBox.question(self, 'DELETION', 'Really delete?\n' + filePath, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            filePath = str(filePath.toUtf8())
            filePath = filePath.decode('utf-8')
            os.remove(os.path.abspath(filePath))
            self.textEdit.clear()
            self.statusbar.showMessage('Deleted!')

    def syncFiles(self):
        filesPath = self.preferences.value('files')
        syncPath = self.preferences.value('syncpath')
        filesPath = filesPath.toString()
        filesPath = filesPath.toUtf8()
        filesPath = str(filesPath)
        syncPath = syncPath.toString()
        syncPath = syncPath.toUtf8()
        syncPath = str(syncPath)
        subprocess.call(['rsync', '-a', filesPath, syncPath])
        self.statusbar.showMessage('Synchronized!')

    def goTop(self):
        self.textEdit.verticalScrollBar().setValue(0)

    def goBottom(self):
        self.textEdit.verticalScrollBar().setValue(self.textEdit.verticalScrollBar().maximum())

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

    def loadFile(self, filePath):
        key = self.getKey()
        with open(filePath.decode('utf-8'), 'rb') as f:
            data = f.read()
        decData = self.decrypt(key, data)
        self.statusbar.showMessage(filePath.decode('utf-8'))
        self.textEdit.setPlainText(decData.decode('utf-8'))

    def saveFile(self):
        key = self.getKey()
        data = self.textEdit.toPlainText()
        data = data.toUtf8()
        data = str(data)
        encData = self.encrypt(key, data)
        filePath = self.preferences.value('current')
        filePath = filePath.toString()
        filePath = filePath.toUtf8()
        filePath = str(filePath)
        with open(filePath, 'wb') as f:
            f.write(encData)
        self.statusbar.showMessage('Saved!')

        state = self.saveState()
        self.preferences.setValue('state', state)
        self.preferences.sync()

    def checkLastLoad(self):
        state = self.preferences.value('autoload')
        state = state.toBool()
        if state:
            return True
        else:
            return False

    def exit(self):
        QtGui.qApp.quit()

    def getKey(self):
        passkey = self.preferences.value('keyfile')
        passkey = passkey.toString()
        passkey = passkey.toUtf8()
        passkey = str(passkey)
        with open(passkey, 'r') as f:
            data = f.read()
            key = hashlib.sha256(data).digest()
        return key

    def insertDate(self):
        date = datetime.datetime.now().strftime('[%d/%m/%Y] ')
        self.textEdit.insertPlainText(date)

    def insertPlatformPS1(self):
        platform = '(PS1) '
        self.textEdit.insertPlainText(platform)

    def insertPlatformPS1(self):
        platform = ' (PS1) '
        self.textEdit.insertPlainText(platform)

    def insertPlatformPS2(self):
        platform = ' (PS2) '
        self.textEdit.insertPlainText(platform)

    def insertPlatformPS3(self):
        platform = ' (PS3) '
        self.textEdit.insertPlainText(platform)

    def insertPlatformPSP(self):
        platform = ' (PSP) '
        self.textEdit.insertPlainText(platform)

    def insertPlatformPC(self):
        platform = ' (PC) '
        self.textEdit.insertPlainText(platform)

    def insertPlatformNES(self):
        platform = ' (NES) '
        self.textEdit.insertPlainText(platform)

    def insertPlatformSNES(self):
        platform = ' (SNES) '
        self.textEdit.insertPlainText(platform)

    def insertPlatformGC(self):
        platform = ' (GC) '
        self.textEdit.insertPlainText(platform)

    def insertPlatformWII(self):
        platform = ' (WII) '
        self.textEdit.insertPlainText(platform)

    def insertPlatformGBA(self):
        platform = ' (GBA) '
        self.textEdit.insertPlainText(platform)

    def insertPlatformNDS(self):
        platform = ' (NDS) '
        self.textEdit.insertPlainText(platform)

    def insertPlatformGENESIS(self):
        platform = ' (GENESIS) '
        self.textEdit.insertPlainText(platform)

    def insertFirstrun(self):
        run = '<firstrun>'
        self.textEdit.insertPlainText(run)

    def insertRerun(self):
        run = '<rerun>'
        self.textEdit.insertPlainText(run)

    def about(self):
        QtGui.QMessageBox.information(self, 'About qmycrap',
        '<img src="./icons/app.png"><br><b>qmycrap 0.999</b><br>(c) 2014 Anonymous')

passkey = '/home/max/passkey.aes'

app = QtGui.QApplication(sys.argv)

window = MyCrap_Window()
window.show()

sys.exit(app.exec_())
