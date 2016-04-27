from setuptools import setup, find_packages
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='CertCenter',
    description='The official CertCenter API library',
    long_description=long_description,
    version=re.search('^__version__\s*=\s*"(.*)"', open('CertCenter.py').read(), re.M).group(1),
    url='https://github.com/CertCenter/pyCertCenter',
    author='CertCenter Development Team',
    author_email='pyCertCenter-dev@certcenter.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
		'Environment :: Plugins',
		'Intended Audience :: Developers',
        'Topic :: Security :: Cryptography',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Software Development :: Libraries'

    ],
    keywords='SSL TLS Encryption Certificates CertCenter Sockets',
    py_modules=["CertCenter"]
)
