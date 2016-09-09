# coding: utf-8
import re
import ast
from setuptools import setup


_version_re = re.compile(r'version\s+=\s+(.*)')
with open('coroutx/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='coroutx',
    version=version,
    url='https://github.com/neo1218/coroutx/',
    license='MIT',
    author='neo1218',
    author_email='neo1218@yeah.net',
    description='dead simple async python web framework',
    long_description=__doc__,
    packages=['coroutx'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Werkzeug',
        'gevent',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
