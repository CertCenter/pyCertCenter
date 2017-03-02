#!/usr/bin/env python
# -*- coding: utf-8 -*-

import CertCenter

api = CertCenter.CertAPI(OutputBehavior='dict')
api.setBearer('AValidToken.oauth2.certcenter.com')

""" Fetching current account limitations
"""
#print api.Limit()

""" Fetching available product codes
"""
#print api.Products()

""" Fetching product information
"""
#request = { "ProductCode": "GlobalSign.ExtendedSSL" }
#print api.ProductDetails(req=request)

""" Fetching profile information
"""
#print api.Profile()

""" Get a quote
"""
# request = {
# 	"ProductCode": "GlobalSign.ExtendedSSL",
# 	"SubjectAltNameCount": 2,
# 	"ValidityPeriod": 12,
# 	"ServerCount": 1
# }
# print api.Quote(req=request)

""" Verify and parse a Certificate Signing Request (CSR)
"""
# request = {
# 	"CSR": """-----BEGIN CERTIFICATE REQUEST-----
# MIIBVTCB/QIBADCBmjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNPMRkwFwYDVQQH
# ExBDb2xvcmFkbyBTcHJpbmdzMRkwFwYDVQQKExBTdXBlciBNYWxsLCBJbmMuMR8w
# HQYDVQQDExZ3d3cuc3VwZXItbWFsbC1pbmMuY29tMScwJQYJKoZIhvcNAQkBFhhh
# ZG1pbkBzdXBlci1tYWxsLWluYy5jb20wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC
# AAT4E1K5QOPD55LbB7x8ydEJhVa69SpScj5at6R1f8HdBckhuXvxJX+XvaLQvA0d
# M6aZFEfcPlzoLgmTbtcnUEWloAAwCQYHKoZIzj0EAQNIADBFAiAB0XTEhsle2SNb
# A2462JcRYBSAWf4gSRUHpCxCRHm6OQIhAK6rn6B40kh4EdAvuL9BaCQjeU0HHIG9
# lj1JDQDKSbBZ
# -----END CERTIFICATE REQUEST-----
#"""
# }
# print api.ValidateCSR(req=request)

""" Request User Agreement for ProductCode
"""
#request = {
#	'ProductCode': 'GeoTrust.QuickSSLPremium'
#}
#print api.UserAgreement(req=request)

""" Fetch valid email adresses for a EMAIL based domai validation order.
"""
# request = {
# 	'CommonName': 'www.certcenter.com',
# 	'ProductCode': 'GeoTrust.QuickSSLPremium'
# }
# print api.ApproverList(req=request)

""" Request data for TestOrder/Order methods.
"""
# request = {
#   "OrganizationInfo": {
# 	"OrganizationName": "Super Mall, Inc.",
# 	"OrganizationAddress": {
# 		"AddressLine1": "5550 E Woodmen Rd",
# 		"PostalCode": "80920",
# 		"City": "Colorado Springs",
# 		"Region": "CO",
# 		"Country": "US",
# 		"Phone": "string",
# 		"Fax": "string",
# 		"Phone": "+1 719-111-111",
# 		"Fax": "+1 719-111-112"
# 	}
#   },
#   "OrderParameters": {
#     "ProductCode": "GlobalSign.OrganizationSSL",
#     "IsCompetitiveUpgrade": False,
#     "SubjectAltNames": [
#       "www.super-mall-inc.net",
#       "www.super-mall-inc.de"
#     ],
#     "PartnerOrderID": "WhatEverYouWant-ItsYourOrderIdentifier",
#     "IsRenewal": False,
#     "ServerCount": 1,
#     "SignatureHashAlgorithm": "SHA256-ECC-HYBRID",
#     "CSR": """-----BEGIN CERTIFICATE REQUEST-----
# MIIBVTCB/QIBADCBmjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNPMRkwFwYDVQQH
# ExBDb2xvcmFkbyBTcHJpbmdzMRkwFwYDVQQKExBTdXBlciBNYWxsLCBJbmMuMR8w
# HQYDVQQDExZ3d3cuc3VwZXItbWFsbC1pbmMuY29tMScwJQYJKoZIhvcNAQkBFhhh
# ZG1pbkBzdXBlci1tYWxsLWluYy5jb20wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNC
# AAT4E1K5QOPD55LbB7x8ydEJhVa69SpScj5at6R1f8HdBckhuXvxJX+XvaLQvA0d
# M6aZFEfcPlzoLgmTbtcnUEWloAAwCQYHKoZIzj0EAQNIADBFAiAB0XTEhsle2SNb
# A2462JcRYBSAWf4gSRUHpCxCRHm6OQIhAK6rn6B40kh4EdAvuL9BaCQjeU0HHIG9
# lj1JDQDKSbBZ
# -----END CERTIFICATE REQUEST-----
# """,
#     "Email": "domains@super-mall.com",
#     "ValidityPeriod": 12
#   },
#   "AdminContact": {
#     "Title": "CIO",
#     "FirstName": "John",
#     "LastName": "Doe",
#     "OrganizationName": "Super Mall, Inc.",
#     "OrganizationAddress": {
#       "AddressLine1": "5550 E Woodmen Rd",
#       "PostalCode": "80920",
#       "City": "Colorado Springs",
#       "Region": "CO",
#       "Country": "US"
#     },
#     "Phone": "+1 719-111-111",
#     "Fax": "+1 719-111-112",
#     "Email": "admin@super-mall.com"
#   },
# }
# request['TechContact'] = request['AdminContact']

