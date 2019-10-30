#!/usr/bin/env python3
#######################################################################################################
#	Main class ( gestion) for the app																						#
#	Was the first writing in no class, don the main loop and init all the stuff								#
#	Creator:		Yves Huguenin																									#
#	Date:			28.10.2019																										#
#	Version:		0.1																												#
#																																		#
#######################################################################################################
from PyQt5 					import	uic
from PyQt5.QtGui			import	QImage ,  QPixmap
from PyQt5.QtWidgets 	import 	QMessageBox


from datetime 				import	date
from time					import	sleep

from theApp					import	theApp
from settings 				import	settings
#from t_cards 				import	t_cards
from dispatcher 			import dispatcher
from constant				import const

from modules.tcpip	import listener
class gestion:
	def __init__(self):
		
		self.app 			= theApp([])
#		self.thePref 		= settings( self.app )
#		self.about		= uic.loadUi( const.aboutWindow)
#		logo 				= QImage( const.logoFile )
#		self.about.logo.setPixmap(QPixmap.fromImage(logo))
#		self.about.info.setText("Initialising Application")
#		self.about.show()
#		sleep(2)
		
	def initDatabase(self):
		
#		self.about.info.close()
#		self.about.info.setText("Trying to connect to database")
#		self.about.show()
#		thePref			= self.thePref
		
#		while 1:
#			try:
#				conn = pymysql.connect(	host		= thePref.elems[0]['DBHost'], 
#													port		= int( thePref.elems[0]['DBPort'] ), 
#													user		= thePref.elems[0]['DBUser'], 
#													passwd	= thePref.elems[0]['DBPass'], 
#													db			= thePref.elems[0]['DBdb'])

#				cur = conn.cursor()
#				break
		None
		
	def initApplication(self):
		
		global primaryScreen
		
		win 					= uic.loadUi( const.mainWindow )
		dispatch			= dispatcher( win, self )
		primaryScreen	= self.app.primaryScreen()
		scrSize			= primaryScreen.size()
		win.move( scrSize.width()/2 - win.width()/2, scrSize.height()/2 - win.width()/2 )
		

		now 	= (date. today()).replace(day=1)
		mn 	= now.month+1
		if mn > 12:
			fin=now.replace(year=now.year+1, month=1)
		else:
			fin=now.replace( month=mn)
			
		mn 	= now.month-1
		if mn < 0:
			fin=now.replace(year=now.year-1, month=12)
		else:
			fin=now.replace( month=mn)
			

		self.win			= win
		self.dispatch	= dispatch
		self.listener		= listener()
		self.listener.setCallBack( dispatch.updateTank )
		win.actionQuitter.triggered.connect(self.listener.stopServer)
		self.win.tabTank.clear()
		listener.test()
		self.listener.startServer()
		
	def	mainLoop(self):
#		self.about.close()
#		self.about.info.setText("")
		self.win.show()
		ret = self.app.exec()

#		self.app.conn.close()
		exit( ret )
