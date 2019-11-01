#!/usr/bin/env python3
#######################################################################################################
#	Dispatcher for the event in the App																						#
#	Do all the events stuff																										#
#	Creator:		Yves Huguenin																									#
#	Date:			28.10.2019																										#
#	Version:		0.1																												#
#																																		#
#######################################################################################################
from PyQt5 				import QtCore, QtGui, QtWidgets
from modules.gfx		import CiterneGfx

class dispatcher( QtCore.QObject ):
	addTabSignal 			= QtCore.pyqtSignal( int )
	createTabSignal 		= QtCore.pyqtSignal( str, int, int, int, int )
	receivedTankSignal	= QtCore.pyqtSignal( str, int, int, int, int )
####################################################################################################
#																																	#
#																																	#
####################################################################################################

	def __init__(self, theWin, theGest):
		super().__init__()
		self.win		= theWin
		self.app		= theGest.app
		self.Main		= theGest
		self.tabs		= {}
		self.addTabSignal.connect( self.addTab )
		self.createTabSignal.connect( self.createTab )
		self.receivedTankSignal.connect( self._updateTank )

		
####################################################################################################
#																																	#
#																																	#
####################################################################################################

	def dateDecompte(self):
		None
		
####################################################################################################
#																																	#
#																																	#
####################################################################################################

	def dateTransaction(self):
		None
		
####################################################################################################
#																																	#
#																																	#
####################################################################################################

	def createExcel(self):
		None
		
####################################################################################################
#																																	#
#																																	#
####################################################################################################

	def createPdf(self):
		None
		
####################################################################################################
#																																	#
#																																	#
####################################################################################################

	def  setCards(self,  theCards):
		None
		
