#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.abspath('../cruxpy'))
sys.path.append(os.path.abspath('..'))
from portspage import page

page = page('../wawrzek')
print (page.content)


