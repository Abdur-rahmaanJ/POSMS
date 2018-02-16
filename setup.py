# -*- coding: utf-8 -*-
"""
pyOSMS is a software relieving you from 
subscriber system mailing costs 
"""
from setuptools import setup, find_packages

NAME = 'pyosms'
AUTHOR = 'Abdur-Rahmaan Janhangeer'
VERSION = '1.0'
CONTACT = 'arj.python@gmail.com'
URL = 'https://github.com/Abdur-rahmaanJ/pyOSMS-PythonOpenSubscriberMailSystem'
LICENSE = 'MIT'

setup(
    name=NAME,
    version=VERSION,
    long_description=__doc__,
    author=AUTHOR,
    author_email=CONTACT,
    url=URL,
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    classifiers=['Intended Audience :: individuals',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.6'])
