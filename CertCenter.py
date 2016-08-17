# -*- coding: utf-8 -*-

__version__ = "1.13.5"

import logging
import urllib
import urllib2
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

__all__ = ['CertAPI']

class CertAPI(object):

	__authorization = {'Bearer': None }
	__ob = 'dict'
	API_URL = 'https://api.certcenter.com/rest/v1'

	__MethodInfo = {
		'Limit':				{'http_method': 'GET'},
		'Products':				{'http_method': 'GET'},
		'ProductDetails':		{'http_method': 'GET'},
		'Profile':				{'http_method': 'GET'},
		'Quote':				{'http_method': 'GET'},
		'ValidateCSR':			{'http_method': 'POST'},
		'TestOrder':			{'http_method': 'POST'},
		'Order':				{'http_method': 'POST'},
		'VulnerabiltyAssessment': {'http_method': 'POST'},
		'AddUser':				{'http_method': 'POST'},
		'GetUser':				{'http_method': 'GET', 'path_parameter': 'UserNameOrUserId'},
		'UpdateUser':			{'http_method': 'POST', 'path_parameter': 'UserNameOrUserId'},
		'DeleteUser':			{'http_method': 'DELETE', 'path_parameter': 'UserNameOrUserId'},
		'CancelOrder':			{'http_method': 'DELETE', 'path_parameter': 'CertCenterOrderID'},
		'GetCustomer':			{'http_method': 'GET', 'path_parameter': 'UserNameOrUserId'},
		'GetCustomers':			{'http_method': 'GET'},
		'Revoke':				{'http_method': 'DELETE', 'path_parameter': 'CertCenterOrderID'},
		'UserAgreement':		{'http_method': 'GET'},
		'ApproverList':			{'http_method': 'GET'},
		'Orders':				{'http_method': 'GET'},
		'ModifiedOrders':		{'http_method': 'GET'},
		'GetOrder':				{'http_method': 'GET', 'path_parameter': 'CertCenterOrderID'},
		'Reissue':				{'http_method': 'POST'},
		'UpdateApproverEmail':	{'http_method': 'PUT', 'path_parameter': 'CertCenterOrderID', 'query_parameter': 'ApproverEmail'},
		'ResendApproverEmail':	{'http_method': 'POST', 'path_parameter': 'CertCenterOrderID'},
		'DNSData':				{'http_method': 'POST'},
		'FileData':				{'http_method': 'POST'},
		'ValidateName':			{'http_method': 'POST'}
	}

	def __init__(self,OutputBehavior='dict'):
		self.__ob = OutputBehavior

	def setBearer(self, Bearer):
		self.__authorization = {'Bearer':Bearer}

	def __getattr__(self,name):
		def handlerFunction(*args,**kwargs):
			info = False if not self.__MethodInfo.has_key(name) else self.__MethodInfo[name]
			if not info: return False
			return self.__generic(method=name, kw=kwargs, info=info)
		return handlerFunction

	def __generic(self, method="Limit", kw={}, info={}):
		http_method=info['http_method']
		data = {} if not kw.has_key('req') else kw['req']
		if not isinstance(data,dict): data = {}

		_method = method
		if _method.startswith("Get") or _method.startswith("Add"):
			_method = _method[3:]
		elif _method.startswith("Update") or _method.startswith("Delete") or _method.startswith("Resend") or _method.startswith("Cancel"):
			_method = _method[6:]

		if info.has_key('path_parameter'):
			if data.has_key(info['path_parameter']):
				_method += "/"+str(data[info['path_parameter']])
				del data[info['path_parameter']]

		if http_method=='GET' or info.has_key('query_parameter'):
			if info.has_key('query_parameter'):
				query_parameter = info['query_parameter']
				_data = {}
				if isinstance(query_parameter,str):
					_data = {query_parameter:data[query_parameter]}
				elif isinstance(query_parameter,list):
					for item in query_parameter:
						_data.update( {query_parameter:data[query_parameter]} )
			else:
				_data = data.copy()
			_method = _method+"?"+urllib.urlencode(_data)
			data = {}

		url = "%s/%s" % (self.API_URL, _method)
		#logging.info("Calling CertCenter RESTful API Method '%s' via HTTP '%s' (%s)" % (method, http_method, url))

		handler = urllib2.HTTPHandler()
		opener = urllib2.build_opener(handler)

		request = urllib2.Request(url, data=json.dumps(data))

		if data != {}:
			request.add_header("Content-Type",'application/json')

		request.add_header("Authorization",'Bearer %s' % self.__authorization['Bearer'])
		request.get_method = lambda: http_method

		try:
			connection = opener.open(request)
		except urllib2.HTTPError, e:
			connection = e

		try:
			data = connection.read()
			return json.loads(data) if self.__ob!='json' else data
		except Exception, e:
			return False
