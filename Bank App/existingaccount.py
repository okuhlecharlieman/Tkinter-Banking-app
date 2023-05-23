file = "bankdata.txt"
delimeter = '='

file= open(file, "r")

def check(fullString):
    fullString = fullString.strip('\n')
    value = fullString[fullString.index(delimeter)+1:]
    value = value.replace(" ","")
    return value

for line in file:
    if line.startswith('AccountNumber'):
        AccountNumber = check(file)
        if line.startswith('Password'):
            Password = check(file)

print("-" + AccountNumber + "-")
print("-" + Password + "-")