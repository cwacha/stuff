#!/usr/bin/env python

import os
import cgi
import json

import cgitb
cgitb.enable(1,None,5,"text")

import pprint
pp = pprint.PrettyPrinter(indent=4)

fields = cgi.FieldStorage()


print "Content-type: text/html"
print
print "<title>Test CGI</title>"
print "<p>Hello World!</p>"
print "<pre>"

#pp.pprint(fields.value)
#pp.pprint(os.environ)
try:
	data = json.loads(fields.value)

	#print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
	pp.pprint(data)
	pp.pprint(data['release']['draft'])
	pp.pprint(data['release']['prerelease'])
	pp.pprint(data['release']['tag_name'])
	pp.pprint(data['release']['url'])

except ValueError:
	print "malformed JSON"

print "</pre>"