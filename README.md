# Installation

As this project now is a part of the <a href="https://pypi.python.org/pypi/CertCenter/">Python Package Index</a>
you may be able to install the CertCenter module with a single command:

```
$ pip install CertCenter
```

If pip is not installed on your computer, you <a href="https://pip.pypa.io/en/stable/installing/" target="_blank">should read this</a>.


# Usage

```python
# Import the module
import CertCenter

# Instantiate
api = CertCenter.CertAPI()

# Set authentication information (valid OAuth2 bearer token)
api.setBearer('XYZXYZXYZ.oauth2.certcenter.com')

# Call a method (for instance, the Limit method)
api.Limit()
```

# How can I get a valid OAuth2 bearer token?

It's quite easy and a howto is already available:

- <a target="_blank" href="https://blog.certcenter.com/2015/11/how-does-it-actually-work-to-access-the-certcenter-restful-api/">English version</a>
- <a target="_blank" href="https://blog.certcenter.de/2015/10/demo-zugriff-certcenter-restful-api/">German version</a>

# Which methods are available and what kind of data do I need?

Please refer to the detailed REST API documentation:

- <a target="_blank" href="https://api.certcenter.help/rest-api-doc-en/">English version</a>
- <a target="_blank" href="https://api.certcenter.help/rest-api-doc-de/">German version</a>

You may pass all required data as dict objects as demonstrated in this projects <a href="https://github.com/CertCenter/pyCertCenter/tree/master/examples">example implementations</a>.


# Documentation

An extensive API and module documentation is available at https://api.certcenter.help
