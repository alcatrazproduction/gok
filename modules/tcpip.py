#!/usr/bin/env python3
import	socket
import	socketserver
from		http.server 		import BaseHTTPRequestHandler, HTTPServer

from threading import Thread

class listener:
# ##########################################################################################################
#	Protocol:                                                                                                                                                                                                                                                        #
#	on Connect, must send "PC-LINK\0x0a"                                                                                                                                                                                                              #
#	Gok send 20 bytes	: nn nn nn ii ii QQ QQ QQ QQ QQ	( n ???; iiii id in hex; Q is value of quanty )                                                                                                                   #
#							  02 11 08 04CF 0000322000
#	Gok send 19 bytes	: nn cc cc hh hh nn nn nn nn \0x0a		( n ???; cccc capacity in Hex; hhhh high in Hex )   																						#
#							  21 2134 05DD 0A 0A AA 03
# test: 02110804CF000032200021213405DD0A0AAA03
# ##########################################################################################################

	class GokHandler(socketserver.StreamRequestHandler):
		
		
		
		def setCallBack(self,  theEntry	= None):
			global callBack
			callBack	= theEntry

		def handle(self):
			# self.rfile is a file-like object created by the handler;
			# we can now use e.g. readline() instead of raw recv() calls
			
			global callBack
			
			self.wfile.write(b"PC-LINK\n")
			self.data = self.rfile.read(20).strip()
			print("{} wrote:".format(self.client_address[0]))
			ip				= self.client_address[0]
			print("ID: {}".format( self.data[6:9]))
			id				= self.data[6:9]
			level		= self.data[10:19]
			print("Level: {}".format( self.data[10:19]))
			self.data = self.rfile.read(19).strip()
			capacity	= self.data[2:5]
			print("Capacity: {}".format( self.data[2:5]))
			high			= self.data[6:9]
			print("High: {}".format( self.data[6:9]))
			
			print( callBack )
			if callBack:
				callBack( ip, id, level, capacity, high )
			# Likewise, self.wfile is a file-like object used to write back
			# to the client
			


	def __init__(self, port=8000, ip='0.0.0.0'):
		global callBack
		self.port	= port
		self.ip		= ip
		
												
	def startServer(self ):
		global callBack
		self.server = socketserver.TCPServer((self.ip, self.port), listener.GokHandler)
		self.thread					= Thread(
												target 	= self._startServer, 
												args		= (  ))
		self.thread.start()
		
	def setCallBack(self,  theEntry	= None):
		global callBack
		
		callBack	= theEntry
		listener.GokHandler.setCallBack( theEntry )
		
	def handle(self,  client):
		request		= client.recv(1024)
		print( 'Received {}'.format( request ) )
		client.send('PC-LINK')
	
	def _startServer(self ):
		self.server.serve_forever()
		
	def stopServer(self ):
		self.server.shutdown()
		self.server.server_close()

# *******************************************************************************************

class	webinterface:
	
	class httpHandler(BaseHTTPRequestHandler):
		def do_HEAD(self):
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

		def do_GET(self):
			paths = {
				'/foo': {'status': 200},
				'/bar': {'status': 302},
				'/baz': {'status': 404},
				'/qux': {'status': 500}
			  }

			if self.path in paths:
				self.respond(paths[self.path])
			else:
				self.respond({'status': 500})

		def handle_http(self, status_code, path):
			self.send_response(status_code)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			content = '''
			<html><head><title>Title goes here.</title></head>
			<body><p>This is a test.</p>
			<p>You accessed path: {}</p>
			</body></html>
			'''.format(path)
			return bytes(content, 'UTF-8')

		def respond(self, opts):
			response = self.handle_http(opts['status'], self.path)
			self.wfile.write(response)
		  
	def __init__(self, port=8001, ip='0.0.0.0'):
		self.port	= port
		self.ip		= ip
		
		if 1:
			server_class = HTTPServer
			self.httpd = server_class((self.ip, self.port), self.httpHandler)
			
			self.thread					= Thread(
													target 	= self.startServer, 
													args		= (  ))
			self.thread.start()
	def startServer(self ):
			try:
				self.httpd.serve_forever()
			except KeyboardInterrupt:
				pass
		
	def stopServer(self ):
			self.httpd.server_close()