####################################################################################################
#																																	#
#																																	#
####################################################################################################
	def _updateTank( self,  ip, tSerial, tLevel, tFull, tHeight ):
		try:			
			if tSerial in self.tabs:
				tab		= self.tabs[tSerial]
				tab[ 'cPercent' ].setValue( tLevel / tFull * 100)
				tab[ 'cCapacity' ].setText("{}".format(tLevel))
				tab[ 'cFull' ].setText("{}".format(tFull))
				tab[ 'cHeight' ].setText("{}".format(tHeight))
				tab[ 'gfx' ].draw( tLevel, tFull)
			else:
				self.createTabSignal.emit( ip, tSerial, tLevel, tFull, tHeight )
		except Exception as inst:
			print(inst)
			
	def updateTank( self,  ip, id, level, capacity, high ):
		global	_translate
		
		print("Callback called")
		try:
			tSerial		= int( id, 16)
			tLevel		= int( level ) / 100.0
			tFull			= int( capacity, 16)
			tHeight	= int( high, 16)
			
			self.receivedTankSignal.emit( ip, tSerial, tLevel, tFull, tHeight )
		except Exception as inst:
			print(inst) 	

	def createTab(self,  ip,  tSerial, tLevel, tFull, tHeight ):
		global	_translate
		_translate 		= QtCore.QCoreApplication.translate
		tab						= {}

		tab['tab1'] 		= QtWidgets.QWidget()
		tab['tab1'] .setObjectName("{}".format( tSerial ))
		tab['horizontalLayoutWidget'] = QtWidgets.QWidget(tab['tab1'] )
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
		tab['formLayout'].setVerticalSpacing(12)
		tab['formLayout'].setObjectName("formLayout")
		tab['label'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label'].setObjectName("label")
		tab['formLayout'].setWidget(0, QtWidgets.QFormLayout.LabelRole, tab['label'])
		tab['cPercent'] = QtWidgets.QProgressBar(tab['horizontalLayoutWidget'])
		tab['cPercent'].setProperty("value", 38)
		tab['cPercent'].setAlignment(QtCore.Qt.AlignCenter)
		tab['cPercent'].setInvertedAppearance(False)
		tab['cPercent'].setObjectName("cPercent")
		tab['formLayout'].setWidget(0, QtWidgets.QFormLayout.FieldRole, tab['cPercent'])
		tab['label_2'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_2'].setObjectName("label_2")
		tab['formLayout'].setWidget(2, QtWidgets.QFormLayout.LabelRole, tab['label_2'])
		tab['cCapacity'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cCapacity'].setObjectName("cCapacity")
		tab['formLayout'].setWidget(2, QtWidgets.QFormLayout.FieldRole, tab['cCapacity'])
		tab['label_3'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_3'].setObjectName("label_3")
		tab['formLayout'].setWidget(3, QtWidgets.QFormLayout.LabelRole, tab['label_3'])
		tab['cSerial'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cSerial'].setObjectName("cSerial")
		tab['formLayout'].setWidget(3, QtWidgets.QFormLayout.FieldRole, tab['cSerial'])
		tab['label_4'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_4'].setObjectName("label_4")
		tab['formLayout'].setWidget(4, QtWidgets.QFormLayout.LabelRole, tab['label_4'])
		tab['cDesign'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cDesign'].setObjectName("cDesign")
		tab['formLayout'].setWidget(4, QtWidgets.QFormLayout.FieldRole, tab['cDesign'])
		tab['label_5'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_5'].setObjectName("label_5")
		tab['formLayout'].setWidget(5, QtWidgets.QFormLayout.LabelRole, tab['label_5'])
		tab['cUnite'] = QtWidgets.QComboBox(tab['horizontalLayoutWidget'])
		tab['cUnite'].setCurrentText("")
		tab['cUnite'].setObjectName("cUnite")
		tab['formLayout'].setWidget(5, QtWidgets.QFormLayout.FieldRole, tab['cUnite'])
		tab['label_6'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_6'].setObjectName("label_6")
		tab['formLayout'].setWidget(6, QtWidgets.QFormLayout.LabelRole, tab['label_6'])
		tab['cType'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cType'].setObjectName("cType")
		tab['formLayout'].setWidget(6, QtWidgets.QFormLayout.FieldRole, tab['cType'])
		tab['label_7'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_7'].setObjectName("label_7")
		tab['formLayout'].setWidget(7, QtWidgets.QFormLayout.LabelRole, tab['label_7'])
		tab['cFull'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cFull'].setObjectName("cFull")
		tab['formLayout'].setWidget(7, QtWidgets.QFormLayout.FieldRole, tab['cFull'])
		tab['label_8'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_8'].setObjectName("label_8")
		tab['formLayout'].setWidget(8, QtWidgets.QFormLayout.LabelRole, tab['label_8'])
		tab['cHeight'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cHeight'].setObjectName("cHeight")
		tab['formLayout'].setWidget(8, QtWidgets.QFormLayout.FieldRole, tab['cHeight'])
		tab['label_9'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_9'].setObjectName("label_9")
		tab['formLayout'].setWidget(9, QtWidgets.QFormLayout.LabelRole, tab['label_9'])
		tab['cTemp'] = QtWidgets.QLineEdit(tab['horizontalLayoutWidget'])
		tab['cTemp'].setObjectName("cTemp")
		tab['formLayout'].setWidget(9, QtWidgets.QFormLayout.FieldRole, tab['cTemp'])
		tab['label_10'] = QtWidgets.QLabel(tab['horizontalLayoutWidget'])
		tab['label_10'].setObjectName("label_10")
		tab['formLayout'].setWidget(10, QtWidgets.QFormLayout.LabelRole, tab['label_10'])
		tab['cTime'] = QtWidgets.QDateTimeEdit(tab['horizontalLayoutWidget'])
		tab['cTime'].setInputMethodHints(QtCore.Qt.ImhNone)
		tab['cTime'].setReadOnly(True)
		tab['cTime'].setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
		tab['cTime'].setKeyboardTracking(False)
		tab['cTime'].setObjectName("cTime")
		tab['formLayout'].setWidget(10, QtWidgets.QFormLayout.FieldRole, tab['cTime'])
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
		
		self.tabs[ tSerial ] = tab
		tab[ 'cPercent' ].setValue( tLevel / tFull * 100)
		tab[ 'cCapacity' ].setText("{}".format( tLevel ))
		tab[ 'cFull' ].setText("{}".format( tFull ))
		tab[ 'cHeight' ].setText("{}".format( tHeight ))
		tab[ 'cSerial' ].setText("{}".format( tSerial ))
		self.addTabSignal.emit( tSerial )
		tab[ 'gfx' ]	= CiterneGfx( tab['dCiterne'] )
		tab[ 'gfx' ].draw( tLevel, tFull)
		
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

	def addTab(self,  tSerial ):
		self.win.tabTank.addTab(self.tabs[ tSerial ]["tab1"], "{}".format( tSerial ))

####################################################################################################
#																																	#
#																																	#
####################################################################################################

	def  setAbout(self,  theAbout):
		self.about	= theAbout
		
####################################################################################################
#																																	#
#																																	#
####################################################################################################

	def doAbout(self):
		self.about.setModal( True )
		self.about.show()
		
####################################################################################################
#																																	#
#																																	#
####################################################################################################

	def resizeWindow(self):
		win	= self.win
		size	= win.size()
		msize	= 20
		tsize	= msize + 20
		vsize	= tsize + 20
		hsize	= 20

		
####################################################################################################
#																																	#
#																																	#
####################################################################################################

	def doPreferences(self):
		
		ret =	self.Main.thePref.showDialog()
		if ret == 1:
			None
