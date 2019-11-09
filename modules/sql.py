#!/usr/bin/env python3

import	importlib

class db:
	
	def __init__(self, theHost, theDb,  theUser,  thePw,  moteur='mysql'):
		try:
			self.theDb	= importlib.import_module( "modules."+moteur ).link( theHost, theDb,  theUser,  thePw )
			self.base		= moteur
		except Exception as e:
			print(e)
			self.theDb	= None
			self.base		= None
			
	def	isOpen( self ):
		if self.theDb == None:
			return False
		return True
