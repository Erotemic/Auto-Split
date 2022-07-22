#!/bin/bash
__doc__="
Run this from the repo root directory
"
pip install -r scripts/requirements-linux.txt
mkdir -p ./src/gen
pyuic6 './res/about.ui' -o './src/gen/about.py'
pyuic6 './res/design.ui' -o './src/gen/design.py'
pyuic6 './res/settings.ui' -o './src/gen/settings.py'
pyuic6 './res/update_checker.ui' -o './src/gen/update_checker.py'

BUILD_NUMBER=$(date +'%Y%m%d%H%M%S')
echo "AUTOSPLIT_BUILD_NUMBER = '$BUILD_NUMBER'" > src/gen/build_number.py

# Run the program
(cd src && python AutoSplit.py)