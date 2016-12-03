import string

stringIn = "string with punctuation!"
out = stringIn.translate(str.maketrans('', '', string.punctuation))
print(out)