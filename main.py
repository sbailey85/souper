#!/usr/bin/python
import re
import os
import urllib2
from bs4 import BeautifulSoup
import ConfigParser


cachedir = os.path.expanduser('~')+'/.souper/cache/'
if not os.path.exists(cachedir):
	os.mkdir(cachedir)
else:
	print('exits')
def cfgini():
	home = os.path.expanduser('~')
	cfgroot = home+'/.souper'
	cfgfile = cfgroot+'/souper.cfg'
	if not os.path.exists(cfgroot):
		os.mkdir(cfgroot)

		
	try:
		
		open(cfgfile)
	except IOError:
		print('does not exist')
		cfg = open(cfgfile, 'w')	
		

		


	


class Souper():
	def __init__(self,url):
		self.self = self
		self.url = url
		fname = self.url.split('/')[2]
		self.name = fname
		if os.path.exists(cachedir+fname):
			self.soup = BeautifulSoup(open(cachedir+fname).read())
		else:
			os.mkdir(cachedir+fname)
			f = open(cachedir+fname+fname, 'w')
			f.write(urllib2.urlopen(self.url).read())
			f.close()		
			
		
	def getlinks(self):
		 print(self.soup.find_all('a'))
	def getstatic(self):
		print(self.soup.find_all(href=re.compile('.jpg$'))['href'])	



