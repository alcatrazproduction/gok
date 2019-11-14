#!/usr/bin/env python3
#######################################################################################################
#	Main class ( gestion) for the app
#	Was the first writing in no class, don the main loop and init all the stuff
#	Creator:		Yves Huguenin
#	Date:			28.10.2019
#	Version:		0.1
#								
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
		bRed				= QBrush( Qt.red )
		bBlack				= QBrush( Qt.black )
		bBlue				= QBrush( Qt.blue )
		bWhite				= QBrush( Qt.white )
		pGreen			= QPen( Qt.green )
		pRed				= QPen( Qt.red )
		pBlack				= QPen( Qt.black )
		pBlue				= QPen( Qt.blue )
		pWhite				= QPen( Qt.white )

		def __init__(self, theView):
		
			try:
				print("Init CiternGfx")
				self.view 			= theView
				theScene			= theView.scene()
				if theScene == None:
					theScene	= QGraphicsScene()
					theView.setScene( theScene )
				self.scene		= theScene
				self.bGreen		= QBrush( Qt.green )
				self.bRed			= QBrush( Qt.red )
				self.bBlack		= QBrush( Qt.black )
				self.bBlue		= QBrush( Qt.blue )
				self.pGreen		= QPen( Qt.green )
				self.pRed			= QPen( Qt.red )
				self.pBlack		= QPen( Qt.black )
				self.pBlue		= QPen( Qt.blue )
				self.tank			= QPixmap.fromImage( QImage( const.tankFile ) )
				
			except Exception as inst:
				print(inst) 	
			
		def draw(self,  current,  max):
			if self.scene:
				self.scene.clear()
				self.scene.addPixmap(  self.tank )
				y0	= 35.0
				y1	= 372.0
				x0	= 1.0
				x1	= 103.0
				x2	= 108.0
				x3	= 114.0
				x4	= 119.0
				x5	= 210.0
				r		= 18.0
				rx		= [ 	17.97,  17.89,  17.75, 17.55, 17.29, 16.97, 16.58, 16.12, 15.59, 14.97,
								14.25, 13.42, 12.45, 11.31, 9.95, 8.25, 5.92, 0.00]
				rx1		= [ 	18.00, 17.93, 17.73, 17.39, 16.91, 16.31, 15.59, 14.74, 13.79, 12.73,
								11.57, 10.32, 9.00, 7.61, 6.16, 4.66, 3.13, 1.57,0.00]

				h		= r + y1 - y0
				p		= (current * 1.0) / max
				y		= h - ( h * p )
				if y > y1-y0 :
					self.scene.addRect(x2		, y+ y0	, x3-x2-2.5		, y1-y0-y		,  self.pRed	,  self.bWhite  )
					for z in range(   int( y -.5 )-int(y1-y0) ,-1,  -1	 ):
						try:
							self.scene.addRect(x0+r-(rx1[z])+1 	, ( y1)+z		, x2-x0-(r-rx1[z])	, 1		,  self.pWhite	,  self.bWhite  )
							self.scene.addRect(x4							, y1+z		, x5-(x4-rx[z] ) -r		,  1		,  self.pWhite	,  self.bWhite  )
						except Exception as inst:
							print("{}: -> {};{} ".format(inst,  y, z) )
				elif y < r:
					self.scene.addRect(x0		,r+ y0		, x1-x0		, y1-y0-r			,  self.pRed	,  self.bRed  )
					self.scene.addRect(x2		, y+y0		, x3-x2		, y1-y0-y			,  self.pRed	,  self.bRed  )
					self.scene.addRect(x4		,r+ y0		, x5-x4		, y1-y0-r			,  self.pRed	,  self.bRed  )
					for z in range(  18,  int( y ), -1	 ):
						try:
							self.scene.addRect(x0+(18-rx[ 18-z ]) 	, z-1+y0		, x1-x0-(18-rx[ 18-z ])	, 1		,  self.pBlue	,  self.bBlue  )
							self.scene.addRect(x4								,z-1+y0		, x5-( x4-rx[18- z ] )-r		,  1		,  self.pBlue	,  self.bBlue  )
						except Exception as inst:
							print("{}: -> {};{} ".format(inst,  y, z) ) 
				else:
					try:
						self.scene.addRect(x0		, y+y0		, x1-x0		, y1-y0-y		,  self.pRed	,  self.bGreen  )
						self.scene.addRect(x2		, y+y0		, x3-x2		, y1-y0-y		,  self.pRed	,  self.bGreen  )
						self.scene.addRect(x4		, y+y0		, x5-x4		, y1-y0-y		,  self.pRed	,  self.bGreen  )
					except Exception as inst:
						print(inst) 
