__author__ = 'wangzi6147'

import urllib2


def get(url):
    urllib2.urlopen(url)
    return urllib2.urlopen(url).read()
