# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClientForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chat_window_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.chat_window_text.setReadOnly(True)
        self.chat_window_text.setObjectName("chat_window_text")
        self.verticalLayout.addWidget(self.chat_window_text)
        self.text_to_send = QtWidgets.QLineEdit(self.centralwidget)
        self.text_to_send.setObjectName("text_to_send")
        self.verticalLayout.addWidget(self.text_to_send)
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setObjectName("submit_button")
        self.verticalLayout.addWidget(self.submit_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chat_window_text.setPlaceholderText(_translate("MainWindow", "Здесь будут сообщения..."))
        self.text_to_send.setPlaceholderText(_translate("MainWindow", "Введите текст сообщения"))
        self.submit_button.setText(_translate("MainWindow", "Отправить"))
