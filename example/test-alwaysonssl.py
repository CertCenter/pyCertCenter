#!/usr/bin/env python
# -*- coding: utf-8 -*-
from CertCenter import CertAPI

""" Make sure you already provided proper authentication information
	to CertCenter.py's authorization attribute.
	--
	OutputBehavior can be 'json' or 'dict'. Consider to use 'dict'
	if you want to work with the output.
"""
api = CertAPI(OutputBehavior='dict')

""" First of all, check the common name against the CAs phishing blacklist.
"""
request = { 'CommonName': 'dvtest.alwaysonssl.com' }
ValidateNameResult = api.ValidateName(req=request)
print repr(ValidateNameResult)
#Example Result: {u'IsQualified': True, u'success': True}

if not ValidateNameResult['IsQualified']:
	print "CommonName cannot be used for AlwaysOnSSL because it's blacklisted.\n"
else:
	""" Now let's get the information we need in order to provision
		the DNS zone with the proper CNAME record.
	"""

	CSR = """-----BEGIN CERTIFICATE REQUEST-----
MIIC1zCCAb8CAQAwaTEfMB0GA1UEAwwWZHZ0ZXN0LmFsd2F5c29uc3NsLmNvbTEL
MAkGA1UEBhMCREUxDzANBgNVBAgMBkhlc3NlbjEQMA4GA1UEBwwHR2llc3NlbjEW
MBQGA1UECgwNTm90IEF2YWlsYWJsZTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC
AQoCggEBALcmAP8FpqcJp2OXrDUp4AEY1VHQu9UtFOu2tPKZ6VvkTfRe2Jbk011V
aqn5ioDPhFcGB1ZfzEo8Umbn/F9Da6XoRdJv/gAr+0EWGkCRkLdtn8mr1DMZaBnF
b2YUxGIjj4BfBPMada9Wt8VuIjpSgafYHhLJohC7c2icuyf/bqfxtLJslpepu5iZ
QSdc5TqCsAWhjoXEcLoa/07v/VbLLpjmViOkrAd8h2nuRg2AoKydU+SYC2+EDImz
kxTcGIjb6GVl6QL/XVwdz602bjzyzFyZdexPKDfw8PaYuJkifxjbfzAKSxhAgd4k
PgJbY0fq0OV6LU1yAGkromTBu202eysCAwEAAaApMCcGCSqGSIb3DQEJDjEaMBgw
CwYDVR0PBAQDAgXgMAkGA1UdEwQCMAAwDQYJKoZIhvcNAQELBQADggEBAJO3dM4y
ngKsjylNJjCFopntboXZH/Jwu5Tjm6icwc4ULhd2F5Yzrq2RvZ9TAUCmp+WHQwwr
vETPgZB8/SXtQYn2DBY8DUETW7jF/AghkPcyNuOzbpmxI0uf6Bp6uju4hzovcbOq
m4rD+jl0JGfQCbnQyJ0oH1KxNhMYRzush72129hNshl1Z1KVV2nu/pQxULg9N5k6
GVCfacmDgOOCMpCI5nsif/wGR5NjTlEqQ4/MKkBzgNxpNACl09g8U9BEkcBFokk0
7XDEKxP9TmH2TkWYmZ8RWRBihijQmSvA7RoJbGdqryRXg9msV1AUTxHrTyxneV9/
Qfhjn38lALqDF60=
-----END CERTIFICATE REQUEST-----"""

	request = {
		"ProductCode": "AlwaysOnSSL.AlwaysOnSSL",
		"CSR": CSR,
	}
	DNSDataResult = api.DNSData(req=request)
	print repr(DNSDataResult)
	# Example Result: {u'DNSAuthDetails': {u'PointerType': u'CNAME', u'DNSEntry': u'sadxoi5spfy8axlgu9lpcga55wncn6bo.dvtest.alwaysonssl.com.', u'DNSValue': u's20160322210004.dvtest.alwaysonssl.com.'}, u'success': True}
	# Create a CNAME entry like this:
	#	sadxoi5spfy8axlgu9lpcga55wncn6bo.dvtest.alwaysonssl.com. IN CNAME s20160322210004.dvtest.alwaysonssl.com.

	""" The name is qualified, the dns zone has been updated with the
		proper DNS records. Now we can request the AlwaysOnSSL Certificate.
	"""
	request = {
		'OrderParameters': {
			"ProductCode": "AlwaysOnSSL.AlwaysOnSSL",
			"CSR": CSR,
			"ValidityPeriod": 180,
		}
	}
	OrderResult = api.Order(req=request)
	print repr(OrderResult)
	# Example Result: {u'Timestamp': u'2016-03-22T14:03:33Z', u'OrderParameters': {u'ProductCode': u'AlwaysOnSSL.AlwaysOnSSL', u'DVAuthMethod': u'DNS', u'PartnerOrderID': u'APIR-3F3PWARU2KCNEQ4OWXEO2Y3H', u'ValidityPeriod': 180, u'CSR': u'YourCSR', u'SignatureHashAlgorithm': u'SHA256-FULL-CHAIN'}, u'CertCenterOrderID': 6260500, u'success': True, u'Fulfillment': {u'Certificate_PKCS7': u'-----BEGIN PKCS #7 SIGNED DATA-----{...}-----END PKCS #7 SIGNED DATA-----', u'Intermediate': u'-----BEGIN CERTIFICATE-----{...}-----END CERTIFICATE-----', u'Certificate': u'-----BEGIN CERTIFICATE-----{...}-----END CERTIFICATE-----\n'}}




