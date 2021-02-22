# encoding: utf-8
from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
import sys

if sys.version[0] == '2':
	import SimplePreview
else:
	import LoadSP3