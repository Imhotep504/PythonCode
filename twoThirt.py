#!/usr/bin/python 

import shutil

#copy file from shutil module w/ src + dst ;) 
shutil.copyfile('hellos','goodbyes') 


#now for simple HTTP server ;) 
import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler) 

print "serving at port", PORT
httpd.serve_forever() 