""" Test a certificate order
"""
# print api.TestOrder(req=request)

""" Order a certificate
"""
# print api.Order(req=request)

""" Query required DNS CNAME details for AlwaysOnSSL orders
"""
# request = {
#     "ProductCode": "AlwaysOnSSL.AlwaysOnSSL",
#     "CSR": """-----BEGIN CERTIFICATE REQUEST-----
# MIIEtDCCApwCAQAwbzELMAkGA1UEBhMCREUxDzANBgNVBAgTBkhlc3NlbjEQMA4G
# A1UEBxMHR2llc3NlbjEWMBQGA1UEChMNQ2VydENlbnRlciBBRzElMCMGA1UEAxMc
# ZWUtdGVzdC0wMDAwMS5jZXJ0Y2VudGVyLmNvbTCCAiIwDQYJKoZIhvcNAQEBBQAD
# ggIPADCCAgoCggIBAOTAPEoB9iU9CXITRbF8GkChpcXfPzv4DyWynNOAjE3QtKzh
# AQFFrHEfk7LG8hVHa+hT83ZOom8pZlvQwT4HRwsTFdVdzkSvrUGN3QqmRxYopeS3
# WCk4aTYDCTutm2y04fOiWMHlNxVGg7eWYse8IAqaQH66wa4mcBhc0JbkuDLYmq/j
# xb1Cl+/z1DJK/SZArpAC3rxdk8ZMnHPmAEtU2KW/ZLmXSb/deNrqhikD47TWw5U2
# g/iUFbp8N9hi40wKITIGiVZ7mHDl0Fgr5xZXC4G8fsdtSFB54hy47TfusX3nssL7
# zLfy/01RmpZMCxpg2AY/jOZOv8OT7+2PxuyTI2ufuI1aNyxmnkBY4i9E/rs1RTpo
# zow0hYiRjUdYxfied9QFsbK3QZzbvrcDDrAt1qW2Tk5K4waXaGRttrRJVDNOE6jL
# 9CojmJSBp4DnD60nqXEIBAN53IEi4G7k5SBrZxwvQgf6puc3l7LsZhq0acX72245
# HWANrQu++mYRHB6IldXeHzGr0CEKuF/DR2MM8H+3sC5cd3FX4FUrnfpAM2ASCeB8
# +o2BlDWlfNJa+p9i/YCdkprDY7hV2yBfxUZ1l7UFnaAEV880e1SOkaKzfttb755J
# Mwi5++kbdBHBS4yHBaFBx/8kC78Ewgt1siMO+oitjd4txgAOdV/EW2m8MKqpAgMB
# AAGgADANBgkqhkiG9w0BAQsFAAOCAgEA2DfsP7uYgjW685llz086TEC9E/Z263VC
# inCBLjkxQ/rAFYyNI1nRlr0lTToxn7tcHEBIpRl8jUJOx762krFNRbaZKJly3HSb
# PQ3MLs44lPWbSGTRcjqeItpgo5VeY/2tXaYgBfppSWE+33yMq/OXwKZh21S8vpa5
# dClIgoNWnXQbqNYcdlHxGqCgNUDvkFhV8c7b+Ak0UdJhMO6bpP+B00usA71uG+e7
# b+vQ03hjIbx9RLDXp1CLpIGKr5YNqaRrtqu0vgLJqrFUON067ERWXXRtqK2yN/5v
# Jx69LkeSCtjQavNx5dXngAGk87AIViUPKpy7eOOznH4me+naAo6TRz18eNNywvkL
# tD8Mf9DQuiILC7y1rWKQ5kkP+J9ZVY9upZDXdJ44sU5eR1HAVUcEpx81cU8kr8rv
# J2V3mZqWZzwrsN7oD2PhDzWWScOkgSZhVDtoSghm5b6LT2OzqCxbGgZd6p1bievW
# P9Lnt6ddDuO09O6t/5LI1mrt+h3MYrqKI69yqGX36UdHoGjCKZ8KSFKQIBH+/NLB
# dgNM1Xxt4xBTyrCBfDk7ZEsU08Ua55rzfOtVTBWVvE4ljNI2zifODc9V6SpJjruY
# ON3lknn9CBo7HpgmiJz471k8kOqHVLyx9J3t6rXkPFaiIJl46cz0Aa5POAU7CDnQ
# B8xejz8WMbM=
# -----END CERTIFICATE REQUEST-----"""
# }
# print api.DNSData(req=request)

