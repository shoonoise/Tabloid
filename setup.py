#!/usr/bin/env python
from setuptools import setup

if __name__ == '__main__':
    setup(name='tabloid',
          version='0.1',
          description='Make your terminal pretty',
          author='Alexander Kushnarev',
          author_email='avkushnarev@gmail.com',
          url='https://github.com/shoonoise/tabloid',
          packages=['tabloid'],
          install_requires=['colorama'])
