# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
		Dialog.resize(561, 390)
		Dialog.setWindowTitle("A Propos")
		Dialog.setSizeGripEnabled(True)
		self.logo = QtWidgets.QLabel(Dialog)
		self.logo.setGeometry(QtCore.QRect(0, 0, 551, 261))
		self.logo.setText("")
		self.logo.setPixmap(QtGui.QPixmap("resources/logo.png"))
		self.logo.setObjectName("logo")
		self.info = QtWidgets.QLabel(Dialog)
		self.info.setGeometry(QtCore.QRect(0, 0, 561, 31))
		self.info.setText("")
		self.info.setObjectName("info")
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(20, 230, 511, 151))
		self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label.setObjectName("label")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">(c) Yves Huguenin 2019</span><br/></p><p><span style=\" font-weight:600;\">KSW Technik S.A.<br/>Chemin des Dailles 4<br/>1053 Cugy (VD)</span><br/></p><p><span style=\" font-weight:600;\">Tel: 021 731 9340<br/>Fax: 021 731 5005<BR><a href=\"https://www.kswtech.com/en\"><span style=\" text-decoration: underline; color:#0000ff;\">KSW Tech</span></a></p></body></html>"))
import gok_rc
