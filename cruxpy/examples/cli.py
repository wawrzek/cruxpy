#!/usr/bin/env python3
"""
Simple example how to check port information from the CLI.
It takes a path to the port.
Otherwise it is going to ask it.
"""

from pprint import pprint
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from repo import port as cruxport

port = sys.argv[1] if len(sys.argv) > 1 else input("Please specify the path to a port > ")

p = cruxport(port+"/Pkgfile", git_info=False)

print ("Port fields")
pprint (p.fields)

print ("=" * 20)
print ("URL is %s" %p.url)
