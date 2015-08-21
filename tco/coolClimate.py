#!/usr/bin/env python
# -*- coding: utf-8 -*-
#learning hp on demand api

import requests
# from xml.etree import ElementTree
# from xml.dom import minidom
import xmltodict
import math

url = 'https://apis.berkeley.edu:443/coolclimate/footprint-defaults?'

app_key = '955f4c4788a6d28d89a8d6a39a81d93b'
app_id = 'd60c720f'

def postrequests(data ={}):
	data["app_id"] = app_id
	data["app_key"] = app_key
	response = requests.get(url, params = data)

	# print response.content
	# return response.content

	obj = xmltodict.parse(response.content)
	print obj['response']['result_grand_total']
	print type(float(unicode(obj["response"]["result_grand_total"])))
	print float(unicode(obj["response"]["result_grand_total"]))
	val = float(unicode(obj["response"]["result_grand_total"]))
	val = int(val)
	print val
	return val
	# return float(unicode(obj["response"]["result_grand_total"]))

def coolclimate(data):
	return postrequests(data)