""" Order a AlwaysOnSSL certificate
"""
# request = {
#   "OrderParameters": {
#     "ProductCode": "AlwaysOnSSL.AlwaysOnSSL",
#     "CSR": """-----BEGIN CERTIFICATE REQUEST-----
# MIIEtDCCApwCAQAwbzELMAkGA1UEBhMCREUxDzANBgNVBAgTBkhlc3NlbjEQMA4G
# A1UEBxMHR2llc3NlbjEWMBQGA1UEChMNQ2VydENlbnRlciBBRzElMCMGA1UEAxMc
# ZWUtdGVzdC0wMDAwMS5jZXJ0Y2VudGVyLmNvbTCCAiIwDQYJKoZIhvcNAQEBBQAD
# ggIPADCCAgoCggIBAOTAPEoB9iU9CXITRbF8GkChpcXfPzv4DyWynNOAjE3QtKzh
# AQFFrHEfk7LG8hVHa+hT83ZOom8pZlvQwT4HRwsTFdVdzkSvrUGN3QqmRxYopeS3
# WCk4aTYDCTutm2y04fOiWMHlNxVGg7eWYse8IAqaQH66wa4mcBhc0JbkuDLYmq/j
# xb1Cl+/z1DJK/SZArpAC3rxdk8ZMnHPmAEtU2KW/ZLmXSb/deNrqhikD47TWw5U2
# g/iUFbp8N9hi40wKITIGiVZ7mHDl0Fgr5xZXC4G8fsdtSdB54hy47TfusX3nssL7
# zLfy/01RmpZMCxpg2AY/jOZOv8OT7+2PxuyTI2ufuI1aNyxmnkBY4i9E/rs1RTpo
# zow0hYiRjUdYxfied9QFsbK3QZzbvrcDDrAt1qW2Tk5K4waXaGRttrRJVDNOE6jL
# 9CojmJSBp4DnD60nqXEIBAN53IEi4G7k5SBrZxwvQgf6puc3l7LsZhq0acX72245
# HWANrQu++mYRHB6IldXeHzGr0CEKuF/DR2MM8H+3sC5cd3FX4FUrnfpAM2ASCeB8
# +o2BlDWlfNJa+p9i/YCdkprDY7hV2yBfxUZ1l7UFnaAEV880e1SOkaKzfttb755J
# Mwi5++kbdBHBS4yHBaFBx/8kC78Ewgt1siMO+oitjd4txgAOdV/EW2m8MKqpAgMB
# AAGgADANBgkqhkiG9w0BAQsFAAOCAgEA2DfsP7uYgjW685llz086TEC9E/Z263VC
# inCBLjkxQ/rAFYyNI1nRlr0lTToxn7tcHEBIpRl8jUJOx762krFNRbaZKJly3HSb
# PQ3MLs44lPWbSGTRcjqeItpgo5VeY/2tXaYgBfppSWE+33yMq/OXwKZh21S8vpa5
# dClIgoNWnXQbqNYcdlHxGqCgNUDvkFhV8c7b+Ak0UdJhMO6bpP+B00usA71uG+e7
# b+vQ03hjIbx9RLDXp1CLpIGKr5YNqaRrtqu0vgLJqrFUON067ERWXXRtqK2yN/5v
# Jx69LkeSCtjQavNx5dXngAGk87AIViUPKpy7eOOznH4me+naAo6TRz18eNNywvkL
# tD8Mf9DQuiILC7y1rWKQ5kkP+J9ZVY9upZDXdJ44sU5eR1HAVUcEpx81cU8kr8rv
# J2V3mZqWZzwrsN7oD2PhDzWWScOkgSZhVDtoSghm5b6LT2OzqCxbGgZd6p1bievW
# P9Lnt6ddDuO09O6t/5LI1mrt+h3MYrqKI69yqGX36UdHoGjCKZ8KSFKQIBH+/NLB
# dgNM1Xxt4xBTyrCBfDk7ZEsU08Ua55rzfOtVTBWVvE4ljNI2zifODc9V6SpJjruY
# ON3lknn9CBo7HpgmiJz471k8kOqHVLyx9J3t6rXkPFaiIJl46cz0Aa5POAU7CDnQ
# B8xejz8WMbM=
# -----END CERTIFICATE REQUEST-----
# """,
#     "ValidityPeriod": 90		## DAYS, not months!
#   }
# }
#print api.Order(req=request)

