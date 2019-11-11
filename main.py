#!/usr/bin/env python3
#######################################################################################################
#	Main class ( gestion) for the app																						#
#	Was the first writing in no class, don the main loop and init all the stuff								#
#	Creator:		Yves Huguenin																									#
#	Date:			28.10.2019																										#
#	Version:		0.1																												#
#																																		#
#######################################################################################################
from PyQt5 					import	uic, QtCore
from PyQt5.QtGui			import	QImage ,  QPixmap
from PyQt5.QtWidgets 	import 	QMessageBox


from datetime 				import	date
from time						import	sleep

from theApp					import	theApp
from settings 					import	settings
from dispatcher 				import dispatcher
from constant					import const

from modules.tcpip		import listener
from modules.sql			import db
global _translate

class gestion:
	def __init__(self):
		global _translate
		global translator
		self.app 			= theApp([])
		
		translator			= QtCore.QTranslator()
#		_translate.load("hellotr_la");
		self.app.installTranslator(translator)
		_translate = QtCore.QCoreApplication.translate
		self.thePref 		= settings( self.app )
		self.about		= uic.loadUi( const.aboutWindow)
#		logo 				= QImage( const.logoFile )
#		self.about.logo.setPixmap(QPixmap.fromImage(logo))
#		self.about.info.setText("Initialising Application")
		self.about.show()
		sleep(0.1)
		
	def initDatabase(self):
		
		thePref			= self.thePref
		

		conn = db( 	thePref.elems['DBHost'], 
							thePref.elems['DBName'], 
							int( thePref.elems['DBPort'] ), 
							thePref.elems['DBUser'], 
							thePref.elems['DBPass'], 
							thePref.elems['DBEngine'] )
		self.db	= conn
		
	def initApplication(self):
		
		global primaryScreen
		global _translate
		
		win 					= uic.loadUi( const.mainWindow )
		dispatch			= dispatcher( win, self )
		primaryScreen	= self.app.primaryScreen()
		scrSize				= primaryScreen.size()
		win.move( scrSize.width()/2 - win.width()/2, scrSize.height()/2 - win.width()/2 )
		
	
		win.setWindowTitle(_translate("mainWindow", "KSW_Gok"))
		win.menuFichier.setTitle(_translate("mainWindow", "Fic&hier"))
		win.actionQuitter.setText(_translate("mainWindow", "&Quitter"))
		win.menuHelp.setTitle(_translate("mainWindow", "Aide"))
		win.menuLangues.setTitle(_translate("mainWindow", "Langues"))
		win.actionQuitter.setText(_translate("mainWindow", "&Quitter"))
		win.actionApropos.setText(_translate("mainWindow", "A propos"))
		win.actionFran_ais.setText(_translate("mainWindow", "Français"))
		win.actionItalien.setText(_translate("mainWindow", "Italien"))
		win.actionAllemand.setText(_translate("mainWindow", "Allemand"))
		win.actionAnglais.setText(_translate("mainWindow", "Anglais"))
		win.actionPr_ferences.setText(_translate("mainWindow", "Préferences..."))


			

		self.win			= win
		self.status		= win.statusBar()
		self.status.showMessage(_translate("main.py", "appReady"))
		self.dispatch	= dispatch
		self.listener		= listener()
		self.listener.setCallBack( dispatch.updateTank )
		win.actionQuitter.triggered.connect(self.listener.stopServer)
		win.actionApropos.triggered.connect( dispatch.doAbout )
		win.actionPr_ferences.triggered.connect( dispatch.doPreferences )
		self.win.tabTank.clear()
		self.listener.startServer()
		
	def	mainLoop(self):
		self.about.close()
#		self.about.info.setText("")
		self.win.show()
		ret = self.app.exec()

		self.listener.stopServer
		exit( ret )
