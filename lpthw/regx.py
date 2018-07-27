import re
line = ("Cats are smarter than dogs")
print(re.split("d|h|m|s|ms","1d2h2ms6"))
print(re.split("[0-9]","1d2h2ms"))