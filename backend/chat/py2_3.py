import sys


try:  # py2
	from urllib import urlopen
except ImportError:  # py3
	from urllib.request import urlopen


try:  # py2
	from urlparse import urlparse
except ImportError:  # py3
	from urllib.parse import urlparse


try:
	from urllib import quote
except ImportError:  # py3
	from urllib.parse import quote


def get_unicode(ch):
	if sys.version > '3':
		return chr(ch)
	else:
		return unichr(ch)


str_type = str if sys.version > '3' else basestring


def dict_values_to_list(dict):
	if sys.version > '3':
		return list(dict.values())
	else:
		return dict.values()
