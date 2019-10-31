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
		bGreen			= QBrush( Qt.green )
		bRed			= QBrush( Qt.red )
		bBlack			= QBrush( Qt.black )
		bBlue			= QBrush( Qt.blue )
		pGreen			= QPen( Qt.green )
		pRed			= QPen( Qt.red )
		pBlack			= QPen( Qt.black )
		pBlue			= QPen( Qt.blue )

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
				self.scene.clear()
				self.scene.addPixmap(  self.tank )
				y0	= 40.0
				y1	= 372.0
				x0	= 1.0
				x1	= 103.0
				x2	= 108.0
				x3	= 114.0
				x4	= 119.0
				x5	= 210.0
				r		= 18.0
				
				h		= y1 - y0 + r
				p		= (current * 1.0) / max
				y		= h - ( h * p )
				print(current)
				print(max)
				print(h)
				print(p)
				print(y)
				if y > y1-y0 :
					self.scene.addRect(x0, y0, x1-x0, y1,  self.pRed,  self.bRed  )
					self.scene.addRect(x2, y0, x3-x2, y1,  self.pRed,  self.bRed  )
					self.scene.addRect(x4, y0, x5-x4, y1,  self.pRed,  self.bRed  )
				else:
					self.scene.addRect(x0, y+y0, x1-x0, y1-y0-y, self.pRed,  self.bRed  )
					self.scene.addRect(x2, y+y0, x3-x2, y1-y0-y,  self.pRed,  self.bRed  )
					self.scene.addRect(x4, y+y0, x5-x4, y1-y0-y,  self.pRed,  self.bRed  )
