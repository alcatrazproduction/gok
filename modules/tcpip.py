import socket
from threading import Thread

class listener:
	def __init__(self, port=8000, ip=''):
		self.port		= port
		self.ip		= ip
		
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
												args		= (self.sock, ))
		self.thread.start()
		
	def handle(self,  client):
		request		= client.recv(1024)
		print( 'Received {}'.format( request ) )
		client.send('PC-LINK')
	
	
