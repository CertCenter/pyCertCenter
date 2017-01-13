#!/usr/bin/env python
# -*- coding: utf-8 -*-

import CertCenter

api = CertCenter.CertAPI(OutputBehavior='dict')
api.setBearer('XYZXYZXYZ.oauth2.certcenter.com')

""" First of all, check the common name against the CAs phishing blacklist.
"""
request = { 'CommonName': 'testdv.alwaysonssl.com' }
DVAuthMethod = 'FILE' # Possible values: DNS, FILE
ValidateNameResult = api.ValidateName(req=request)
print repr(ValidateNameResult)
#Example Result: {u'IsQualified': True, u'success': True}

if not ValidateNameResult['IsQualified']:
	print "CommonName cannot be used for AlwaysOnSSL because it's blacklisted.\n"
else:
	""" Now let's get the information we need in order to provision
		the authorization data (DNS CNAME record or File).
	"""

	CSR = """-----BEGIN CERTIFICATE REQUEST-----
MIICsTCCAZkCAQAwbDELMAkGA1UEBhMCREUxDzANBgNVBAgTBkhlc3NlbjEQMA4G
A1UEBxMHR2llc3NlbjEWMBQGA1UEChMNQ2VyEEnlbnRlciBBRzEiMCAGA1UEAxMZ
ZGV2ZWxvcGVycy5jZXJ0Y2VudGVyLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBAKt64cS+fjdKFEz5dWLKZAYaWM3HQJ4ewNSaM3U00gUYOJbxOnKp
uzjrR8PHAVssFtgjCMqfv7UeAASMwP7o5KdRctxsJQuxQqtRXimclZ3zUWUsDyN8
vX1q+QmC3zxuFnlrfFQrLMAIvwHnJHmzChQQRCQ+niFr3kTlKPuCKaUVZ4/V7Cfk
gZebooBhBGJ3C4ZRNKIkvDaXEdup6MbJ1Zb63dsFfP3hiFXagcmlmTVigc5nSB2k
OC5QHXEmAW64gaiATtfmgY85QU6XlFSevHk5lvqcbXKfHbhzahZj0q4L2GosVV1Q
goBm8Yvn+EKqZ6jD2DzSEQQt4VaBoqo7NuMCAwEAAaAAMA0GCSqGSIb3DQEBCwUA
A4IBAQB0VQCln+/5XywLYsASs+CQa7oYQxAoJbiXQZ8s0zrKGMQhfgtX4Px+odjs
4PlKcQ5VVsVeyLiHDrusntpCd09D7vcIwGHkrze7tANFFJkWAsd47V17fu4GrZ6X
weyyiXVypYRIBtk9hjkZopr9t3YEDxeoAx/U0uNl9hl7+dFCnmBlxMPhvqEn1uzu
omDrNuiOWGULy5Udb2iqOL2U2ILxPFlBBRF2SeBj/F7qf7dHSN+fAazvckTntxSO
dys7+l3rOykKgT1L22nx3yVFpKROCQs/hKQH18tPfrEoUOQerjTgSczbibw+wnJj
Tx4K5s4Ks+9vv4wS7zWLdU83BDMD
-----END CERTIFICATE REQUEST-----"""

	request = {
		"ProductCode": "AlwaysOnSSL.AlwaysOnSSL",
		"CSR": CSR
	}

	if DVAuthMethod == 'DNS':

		DNSDataResult = api.DNSData(req=request)
		print repr(DNSDataResult)
		# Example Result: {u'DNSAuthDetails': {u'PointerType': u'CNAME', u'DNSEntry': u'sadxoi5spfy8axlgu9lpcga55wncn6bo.dvtest.alwaysonssl.com.', u'DNSValue': u's20160322210004.dvtest.alwaysonssl.com.'}, u'success': True}
		# Create a CNAME entry like this:
		#	sadxoi5spfy8axlgu9lpcga55wncn6bo.dvtest.alwaysonssl.com. IN CNAME s20160322210004.dvtest.alwaysonssl.com.

	elif DVAuthMethod == 'FILE':

		FileDataResult = api.FileData(req=request)
		print repr(FileDataResult)
		# Example Result: {u'FileAuthDetails': {u'FileContents': u'20160817082955250uyhevt9xaauim6pvk4yx5p50su4z2u8atievmbgk3r7gppp', u'FileName': u'http://testdv.alwaysonssl.com/.well-known/pki-validation/fileauth.htm'}, u'success': True}
		# Create the file /.well-known/pki-validation/fileauth.htm
		#	and use 20160817082955250uyhevt9xaauim6pvk4yx5p50su4z2u8atievmbgk3r7gppp as the files content


	""" Now we can request the AlwaysOnSSL certificate.
	"""
	request = {
		'OrderParameters': {
			"ProductCode": "AlwaysOnSSL.AlwaysOnSSL",
			"CSR": CSR,
			"ValidityPeriod": 180,
			"DVAuthMethod": DVAuthMethod
		}
	}

	OrderResult = api.Order(req=request)
	print repr(OrderResult)

	# Example Result: {u'Timestamp': u'2016-03-22T14:03:33Z', u'OrderParameters': {u'ProductCode': u'AlwaysOnSSL.AlwaysOnSSL', u'DVAuthMethod': u'DNS', u'PartnerOrderID': u'APIR-3F3PWARU2KCNEQ4OWXEO2Y3H', u'ValidityPeriod': 180, u'CSR': u'YourCSR', u'SignatureHashAlgorithm': u'SHA256-FULL-CHAIN'}, u'CertCenterOrderID': 6260500, u'success': True, u'Fulfillment': {u'Certificate_PKCS7': u'-----BEGIN PKCS #7 SIGNED DATA-----{...}-----END PKCS #7 SIGNED DATA-----', u'Intermediate': u'-----BEGIN CERTIFICATE-----{...}-----END CERTIFICATE-----', u'Certificate': u'-----BEGIN CERTIFICATE-----{...}-----END CERTIFICATE-----\n'}}
