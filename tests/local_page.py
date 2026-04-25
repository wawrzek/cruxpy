#!/usr/bin/env python3

import shutil
import sys
import os
sys.path.append(os.path.abspath("../cruxpy"))
sys.path.append(os.path.abspath(".."))
from portspage import page

if len(sys.argv) > 1:
    style = sys.argv[1]
else:
    style = "original"

page = page("../../wawrzek", style=style)
page.write("/tmp/ports.html")
page.write_style(style, "/tmp")
