#!/usr/bin/env python3

import	importlib

class db:
	

	

		
	def __init__(self, moteur='mysql'):
		try:
			self.theDb	= importlib.import_module( "modules."+moteur ).link()
		except Exception as e:
			print(e)
			self.theDb	= None
		None
