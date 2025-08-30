#!/usr/bin/env python3
"""
Simple check check if script to create a page for ports repo works fine.
"""


from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from cruxpy.portspage import page

page = page(path="../../../wawrzek")
page.write()
