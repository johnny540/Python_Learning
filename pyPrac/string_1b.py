# Remove spaces from string
"""rstrip() --> remove spaces at right side of string
lstrip() --> remove spaces at left side of string
strip() --> remove spaces at left & right sides of string"""

s = " Johnny How are you    "
s2 = " Hi Johnny"

print("Before removing spaces: ",len(s))
x = s.strip()
print("After removing spaces: ",len(x))