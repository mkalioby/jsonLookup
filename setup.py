#!/usr/bin/env python
import setuptools
from distutils.core import setup

setup(name='jsonLookup',
      version='0.6.0',
      description='Search MySQL JSON fields in Django',
      author='Mohamed El-Kalioby',
      author_email='mkalioby@mkalioby.com',
      url='https://github.com/mkalioby/jsonLookup',
      packages=['jsonLookup'],
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      keywords = ['django','django', 'mysql'],
     )
