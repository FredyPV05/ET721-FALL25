"""
Fredy Perez Vicente
Lab 7, accessing data in a file (functions)
Sep 29, 2025
"""

def testing():
    print("Fredy Perez Vicente")

def read_data(filename):
    fileuser = open(filename, 'r')

    for each in fileuser:
        print(each)