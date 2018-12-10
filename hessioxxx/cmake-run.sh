#!/bin/bash

# A steering script to build hessioxxx (and only hessioxxx
# but not the hessio module from HESS CVS) through cmake.
# To avoid replacing the provided Makefile, it makes sure
# to run cmake only from hessioxxx/build-cmake, optionally
# after creating a build-cmake sub-directory.

# The cmake configuration does not allow for the full range of
# configuration possibilities but just one configuration name.
# This could come from the environment or the command line.
mainconfig="CTA_MAX_SC"
if [ ! -z "${EXTRA_DEFINES}" ]; then
   mainconfig=$(echo "${EXTRA_DEFINES}" | sed 's/-D//g' | cut -d' ' -f1)
fi
if [ ! -z "$1" ]; then
   mainconfig=$(echo "$1" | sed 's/-D//g' | cut -d' ' -f1)
fi

curdir=$(/bin/pwd)
topdir=$(dirname "$curdir")
dncur=$(basename "$curdir")
dntop=$(basename "$topdir")

# echo "curdir=$curdir"
# echo "topdir=$topdir"
# echo "dncur=$dncur"
# echo "dntop=$dntop"

if [ "$dntop" != "hessioxxx" ]; then
   if [ "$dncur" != "hessioxxx" ]; then
      echo "This procedure is supposed to be run under hessioxxx only."
      exit 1
   fi
   # When running directly from hessioxxx, we go into build-cmake first
   if [ ! -d build-cmake ]; then
      mkdir build-cmake || exit 1
   fi
   cd build-cmake || exit 1

   curdir=$(/bin/pwd)
   topdir=$(dirname "$curdir")
   dncur=$(basename "$curdir")
   dntop=$(basename "$topdir")
fi

# After these preliminaries we should really be in hessioxxx/build-cmake

if [ "$dncur" != "build-cmake" ]; then
   echo "This procedures is supposed to be run in the build-cmake directory."
   exit 1
fi

export HESSIO_DIR="$topdir"

if [ ! -f "$topdir/eventio_version.h" ]; then
   echo '#define BASE_RELEASE "unknown: build-cmake"' > "$topdir/eventio_version.h"
   echo '#define EVENTIO_VERSION "'`date '+%F %T %Z'` '('`whoami`'@'`hostname`')"' >>"$topdir/eventio_version.h"
fi

# Use cmake to generate a Makefile and then use make to build things here:

cmake BuildConfig="$mainconfig" $HESSIO_DIR || exit 1

make || exit 1

# Install libraries and binaries where the normal procedure would put them:
# (But keep in mind that binaries may still load hessio/hessio++ from build-cmake/lib/.)

cp lib/* ../lib/
cp bin/* ../bin/

