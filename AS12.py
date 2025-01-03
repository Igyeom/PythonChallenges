file = "file.py"

with open(file, "r") as f:
    content = f.read().splitlines()

conversion_key = {"for": "FOR", "=": "TO", "if": "IF", "==": "EQUALS", "while": "WHILE", "until": "UNTIL", "import": "IMPORT", "class": "DEFINE CLASS", "def": "DEFINE FUNCTION", "else:": "ELSE:", "elif": "ELSEIF", "except:": "EXCEPT:", "try:": "TRY:", "pass": "PASS", "in": "IN", "return ": "RETURN "}

for line in range(len(content)):
    for i, j in conversion_key.items():
        content[line] = content[line].replace(i, j)

with open("pseudocode.txt", "w") as f:
    f.write("\n".join(content))

# doesnt work very well, replaces some keywords that are supposed to stay
# some examples of this:
# int --> INt
# print --> prINt
