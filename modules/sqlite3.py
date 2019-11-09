#!/usr/bin/env python3

import sqlite3

class link:
	def __init__(self, theHost=None, theDb=None,  theUser=None,  thePw=None):
		self.con	= sqlite3.connect('db/gok.db')
		self.con.row_factory = sqlite3.Row
			
