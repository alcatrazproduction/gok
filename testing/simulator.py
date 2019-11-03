#!/usr/bin/env python3

#####################################################################################################
#	Simulator for Gok																				
#	
#	Creator:		Yves Huguenin							
#	Date:			03.11.2019													
#	Version:		0.1																
#																												
#####################################################################################################
import 	socket
from 		random		import	randrange
from		time			import sleep

ip			= 'localhost'
port		= 8000
wait		= 15
gok		= {}	

def	send( HOST, PORT, data):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		response	= s.recv(1024)
		print( response )
		s.sendall( data)
		s.close()

def	generate(serial, capacity, height, value):
#	Gok send 20 bytes	: nn nn nn ii ii QQ QQ QQ QQ QQ	( n ???; iiii id in hex; Q is value of quanty )                                                                                                                   #
#							  02 11 08 04CF 0000322000
#	Gok send 19 bytes	: nn cc cc hh hh nn nn nn nn \0x0a		( n ???; cccc capacity in Hex; hhhh high in Hex )   																						#
#							  21 2134 05DD 0A 0A AA 03
	return b'000000%04x%010d00%04x%04x00000000\n'%(serial, value*100, capacity, height)
	
def	doSimul():
	while True:
		for s in gok:
			d = gok[s]
			nibble = generate( s, d[0], d[1], randrange(0, d[0]))
			print ( nibble )
			send( ip,  port,  nibble )
			None
		sleep( wait )
		

if __name__ == "__main__":
	import sys
	print( sys.argv )

	ign		= False
	for opt in sys.argv[1:]:
		if ign:
			ign=False
			continue
			
		if opt in  ("-h", "--help"):
			print ('{} --ip <ip of server> -p <port of server> -w <delay> [-serialnumber capacity.height]'.format(sys.argv[0]))
			sys.exit()
		elif opt in ("-i", "--ip"):
			ip 	= sys.argv.pop( sys.argv.index(opt)+1)
			ign	= True
		elif opt in ("-p", "--port"):
			port	= int( sys.argv.pop( sys.argv.index(opt)+1) )
			ign	= True
		elif opt in ("-w", "--wait"):
			wait	= int( sys.argv.pop( sys.argv.index(opt)+1) )
			ign	= True
		else:
			if opt[0]=='-':
				try:
					ser	= int( opt[1:])
					v		= sys.argv.pop( sys.argv.index(opt)+1)
					cp	= int( v[:v.index('.')])
					he	= int( v[v.index( '.')+1: ])
					gok[ser] = [cp, he]
				except:
					None
				
			
	print( ip )
	print( port )
	print(gok)
	doSimul()
