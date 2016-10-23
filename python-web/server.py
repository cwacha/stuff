#!/usr/bin/env python
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
import sys
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/"]
 
try:
	httpd = server(server_address, handler)
	httpd.serve_forever()
except KeyboardInterrupt:
	pass
except:
	print "Caught %s exception: %s" % (sys.exc_info()[0].__name__, sys.exc_info()[1])
