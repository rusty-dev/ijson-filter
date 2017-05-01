#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='ijson-filter',
    version='1.0',
    description="Iterative JSON filter.",
    author="https://github.com/rusty-dev",
    author_email="rustykoc@gmail.com",
    url='https://github.com/rusty-dev/ijson-filter',
    packages=['ijson_filter'],
    include_package_data=True,
    install_requires=[
        'ijson>=2.3',
        'simplejson>=3.10.0',
        'click>=6.7'
    ],
    scripts=['ijson_filter/ijson-filter'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
