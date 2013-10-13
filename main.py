#!/usr/bin/python

import os
import urllib2
from bs4 import BeautifulSoup
import ConfigParser

def cfgini():
	home = os.path.expanduser('~')
	cfgroot = home+'/.souper'
	cfgfile = cfgroot+'/souper.cfg'
	
	if not os.path.exists(home+'/.souper'):
		os.mkdir(home+'/.souper')

	


class Soup:
	def __init_(self,url):
		self.self = self
		self.url = url
	
	

