#!/bin/bash
# Based on https://github.com/bioconda/bioconda-recipes/blob/a9090ef7e7ff15215dd8a0624c7154f66259fccc/recipes/peptide-shaker/build.sh
set -eu -o pipefail

outdir=$PREFIX/share/$PKG_NAME-$PKG_VERSION-$PKG_BUILDNUM
mkdir -p $outdir
mkdir -p $PREFIX/bin
cp -R lib/* $outdir/
cp $RECIPE_DIR/bioformats2raw.py $outdir/bioformats2raw
ls -l $outdir
ln -s $outdir/bioformats2raw $PREFIX/bin
chmod 0755 "${PREFIX}/bin/bioformats2raw"
