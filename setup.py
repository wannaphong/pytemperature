# -*- coding: utf-8 -*-
from os import path
from setuptools import find_packages, setup
basedir = path.abspath(path.dirname(__file__))
def read(*paths):
    with open(path.join(basedir,paths), 'r', encoding='utf-8-sig') as f:
        return f.read()
setup(
	name='pytemperature',
	version='1.1',
	packages=['pytemperature'],
	url='https://github.com/wannaphong/pytemperature',
	license='MIT',
	author='Wannaphong Phatthiyaphaibun',
	author_email='wannaphong@yahoo.com',
	keywords = "temperature science",
	description='Scale of temperature',
	long_description=(read('README.md')),
	long_description_content_type="text/markdown",
	classifiers= [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: Implementation :: CPython',
		'Programming Language :: Python :: Implementation :: IronPython'
		'Programming Language :: Python :: Implementation :: Jython'
		'Programming Language :: Python :: Implementation :: PyPy'
		'Topic :: Scientific/Engineering',
	],
)
