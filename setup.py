import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_requires = []


long_description="""Flexible dotted dictionary

A dictionary that allows access to keys via the dot operator, so that instance.value is equivalent to instance['value'].

Github repository: https://github.com/ailling/flexible-dotdict
"""


setup(
    name='flexible-dotdict',
    version='0.2.1',
    description='A dictionary that allows access to keys via the dot operator',
    long_description=long_description,
    author='Alan Illing',
    author_email='alanilling@gmail.com',
    url='https://github.com/ailling/flexible-dotdict',
    packages=['dotdict'],
    package_data={'dotdict': ['VERSION']},
    install_requires=install_requires,
    scripts=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
