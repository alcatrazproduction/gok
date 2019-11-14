#!/usr/bin/env python3
#.######################################################################################################
#	Dispatcher for the event in the App																						
#	Do all the events stuff																										
#	Creator:		Yves Huguenin																									
#	Date:			09.11.2019																										
#	Version:		0.1																												
#																																		
#.######################################################################################################

from PyQt5 				import QtCore, QtGui, QtWidgets
from modules.gfx		import CiterneGfx
from datetime 			import	datetime

def createTab(self,  ip,  tSerial, tLevel, tFull, tHeight ):
	global	_translate
	_translate 											= QtCore.QCoreApplication.translate
	tab														= {}
	try:
		tab['tab1'] 									= QtWidgets.QWidget()
		tab['tab1'] .setObjectName("{}".format( tSerial ))
		tab['horizontalLayoutWidget'] 	= QtWidgets.QWidget(tab['tab1'] )
		tab['horizontalLayoutWidget'].setGeometry(QtCore.QRect(-1, -1, 641, 431))
		tab['horizontalLayoutWidget'].setObjectName("horizontalLayoutWidget")
		tab['horizontalLayout'] = QtWidgets.QHBoxLayout(tab['horizontalLayoutWidget'])
		tab['horizontalLayout'].setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
		tab['horizontalLayout'].setContentsMargins(0, 0, 0, 0)
		tab['horizontalLayout'].setSpacing(2)
		tab['horizontalLayout'].setObjectName("horizontalLayout")
		tab['formLayout'] = QtWidgets.QFormLayout()
		tab['formLayout'].setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
		tab['formLayout'].setContentsMargins(5, 12, 5, -1)
		tab['formLayout'].setVerticalSpacing(11)
		tab['formLayout'].setObjectName("formLayout")
		tab['label'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label'].setObjectName("label")
		slot												= 0
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.LabelRole, tab['label'])
		tab['cPercent'] = QtWidgets.QProgressBar(tab['horizontalLayoutWidget'])
		tab['cPercent'].setProperty("value", 38)
		tab['cPercent'].setAlignment(QtCore.Qt.AlignCenter)
		tab['cPercent'].setInvertedAppearance(False)
		tab['cPercent'].setObjectName("cPercent")
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.FieldRole, tab['cPercent'])
		tab['label_2'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_2'].setObjectName("label_2")
		slot 											+= 1
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.LabelRole, tab['label_2'])
		tab['cCapacity'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cCapacity'].setObjectName("cCapacity")
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.FieldRole, tab['cCapacity'])
		tab['label_3'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_3'].setObjectName("label_3")
		slot 											+= 1
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.LabelRole, tab['label_3'])
		tab['cSerial'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cSerial'].setObjectName("cSerial")
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.FieldRole, tab['cSerial'])
		tab['label_4'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_4'].setObjectName("label_4")
		slot 										+= 1
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.LabelRole, tab['label_4'])
		tab['cDesign'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cDesign'].setObjectName("cDesign")
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.FieldRole, tab['cDesign'])
		tab['label_5'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_5'].setObjectName("label_5")
		slot 										+= 1
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.LabelRole, tab['label_5'])
		tab['cUnite'] = QtWidgets.QComboBox(tab['horizontalLayoutWidget'])
		tab['cUnite'].setCurrentText("")
		tab['cUnite'].setObjectName("cUnite")
		for x in range(9):
			tab['cUnite'].addItem("")
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.FieldRole, tab['cUnite'])
		tab['label_6'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_6'].setObjectName("label_6")
		slot 										+= 1
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.LabelRole, tab['label_6'])
		tab['cType'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cType'].setObjectName("cType")
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.FieldRole, tab['cType'])
		tab['label_7'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_7'].setObjectName("label_7")
		slot 										+= 1
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.LabelRole, tab['label_7'])
		tab['cFull'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cFull'].setObjectName("cFull")
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.FieldRole, tab['cFull'])
		tab['label_8'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_8'].setObjectName("label_8")
		slot 										+= 1
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.LabelRole, tab['label_8'])
		tab['cHeight'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cHeight'].setObjectName("cHeight")
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.FieldRole, tab['cHeight'])
		tab['label_9'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_9'].setObjectName("label_9")
		slot 										+= 1
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.LabelRole, tab['label_9'])
		tab['cTemp'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cTemp'].setObjectName("cTemp")
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.FieldRole, tab['cTemp'])
		tab['label_10'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_10'].setObjectName("label_10")
		slot 										+= 1
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.LabelRole, tab['label_10'])
		tab['cTime'] = QtWidgets.QDateTimeEdit(tab['horizontalLayoutWidget'])
		tab['cTime'].setInputMethodHints(QtCore.Qt.ImhNone)
		tab['cTime'].setReadOnly(True)
		tab['cTime'].setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
		tab['cTime'].setKeyboardTracking(False)
		tab['cTime'].setObjectName("cTime")
		tab['cTime'].setDateTime( datetime.today())		
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.FieldRole, tab['cTime'])
		tab['horizontalLayout'].addLayout(tab['formLayout'])
		tab['dCiterne'] = QtWidgets.QGraphicsView(tab['horizontalLayoutWidget'])
		tab['dCiterne'].setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(tab['dCiterne'].sizePolicy().hasHeightForWidth())
		tab['dCiterne'].setSizePolicy(sizePolicy)
		tab['dCiterne'].setMinimumSize(QtCore.QSize(256, 429))
		tab['dCiterne'].setBaseSize(QtCore.QSize(256, 429))
		tab['dCiterne'].setAcceptDrops(False)
		tab['dCiterne'].setFrameShape(QtWidgets.QFrame.NoFrame)
		tab['dCiterne'].setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		tab['dCiterne'].setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
		brush.setStyle(QtCore.Qt.NoBrush)
		tab['dCiterne'].setForegroundBrush(brush)
		tab['dCiterne'].setSceneRect(QtCore.QRectF(0.0, 0.0, 256.0, 429.0))
		tab['dCiterne'].setObjectName("dCiterne")
		tab['horizontalLayout'].addWidget(tab['dCiterne'])
		tab['label_51'] 		= QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_51'].setObjectName("label_51")
		slot += 1
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.LabelRole, tab['label_51'])
		tab['cAction'] 			= QtWidgets.QComboBox(tab['horizontalLayoutWidget'])
		tab['cAction'].setObjectName("cAction")
		for x in range(3):
			tab['cAction'].addItem("")
			tab['cAction'].setItemData( x,  tSerial )
		tab['formLayout'].setWidget( slot, QtWidgets.QFormLayout.FieldRole, tab['cAction'])
		tab['cAction'].activated[int].connect(self.tabSelectedAction)  
		
		self.tabs[ tSerial ] = tab
		tab[ 'cPercent' ].setValue( tLevel / tFull * 100)
		tab[ 'cCapacity' ].setText("{}".format( tLevel ))
		tab[ 'cFull' ].setText("{}".format( tFull ))
		tab[ 'cHeight' ].setText("{}".format( tHeight ))
		tab[ 'cSerial' ].setText("{}".format( tSerial ))
		addTab( self,  tSerial )
		tab[ 'gfx' ]	= CiterneGfx( tab['dCiterne'] )
		tab[ 'gfx' ].draw( tLevel, tFull)
