#!/bin/bash
# setup vfeed, make the code importable from the falco code
# 
git clone https://github.com/toolswatch/vfeed
echo "import vfeed" > vfeed/__init__.py
