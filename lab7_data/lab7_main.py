"""
Fredy Perez Vicente
Lab 7, accessing data in a file
Sep 29, 2025
"""

import os
os.chdir(os.path.dirname(__file__))


from lab7_function import *

testing()
print("\n---- Example 1: Reading file ----")
read_data("phrases.txt")