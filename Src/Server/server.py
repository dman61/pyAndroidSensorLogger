import SocketServer
import json

bOutputToFile=False

class MyTCPServer(SocketServer.ThreadingTCPServer):
	allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		try:
			global bOutputToFile, outfile
			data=json.loads(self.request.recv(1024).strip())
			print data
			if bOutputToFile: outfile.write(data)
			#self.request.sendall(json.dumps({'return':'ok"}))
		except Exception, e:
			print "Exception wihle receiving message: ", e

if bOutputToFile: outfile=open("sensors.log","wb")
server = MyTCPServer(('10.101.1.246', 13373), MyTCPServerHandler)
server.serve_forever()
