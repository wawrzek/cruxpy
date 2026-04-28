#!/usr/bin/env python3
"""
An example script to print a HTML page of repository ports to the stdout.

It takes one or none arguments. If the argument is passed it's become
the path to the directory where is the repository the page should be created.
Otherwise the path defaults to "../../wawrzek".

Because the script ignores git information of the ports, it can be run without
cruxpy dependencies.
"""

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from cruxpy.portspage import page

repo = sys.argv[1] if len(sys.argv) > 1 else "../../wawrzek"

p = page(repo, git_info=False)
p.read_repo()
print (p.generate_page())

