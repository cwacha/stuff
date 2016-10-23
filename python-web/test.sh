#!/bin/sh

echo "Content-type: text/html"
echo
echo "<title>Test.sh</title>"
echo "<pre>"

echo "vars: $*"
echo "____"
set
echo "</pre>"
