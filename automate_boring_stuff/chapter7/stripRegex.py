#! python 3
# stripRegex.py - using RegEx to create function similar to python's string strip method

def stripRegex(string: str, chars=""):
    import re

    if chars != "" and chars != " ":
        charRegex = re.compile(fr'^[{chars}]*|[{chars}]*$')
        clean_string = charRegex.sub("", string)
    else:
        wsRegex = re.compile(r'^\s*|\s*$')
        clean_string = wsRegex.sub("", string)
        
    return clean_string

input_string = input("Enter a string: ")
print(stripRegex(input_string))