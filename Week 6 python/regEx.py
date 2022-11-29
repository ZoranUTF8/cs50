import re

s = input("Do you agree?").lower()


if re.search("^y(es)?$", s):
    print("Agrred")
elif re.search("^no?$", s):
    print("Not agreed")
