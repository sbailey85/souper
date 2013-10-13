#!/usr/bin/python

import os
import urllib2
from bs4 import BeautifulSoup
import ConfigParser

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
		

		


	


class Soup:
	def __init__(self,url):
		self.self = self
		self.url = url
	def getpage(url):
		urllib2.urlopen(url).read()
	def getsoup():
		soup = BeautifulSoup(getpage(url))
		return soup



a = Soup(url='http://google.com')
