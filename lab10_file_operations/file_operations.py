"""
Fredy Perez Vicente
Oct 15, 2025
lab 9 file operation test (functions)
"""


def write_file(filename, msg):
    with open(filename, "w") as file:
        file.write(msg)


def read_file(filename):
    with open(filename, "r") as file:
        file.readlines()


def append_file(filename):
    with open(filename, "a") as file:
        file.write("\nNew line added.")


# function from exercise lab 7 (yesterday)

"""
create the function
"""
