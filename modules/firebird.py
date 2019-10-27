#!/usr/bin/env python3

import 	fdb

class link:
	def __init__(self, theHost, theDb,  theUser,  thePw):
		self.con = fdb.connect(
						host			= theHost, 
						database	= theDb,
						user			= theUser, 
						password	= thePw
					)
