#!/usr/bin/env python3
''' Installation script for glmtools package '''
from os.path import join as pjoin
from glob import glob

import setuptools

from distutils.core import setup

setup(name='glmtools',
      version='0.1',
      description='Tools for running the GLM',
      packages=['glmtools'],
      license='BSD license',
      author='Your name here',
      author_email='yourname@berkeley.edu',
      maintainer='Your name here',
      maintainer_email='yourname@berkeley.edu',
      url='http://github.com/psych-214-fall-2016/glmtools',
      package_data = {'glmtools': [pjoin('tests', '*')]},
      # Add all the scripts in the scripts directory
      scripts = glob(pjoin('scripts', '*')),
      requires=['numpy (>=1.5.1)', 'scipy (>=0.16.0)'],
      )
