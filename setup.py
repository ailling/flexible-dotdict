import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_requires = []

# long_description = ''
with open('description.txt', 'r') as f:
    long_description = f.read()

def get_version():
    # sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'flexible-dotdict'))
    # from version import VERSION
    # v = VERSION
    # sys.path.pop(0)
    # return v
    from dotdict import VERSION
    return VERSION


setup(
    name='flexible-dotdict',
    version=get_version(),
    description='A dictionary that allows access to keys via the dot operator',
    long_description=long_description,
    author='Alan Illing',
    author_email='alanilling@gmail.com',
    url='',
    packages=[],
    package_data=['VERSION', 'description.txt'],
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
