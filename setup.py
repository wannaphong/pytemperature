import os
from distutils.core import setup
def read(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()
setup(
	name='pytemperature',
	version='1.1',
	packages=['pytemperature'],
	url='https://python3.wannaphong.com',
	license='MIT',
	author='Wannaphong Phatthiyaphaibun',
	author_email='wannaphong@yahoo.com',
	keywords = "temperature science",
	description='Scale of temperature',
	long_description=(read('README.txt')),
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
