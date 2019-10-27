#!/usr/bin/env python3

import 	fdb
import	pymysql

class db:
	
	class mysql:
		def __init__(self):
			None
	
	class firebird:
		def __init__(self, theHost, theDb,  theUser,  thePw):
			self.con = fdb.connect(
							host		= theHost, 
							database	= theDb,
							user		= theUser, 
							password	= thePw
						)
		
	def __init__(self, moteur='mysql'):
		None
