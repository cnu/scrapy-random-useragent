"""
Setup script for PyPi
"""
import codecs
import re
from setuptools import setup


# Get the long description from the relevant file
with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


# Open the package file so we can read the meta data.
with codecs.open('random_useragent.py', encoding='utf-8') as f:
    package_file = f.read()


def get_package_meta(meta_name):
    """Return value of variable set in the package where said variable is
    named in the Python meta format `__<meta_name>__`.
    """
    regex = "__{0}__ = ['\"]([^'\"]+)['\"]".format(meta_name)
    return re.search(regex, package_file).group(1)


version = get_package_meta('version')
author = get_package_meta('author')
email = get_package_meta('email')
license = get_package_meta('license')


setup(
    name='scrapy-random-useragent',
    version=version,

    description='Scrapy Middleware to set a random User-Agent for every Request.',
    long_description=long_description,

    author=author,
    author_email=email,
    url='https://github.com/cnu/scrapy-random-useragent',

    license=license,

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
