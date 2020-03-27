#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import re

import setuptools

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r'^__version__ = ['\']([^'\']*)['\']',
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='airnow.py',
    version=find_version('airnow', 'airnow.py'),
    author='0isamu',
    description='Obtain the latest U.S. air quality data and forecasts.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/0isamu/airnow.py',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Topic :: Software Development :: Version Control :: Git',
    ],
    python_requires='>=3',
)
