#!/usr/bin/env python3
"""
The script saves the ports repository page with a css file to the /tmp/ folder.

It takes one or none argument. The argument defines the css style (file) which
is going to be used. The default style is "original".
"""

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from cruxpy.portspage import page

style = sys.argv[1] if len(sys.argv) > 1 else "original"

p = page("../../wawrzek", style=style)
p.read_repo()
p.write("/tmp/ports.html")
p.write_style("/tmp")
