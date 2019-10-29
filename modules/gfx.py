#!/usr/bin/env python3
#######################################################################################################
#	Main class ( gestion) for the app																						#
#	Was the first writing in no class, don the main loop and init all the stuff								#
#	Creator:		Yves Huguenin																									#
#	Date:			28.10.2019																										#
#	Version:		0.1																												#
#																																		#
#######################################################################################################
from PyQt5.QtCore	import	Qt
from PyQt5.QtGui			import		 QPen, QBrush
from PyQt5.QtWidgets 	import 	  	QGraphicsScene


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
			theScene			= theView.scene()
			if theScene == None:
				theScene	= QGraphicsScene()
				theView.setScene( theScene )
			self.scene		= theScene
			
		def draw(self,  current,  max):
			if self.scene:
				bGreen	= QBrush( Qt.green )
				bRed		= QBrush( Qt.red )
				bBlack	= QBrush( Qt.black )
				bBlue		= QBrush( Qt.blue )
				pGreen	= QPen( Qt.green )
				pRed		= QPen( Qt.red )
				pBlack	= QPen( Qt.black )
				pBlue		= QPen( Qt.blue )
				rect		= self.view.sceneRect()
				self.scene.clear()
				self.scene.addText("                                                                                          ")
				self.scene.addRect(20, 50, 150, 350, pBlack, bGreen)
				
				None
			None
