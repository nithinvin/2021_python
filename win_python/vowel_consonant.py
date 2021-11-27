alph = ""
while len(alph) != 1:
    alph = input("Enter a single alphabet: ")

if alph.lower() in ["a", "e", "i", "o", "u"]:
    print(alph, "is a vowel")
else:
    print(alph, "is a consonant")
