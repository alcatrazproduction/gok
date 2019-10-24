import socket
import socketserver

from threading import Thread


class listener:
# ##########################################################################################################
#	Protocol:                                                                                                                                                                                                                                                        #
#	on Connect, must send "PC-LINK\0x0a"                                                                                                                                                                                                              #
#	Gok send 20 bytes	: nnnnnnnnnnQQQQQQQQQQ	( n ???; Q is value of quanty                                                                                                                                             #
#	Gok send 19 bytes unknow, may be a coded form of the packed value, ended by 0x0a                                                                                                                                                    #
# ##########################################################################################################
	class GokHandler(socketserver.StreamRequestHandler):

		def handle(self):
			# self.rfile is a file-like object created by the handler;
			# we can now use e.g. readline() instead of raw recv() calls
			self.wfile.write(b"PC-LINK\n")
			self.data = self.rfile.read(20).strip()
			print("{} wrote:".format(self.client_address[0]))
			print("ID: {}".format( self.data[0:9]))
			print("Level: {}".format( self.data[10:19]))
			self.data = self.rfile.read(19).strip()
			print(self.data)
			# Likewise, self.wfile is a file-like object used to write back
			# to the client
			


	def __init__(self, port=8000, ip='0.0.0.0'):
		self.port		= port
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
