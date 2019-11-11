from PyQt5						import 	QtCore, uic
from PyQt5.QtWidgets 	import   QTableWidgetItem
import pickle

from constant 					import const

class settings:
	EngineName	= {	'sqlite3':'SqlLite',
									'mysql':'MySql ( MariaDB )', 
									'firebird':'FireBird'}
	def_elems = {
		'$VERS':'0.1', 
		'DBEngine':'sqlite3', 
		'DBHost':'', 
		'DBPort':0, 
		'DBUser':'', 
		'DBPass':'', 
		'DBName':'db/gok.db', 
		'Language':'fr-fr'
		}
	elems		= {}
	dlg			= None
	fileName	= "settings.pref"
	
	def __init__(self,  theApp):
		self.app 		= theApp
		self.readFile()

	def actionSave(self):
		pt = self.dlg.pref_table
		self.elems[ self.last -1 ]
		for i in range(0, len( self.elems[ self.last -1 ]) ):
			e = pt.item(i, 0).text()
			self.elems[ self.last -1 ][ e ] = pt.item(i, 1).text()
		self.elems[0] = self.elems[ self.last -1 ]
		self.writeFile()
	
	def actionCombo( self, item ):
		None
		
	def showDialog(self):
		if self.dlg == None:
			self.dlg = uic.loadUi( const.prefDialog )
		self.retranslateUi( self.dlg )
		self.dlg.show()
		self.dlg.setModal( True )
		ret 	= self.dlg.exec()
		return ret
		
	def readFile(self):
		try:
			theFile		= open( self.fileName,  "rb")
			self.elems 	= pickle.load(  theFile )
			theFile.close()
			if not '$VERS' in self.elems:
				self.elems = self.del_elems
			if self.elems['$VERS'] is None:
				self.elems['$VERS'] = '0.1'
			
		except:
			self.elems = self.def_elems
			print( self.elems )
			self.writeFile()
			
	def writeFile(self):
		theFile		= open( self.fileName,  "wb")
		pickle.dump( self.elems, theFile )
		theFile.close()
		
	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Préferences"))
		Dialog.mdbLabel.setText(_translate("Dialog", "Moteur Base de Données"))
		Dialog.dbHostLabel.setText(_translate("Dialog", "DbHost"))
		Dialog.dbUserLabel.setText(_translate("Dialog", "DbUser"))
		Dialog.dbPassLabel.setText(_translate("Dialog", "DbPass"))
		Dialog.dbNameLabel.setText(_translate("Dialog", "DbName"))
		Dialog.dbPortLabel.setText(_translate("Dialog", "dbPort"))
