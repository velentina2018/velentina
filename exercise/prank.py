import os
from string import digits
list_file = os.listdir("C:\pranks\prank")
os.chdir("C:\pranks\prank")
for file in list_file:
    old_name=file
    print (old_name)
    new_name=old_name.lstrip(digits)
    print(new_name)
    os.renames(old_name,new_name)