#!/usr/bin/env python
from setuptools import setup

setup(
    name='midi',
    version='v0.2.3',
    description='Python MIDI API',
    author='giles hall',
    author_email='ghall@csh.rit.edu',
    package_dir={'midi': 'src'},
    packages=['midi'],
    scripts=[
        'scripts/mididump.py',
    ],
)
