#!/usr/bin/env python3
#######################################################################################################
#	Dispatcher for the event in the App																						#
#	Do all the events stuff																										#
#	Creator:		Yves Huguenin																									#
#	Date:			28.10.2019																										#
#	Version:		0.1																												#
#																																		#
#######################################################################################################
from 		PyQt5 					import QtCore, QtGui, QtWidgets
from 		modules.gfx			import CiterneGfx
from 		datetime 				import	datetime
import	gui.tank_plane
class dispatcher( QtCore.QObject ):
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
		_translate = QtCore.QCoreApplication.translate
		try:			
			if tSerial in self.tabs:
				tab		= self.tabs[tSerial]
				tab[ 'cPercent' ].setValue( tLevel / tFull * 100)
				tab[ 'cCapacity' ].setText("{}".format(tLevel))
				tab[ 'cFull' ].setText("{}".format(tFull))
				tab[ 'cHeight' ].setText("{}".format(tHeight))
				tab[ 'gfx' ].draw( tLevel, tFull)
				tab['cTime'].setDateTime( datetime.today())		
			else:
				gui.tank_plane.createTab( self,  ip, tSerial, tLevel, tFull, tHeight )

			status	= self.win.statusBar()
			status.showMessage(_translate("dispatcher.py", 
				"{} serial {} form {} at {:%d-%m-%Y %H:%M}").format( tLevel,  tSerial,  ip, datetime.today() )
			)
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

	def tabSelectedAction(self, id):
		wg		= self.win.tabTank.currentWidget()
		print(wg.objectName())
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
