#!/bin/bash
# Based on https://github.com/bioconda/bioconda-recipes/blob/a9090ef7e7ff15215dd8a0624c7154f66259fccc/recipes/peptide-shaker/build.sh
set -eu -o pipefail

sharedir=$PREFIX/share
outdir=$sharedir/$PKG_NAME-$PKG_VERSION-$PKG_BUILDNUM

mkdir -p $outdir
cp -R lib/* $outdir/
cp -R $RECIPE_DIR/bioformats2raw_launcher $RECIPE_DIR/setup.py .

sed -i.bak "s/%JAR_DIRNAME%/$PKG_NAME-$PKG_VERSION-$PKG_BUILDNUM/" bioformats2raw_launcher/__init__.py
rm bioformats2raw_launcher/__init__.py.bak
python -m pip install --no-deps --ignore-installed .
