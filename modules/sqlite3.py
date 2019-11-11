#!/usr/bin/env python3

import sqlite3

class link:
	def __init__(self, theHost=None, theDb='db/gok.db', thePort = None,  theUser=None,  thePw=None):
		self.con	= sqlite3.connect( theDb )
		self.con.row_factory = sqlite3.Row
	
	def doInsert(self):
		None
		
	def doSelect(self):
		None
