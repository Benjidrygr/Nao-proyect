#!/bin/bash

# Resolve script's directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Path to the python.org Python 2.7 framework install
PYTHON="/Library/Frameworks/Python.framework/Versions/2.7/bin/python"

# Set environment variables for NAOqi
export PYTHONPATH="${PYTHONPATH}:${SCRIPT_DIR}/sdk/pynaoqi-python2.7-2.8.6.23-mac64-20191127_144231/lib/python2.7/site-packages"
export DYLD_LIBRARY_PATH="${DYLD_LIBRARY_PATH}:${SCRIPT_DIR}/sdk/pynaoqi-python2.7-2.8.6.23-mac64-20191127_144231/lib"

# Optional debug output
# echo "Using Python: $PYTHON"
# echo "PYTHONPATH: $PYTHONPATH"
# echo "DYLD_LIBRARY_PATH: $DYLD_LIBRARY_PATH"

# Run your Python script with arguments
"$PYTHON" main.py