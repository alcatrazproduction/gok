#!/usr/bin/env python3

import	pymysql

class link:
	def __init__(self, theHost, theDb, thePort,   theUser,  thePw):
		self.con	= pymysql.connect(
								host				= theHost,
								 user			= theUser,
								 password	= thePw,
								 db				= theDb )
			
