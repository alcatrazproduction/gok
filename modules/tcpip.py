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
# ##########################################################################################################
	class GokHandler(socketserver.StreamRequestHandler):

		def handle(self):
			# self.rfile is a file-like object created by the handler;
			# we can now use e.g. readline() instead of raw recv() calls
			self.wfile.write(b"PC-LINK\n")
			self.data = self.rfile.read(20).strip()
			print("{} wrote:".format(self.client_address[0]))
			print("ID: {}".format( self.data[6:9]))
			print("Level: {}".format( self.data[10:19]))
			self.data = self.rfile.read(19).strip()
			print("Capacity: {}".format( self.data[2:5]))
			print("High: {}".format( self.data[6:9]))
			# Likewise, self.wfile is a file-like object used to write back
			# to the client
			


	def __init__(self, port=8000, ip='0.0.0.0'):
		self.port	= port
		self.ip		= ip
		
		if 1:
			self.server = socketserver.TCPServer((ip, port), listener.GokHandler)
			self.thread					= Thread(
													target 	= self.startServer, 
													args		= (  ))
			self.thread.start()
			
		else:
			if socket.has_dualstack_ipv6():
				self.server = socket.create_server( ( self.ip,  self.port ), family=socket.AF_INET6, dualstack_ipv6=True)
			else:
				self.server = socket.create_server( ( self.ip,  self.port ))
	#		self.server	= socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
	#		self.server.bind( ( self.ip,  self.port ) )
	#		self.server.listen(10)
			
			self.sock, self.address 	= self.server.accept()
			self.thread					= Thread(
													target 	= self.handle, 
													args		= ( ))
			self.thread.start()
		
	def handle(self,  client):
		request		= client.recv(1024)
		print( 'Received {}'.format( request ) )
		client.send('PC-LINK')
	
	def startServer(self ):
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
