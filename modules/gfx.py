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
from PyQt5.QtGui			import		QPen, QBrush,  QImage,  QPixmap
from PyQt5.QtWidgets 	import 	  	QGraphicsScene


#from datetime 				import	date
#from time					import	sleep

#from theApp					import	theApp
#from settings 				import	settings
#from t_cards 				import	t_cards
#from dispatcher 			import dispatcher
from constant			import const		

class CiterneGfx:
		def __init__(self, theView):
		
			print("Init CiternGfx")
			print( theView )
			self.view 			= theView
			theScene			= theView.scene()
			if theScene == None:
				theScene	= QGraphicsScene()
				theView.setScene( theScene )
			self.scene		= theScene
			self.bGreen			= QBrush( Qt.green )
			self.bRed			= QBrush( Qt.red )
			self.bBlack			= QBrush( Qt.black )
			self.bBlue			= QBrush( Qt.blue )
			self.pGreen			= QPen( Qt.green )
			self.pRed			= QPen( Qt.red )
			self.pBlack			= QPen( Qt.black )
			self.pBlue			= QPen( Qt.blue )
			self.tank				= QPixmap.fromImage( QImage( const.tankFile ) )
			
		def draw(self,  current,  max):
			if self.scene:

				rect		= self.view.sceneRect()
				self.scene.clear()
				self.scene.addPixmap(  self.tank )
				self.scene.addText("     HelloWorld                                                                                     ")

				
				None
			None
