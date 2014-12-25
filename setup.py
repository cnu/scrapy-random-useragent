"""
Setup script for PyPi
"""
import codecs
from setuptools import setup

import random_useragent

# Get the long description from the relevant file
with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='scrapy-random-useragent',
    version=random_useragent.__version__,

    description='Scrapy Middleware to set a random User-Agent for every Request.',
    long_description=long_description,

    author=random_useragent.__author__,
    author_email=random_useragent.__email__,
    url='https://github.com/cnu/scrapy-random-useragent',

    license=random_useragent.__license__,

    py_modules=['random_useragent'],
    platforms=['Any'],

    keywords="scrapy random user-agent ",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Scrapy',
    ]
)