# Translation...
		tab[ 'label' ].setText(_translate("mainWindow", "Pourcentage de remplissage:"))
		tab[ 'label_2' ].setText(_translate("mainWindow", "Litrage:"))
		tab[ 'label_3' ].setText(_translate("mainWindow", "Citerne / No de serie:"))
		tab[ 'label_4' ].setText(_translate("mainWindow", "Désignation de la citerne:"))
		tab[ 'label_5' ].setText(_translate("mainWindow", "Unité:"))
		tab[ 'label_6' ].setText(_translate("mainWindow", "Type de citerne:"))
		tab[ 'label_7' ].setText(_translate("mainWindow", "Volume de la citerne:"))
		tab[ 'label_8' ].setText(_translate("mainWindow", "Hauteur de la citerne"))
		tab[ 'label_9' ].setText(_translate("mainWindow", "Temperature:"))
		tab[ 'label_10' ].setText(_translate("mainWindow", "Date / Heure de la mesure:"))
		tab[ 'cTime' ].setDisplayFormat(_translate("mainWindow", "dd.MM.yyyy HH:mm"))
		
		tab[ 'cUnite' ].setCurrentText(_translate("mainWindow", "Litres"))
		tab[ 'cUnite' ].setItemText(0, _translate("mainWindow", "Litres"))
		tab[ 'cUnite' ].setItemText(1, _translate("mainWindow", "Metre Cube"))
		tab[ 'cUnite' ].setItemText(2, _translate("mainWindow", "Pourcent"))
		tab[ 'cUnite' ].setItemText(3, _translate("mainWindow", "Hauteur(m)"))
		tab[ 'cUnite' ].setItemText(4, _translate("mainWindow", "Kilogramme"))
		tab[ 'cUnite' ].setItemText(5, _translate("mainWindow", "IG"))
		tab[ 'cUnite' ].setItemText(6, _translate("mainWindow", "UG"))
		tab[ 'cUnite' ].setItemText(7, _translate("mainWindow", "Tonne"))
		tab[ 'cUnite' ].setItemText(8, _translate("mainWindow", "milliBar"))
		tab[ 'cUnite' ].setItemText(9, _translate("mainWindow", "kiloPascal"))
		
		tab[ 'label_51' ].setText(_translate("mainWindow", "Action:"))
		tab[ 'cAction' ].setCurrentText(_translate("mainWindow", "E-Mails..."))
		tab[ 'cAction' ].setItemText(0, _translate("mainWindow", "E-Mails..."))
		tab[ 'cAction' ].setItemText(1, _translate("mainWindow", "SMS..."))
		tab[ 'cAction' ].setItemText(2, _translate("mainWindow", "SMNP...."))
		
	except Exception as inst:
		print(inst) 	


def addTab(self,  tSerial ):
	self.win.tabTank.addTab(self.tabs[ tSerial ]["tab1"], "{}".format( tSerial ))
