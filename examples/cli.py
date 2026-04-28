#!/usr/bin/env python3
"""
Simple example how to check port information from the CLI.
The script takes a path to the port from first argument. Or, if it isn't
provided as it iteratively.

To simplify the script ignores git information, and therefore doesn't require
cruxpy dependencies.
"""

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from cruxpy.repo import port as cruxport
from pprint import pprint

port = sys.argv[1] if len(sys.argv) > 1 else input("Please specify the path to a port > ")

p = cruxport(port+"/Pkgfile", git_info=False)

print ("Port fields")
pprint (p.fields)

print ("=" * 20)
print ("URL is %s" %p.url)
