"""
weppy is a full-stack python web framework designed with simplicity in mind.


Links
-----

* `website <http://weppy.org>`_
* `documentation <http://weppy.org/docs>`_
* `git repo <http://github.com/gi0baro/weppy>`_

"""

import ast
import re

from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('weppy/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='weppy',
    version=version,
    url='http://github.com/gi0baro/weppy/',
    license='BSD',
    author='Giovanni Barillari',
    author_email='gi0baro@d4net.org',
    description='The web framework for humans',
    long_description=__doc__,
    packages=[
        'weppy',
        'weppy.asgi', 'weppy.asgi.loops', 'weppy.asgi.protocols',
        'weppy.language', 'weppy.language.plurals',
        'weppy.orm', 'weppy.orm.migrations',
        'weppy.templating',
        'weppy.testing',
        'weppy.tools', 'weppy.tools.auth',
        'weppy.validators',
        'weppy.libs'
    ],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'aiofiles==0.4.0',
        'click>=0.6',
        'pendulum>=2.0.0',
        'pyaes',
        'pyDAL==17.3',
        'pyyaml',
        'uvicorn~=0.3.20',
        # 'uvloop==0.11.3'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts': ['weppy = weppy.cli:main']
    }
)
