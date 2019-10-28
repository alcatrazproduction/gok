#!/usr/bin/env python3
#######################################################################################################
#	Main class ( gestion) for the app																						#
#	Was the first writing in no class, don the main loop and init all the stuff								#
#	Creator:		Yves Huguenin																									#
#	Date:			28.10.2019																										#
#	Version:		0.1																												#
#																																		#
#######################################################################################################
#from PyQt5 					import	uic
#from PyQt5.QtGui			import	QImage ,  QPixmap
from PyQt5.QtWidgets 	import 	QMessageBox,  QGraphicsScene


#from datetime 				import	date
#from time					import	sleep

#from theApp					import	theApp
#from settings 				import	settings
#from t_cards 				import	t_cards
#from dispatcher 			import dispatcher
#from constant			import const		

class CiterneGfx:
		def __init__(self, theView):
		
			self.view 			= theView
			theScene			= theView.scene
			if theScene == None:
				theScene	= QGraphicsScene()
			self.scene		= theScene
			
		def draw(self,  current,  max):
			if self.scene:
				rect		= self.view.sceneRect()
				self.scene.clear()
				
				None
			None
