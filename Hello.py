#!/usr/bin/env python

""""PyQt4 - Hello World"""

import sys
from PyQt4 import Qt

a = Qt.QApplication(sys.argv)


hello = Qt.QLabel("Hello, World")

hello.show()

a.exec_()