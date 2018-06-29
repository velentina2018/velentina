import re
p = re.compile(r'\W+')
result=p.split("This is my first split example string")
print(result)
DOB = "25-01-1991 # This is Date of Birth"
# Delete Python-style comments
Birth = re.sub (r'#.*$', "", DOB)
print ("Date of Birth : ", Birth)
# Remove anything other than digits
Birth1 = re.sub (r'\D', "", Birth)
print ("Before substituting DOB : ", Birth1)
# Substituting the '-' with '.(dot)'
New=re.sub (r'\W',".",Birth)
print ("After substituting DOB: ", New)