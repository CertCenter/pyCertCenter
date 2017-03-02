#!/usr/bin/env python
# -*- coding: utf-8 -*-

import CertCenter

api = CertCenter.CertAPI(OutputBehavior='dict')
api.setBearer('AValidToken.oauth2.certcenter.com')

CommonName = 'www.example.com'

# 1. Check the blacklist
#
request = {
  'CommonName': CommonName
  'GeneratePrivateKey': True,
}
resValidateName = api.ValidateName(req=request)

if not resValidateName['IsQualified']:
  sys.exit("CommonName is not qualified (blacklisted)");

print "Your PrivateKey (save it):\n"
print resValidateName['PrivateKey']

# 2. Fetch file name and hash
#
resFileData = api.FileData(req={
  "ProductCode": "AlwaysOnSSL.AlwaysOnSSL",
  # Of course, CSR will be provided by ValidateName(),
  # because we set 'GeneratePrivateKey' to true
  "CSR": resValidateName['CSR'],
})

# 3. Save the hash in CertCenter's free key value database
#
api.setKvStoreAuthorizationKey("#AValidAPIToken#")
resKvStore = api.KvStore(req={
  "Key": CommonName,
  "Value": resFileData['FileAuthDetails']['FileContents'],
})

# 4. Submit the order
#
resOrder = api.Order(req={
  'OrderParameters': {
    "ProductCode": "AlwaysOnSSL.AlwaysOnSSL",
    "CSR": resValidateName['CSR'],
    "ValidityPeriod": 180,
    "DVAuthMethod": 'FILE',
  }
})

print "Certificate fulfillment:\n\n"
print repr(resOrder)
