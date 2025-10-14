"""
Fredy Perez Vicente
Lab 7, accessing data in a file
Oct 14, 2025
"""

from lab7_function import *

testing()
print("\n---- Example 1: Reading file ----")
read_data("phrases.txt")

print("\n---- Example 2: Reading specific portion of a file ----")
read_up("phrases.txt")

print("\n---- Example 3: Read line ----")
read_readline("phrases.txt")

print("\n---- Example 4: Read lines ----")
read_all("phrases.txt")

print("\n---- Example 5: Loop through each line ----")
read_each("phrases.txt")

print("\n---- Example 6: Creating a new file ----")
new_file("perez.txt")

print("\n---- Example 7: Append data into an existing file ----")
stamp_date("perez.txt")

print("\n---- LAB EXERCISE ----")
count_yahoo = email_read("user_email.txt","@yahoo")
count_gmail = email_read("user_email.txt","@gmail")
count_hotmail = email_read("user_email.txt","@hotmail")

