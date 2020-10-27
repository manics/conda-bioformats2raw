#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys

from setuptools import setup, find_packages
with open('meta.yaml') as f:
    version = re.match(r'{% set version = "(.+)"', f.read()).group(1)
setup(
    name="bioformats2raw-wrapper",
    version=version,
    description="bioformats2raw wrapper",
    py_modules=['bioformats2raw_wrapper'],
    python_requires=">=3",
)
