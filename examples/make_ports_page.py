#!/usr/bin/env python3
"""
The script creates the ports repository page for the ports in the 
"../../wawrzek" directory.

"""


from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from cruxpy.portspage import page

p = page(path="../../wawrzek")
p.read_repo()
p.write()
p.write_style()
