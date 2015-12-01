#!/usr/bin/env python
#coding:utf-8

import SocketServer


class mySocketHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		recv_data=self.request.recv(1024)
		print "From %s: %s" %(self.client_address,recv_data)
if __name__ == "__main__":
	host,port="",18000
	server=SocketServer.ThreadingTCPServer((host,port),mySocketHandler)
	server.serve_forever()
