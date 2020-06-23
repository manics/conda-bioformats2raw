from os import getenv
from setuptools import setup

setup(
    name='bioformats2raw_launcher',
    version=getenv('PKG_VERSION'),
    url='https://github.com/ome/conda-bioformats2raw',
    author='OME',
    description='bioformats2raw entrypoint',
    packages=['bioformats2raw_launcher'],
    entry_points = {
        'console_scripts': ['bioformats2raw=bioformats2raw_launcher:main'],
    }
)
