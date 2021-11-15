import re

# Pattern Strings
contactNameExp = "^([a-zA-z]+( (?=[a-zA-Z])|-(?=[a-zA-Z])){0,1})*$"

# Pattern Objects
contactNamePattern = re.compile(contactNameExp)