""" Lookup orders
"""
# request = {
# 	'Status': 'COMPLETE',
# 	'ProductType': 'SSL',
# 	'CommonName': '*.%',
# 	'Page': 1,
# 	'ItemsPerPage': 1000,
# 	'OrderBy': 'ID',
# 	'OrderDir': 'DESC',
# 	'includeFulfillment': False,
# 	'includeOrderParameters': False,
# 	'includeBillingDetails': False,
# 	'includeContacts': False,
# 	'includeOrganizationInfos': False
# }
# print api.Orders(req=request)

""" Lookup modified orders
"""
# request = {
# 	'FromDate': '2015-11-19T00:00:00Z',
# 	'ToDate': '2015-11-21T00:00:00Z',
# 	'includeFulfillment': False,
# 	'includeOrderParameters': False,
# 	'includeBillingDetails': False,
# 	'includeContacts': False,
# 	'includeOrganizationInfos': False
# }
# print api.ModifiedOrders(req=request)

""" Fetch information about a certain order
"""
# request = {
# 	'CertCenterOrderID': 1234567890,
# 	'includeFulfillment': False,
# 	'includeOrderParameters': False,
# 	'includeBillingDetails': False,
# 	'includeContacts': False,
# 	'includeOrganizationInfos': False
# }
# print api.GetOrder(req=request)

