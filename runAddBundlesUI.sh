#!/bin/bash

# Get the directory of the current script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Open the file located in the parent directory
python3 "$DIR/addBundlesUI.py"
