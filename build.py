#!/usr/bin/env python
import os
import shutil
import subprocess

sharedir = os.path.join(os.getenv('PREFIX'), 'share')
pkg = '-'.join(os.getenv(v) for v in ['PKG_NAME', 'PKG_VERSION', 'PKG_BUILDNUM'])
outdir = os.path.join(sharedir, pkg)

recipedir = os.getenv('RECIPE_DIR')

os.makedirs(sharedir, exist_ok=True)
shutil.copytree(os.getenv('SRC_DIR'), outdir)

with open(os.path.join(recipedir, 'bioformats2raw_wrapper.template')) as f:
    txt = f.read().replace('PACKAGEDIR', pkg)
with open(os.path.join(recipedir, 'bioformats2raw_wrapper.py'), 'w') as f:
    f.write(txt)

subprocess.check_output(['pip', 'install', recipedir])