""" Fetch information about a certain order
"""
# request = {
# 	'CertCenterOrderID': 1234567890,
# 	'OrderParameters': {
# 		'SignatureHashAlgorithm': 'SHA256-FULL-CHAIN',
# 		'DVAuthMethod': 'EMAIL',
# 		'CSR': """-----BEGIN NEW CERTIFICATE REQUEST-----
# MIIGbjCCBFYCAQAwdDELMAkGA1UEBhMCREUxDzANBgNVBAgMBkhlc3NlbjEQMA4G
# A1UEBwwHR2llc3NlbjEWMBQGA1UECgwNQ2VydENlbnRlciBBRzEMMAoGA1UECwwD
# bi9hMRwwGgYDVQQDDBNkZW1vLmNlcnRjZW50ZXIuY29tMIICIjANBgkqhkiG9w0B
# AQEFAAOCAg8AMIICCgKCAgEA4W6OXkU3AJvbMJC/6UEsTad35wXZ4DLzz032U8HZ
# cBNsjg6fqAeQps0de3dYEQLTqj0q3cu3bzzG0F3Uyu3EIwsq93voKDkKY0E3syWL
# XtCbWzVwDpbT9wAQ1Ldcoe36k7BM3TeCITO1vaSRKqQ1bf051OnXfXGjQb9MsznN
# TEvHoeHxH38Or85tba3WDD5p6roDc0lJh6wRHUNEw/nZ8E2BAHQcFzxJQvKNM9KB
# rrDF9jQAoRbbDUzbIVEcf66v
# -----END NEW CERTIFICATE REQUEST-----"""
# 	},
# }
# print api.Reissue(req=request)

""" Update approvers email address
"""
# request = {
# 	'CertCenterOrderID': 1234567890,
# 	'ApproverEmail': 'admin@exmaple.com'
# }
# print api.UpdateApproverEmail(req=request)

""" Resend the Approver Email
"""
# request = {
# 	'CertCenterOrderID': 1234567890,
# }
# print api.ResendApproverEmail(req=request)

""" Cancel a certificate
"""
# request = {
# 	'CertCenterOrderID': 1234567890,
# }
# print api.CancelOrder(req=request)

""" Revoke a cancelled certificate
"""
# request = {
# 	'CertCenterOrderID': 1234567890,
# 	'RevokeReason': 'Key compromised',
# 	'Certificate': """-----BEGIN CERTIFICATE-----
# MIIF9DCCBNygAwIBAgISESFmIcxYP/Sni/D+JNTAGTn2MA0GCSqGSIb3DQEBCwUA
# MGAxCzAJBgNVBAYTAkJFMRkwFwYDVQQKExBHbG9iYWxTaWduIG52LXNhMTYwNAYD
# VQQDEy1HbG9iYWxTaWduIERvbWFpbiBWYWxpZGF0aW9uIENBIC0gU0hBMjU2IC0g
# c3AyLmdsb2JhbHNpZ24uY29tL2dzZG9tYWludmFsc2hhMmcyMB0GA1UdDgQWBBS7
# osGxxbQ36FP3rztgq3Qkw0s83zAfBgNVHSMEGDAWgBTqTnzUgC3lFYGGJoyCbcCY
# pM+XDzANBgkqhkiG9w0BAQsFAAOCAQEAA45xDJ+N10maaDSG2dXMdnFemO7m1T3U
# SAmx7M+vbQHggCwfI4LbQ8Sdv34fZEy+TFTjdP4gnGzuOdyqdzbUQ1eIU2g825qs
# U9RiWWWYEFctSlCJz7uZCuv7IAQSpmRYeRJTxYgbB1r/wLRpe5YPOJKneMhVsXXb
# uPsjgVLkb+qKIduTfHaXZGbLbOwJskBVpiQn/q3D5V5tTfiguWO3R3NiZCkp++I8
# ua7e9NFy2gcnzCWKuzbjHhl/2lkkV+gSnLnLQQ4H8Gc++N1Wx7e/tD4MpMdVMsWa
# 1Mpgjeodu1toGRwerxyPB8LuabwFtT/0vPG/IhfOBM+7NlYYf7lriA==
# -----END CERTIFICATE-----""",
# }
# print api.Revoke(req=request)

""" Get informations about your vouchers
"""
# print api.GetVouchers()

""" Get informations about a particular vouchers
"""
# request = {
# 	'VoucherCode': '0L8EVQ4WTNTH',
# }
# print api.GetVoucher(req=request)

""" Allows you to invalidate a particular voucher
"""
# request = {
# 	'VoucherCode': '0L8EVQ4WTNTH',
# }
# print api.DeleteVoucher(req=request)

