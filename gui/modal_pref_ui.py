# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modal_pref.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
		Dialog.resize(519, 377)
		Dialog.setMouseTracking(True)
		Dialog.setFocusPolicy(QtCore.Qt.StrongFocus)
		Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		Dialog.setToolTip("")
		Dialog.setStatusTip("")
		Dialog.setAccessibleName("")
		Dialog.setAccessibleDescription("")
		Dialog.setAutoFillBackground(False)
		Dialog.setModal(True)
		self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(0, 340, 511, 32))
		self.buttonBox.setToolTip("")
		self.buttonBox.setStatusTip("")
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Save)
		self.buttonBox.setCenterButtons(False)
		self.buttonBox.setObjectName("buttonBox")
		self.formLayoutWidget = QtWidgets.QWidget(Dialog)
		self.formLayoutWidget.setGeometry(QtCore.QRect(0, 10, 511, 331))
		self.formLayoutWidget.setObjectName("formLayoutWidget")
		self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayout.setObjectName("formLayout")
		self.mdbLabel = QtWidgets.QLabel(self.formLayoutWidget)
		self.mdbLabel.setObjectName("mdbLabel")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.mdbLabel)
		self.mbbComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
		self.mbbComboBox.setObjectName("mbbComboBox")
		self.mbbComboBox.addItem("")
		self.mbbComboBox.setItemText(0, "SqlLite3")
		self.mbbComboBox.addItem("")
		self.mbbComboBox.setItemText(1, "MySql ( MariaDB )")
		self.mbbComboBox.addItem("")
		self.mbbComboBox.setItemText(2, "FireBird")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mbbComboBox)
		self.dbHostLabel = QtWidgets.QLabel(self.formLayoutWidget)
		self.dbHostLabel.setObjectName("dbHostLabel")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dbHostLabel)
		self.dbHostLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.dbHostLineEdit.setObjectName("dbHostLineEdit")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dbHostLineEdit)
		self.dbUserLabel = QtWidgets.QLabel(self.formLayoutWidget)
		self.dbUserLabel.setObjectName("dbUserLabel")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dbUserLabel)
		self.dbUserLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.dbUserLineEdit.setObjectName("dbUserLineEdit")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dbUserLineEdit)
		self.dbPassLabel = QtWidgets.QLabel(self.formLayoutWidget)
		self.dbPassLabel.setObjectName("dbPassLabel")
		self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.dbPassLabel)
		self.dbPassLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.dbPassLineEdit.setObjectName("dbPassLineEdit")
		self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dbPassLineEdit)
		self.dbNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
		self.dbNameLabel.setObjectName("dbNameLabel")
		self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.dbNameLabel)
		self.dbNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.dbNameLineEdit.setObjectName("dbNameLineEdit")
		self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dbNameLineEdit)

		self.retranslateUi(Dialog)
		self.buttonBox.accepted.connect(Dialog.accept)
		self.buttonBox.rejected.connect(Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Préferences"))
		self.mdbLabel.setText(_translate("Dialog", "Moteur Base de Données"))
		self.dbHostLabel.setText(_translate("Dialog", "DbHost"))
		self.dbUserLabel.setText(_translate("Dialog", "DbUser"))
		self.dbPassLabel.setText(_translate("Dialog", "DbPass"))
		self.dbNameLabel.setText(_translate("Dialog", "DbName"))
