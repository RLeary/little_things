# Test if internet connections is running

from urllib2 import urlopen, URLError

try:
	urllib2.urlopen('https://www.google.com', timeout=2)
	print('Internet connection is working\n')
except urllib2.URLError:
	print('No internet connection\n')