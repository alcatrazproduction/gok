#!/usr/bin/env python3
#####################################################################################################
#	Main application entry point																																										#
#	Only import the main loop class and call all the init stuff, the run the application																											#
#	Creator:		Yves Huguenin																																									#
#	Date:			28.10.2019																																										#
#	Version:		0.1																																													#
#																																																		#
#####################################################################################################
name = "KSWGok"

from main		import gestion

try:
	main 	= gestion()
	main.initDatabase()
	main.initApplication()
	main.mainLoop()
except Exception as inst:
	print(inst)         
	exit( -10000 )
