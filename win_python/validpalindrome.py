str = "A man, a plan, a canal: Panama"
alnumstr = ""

for char in str:
    if char.isalnum():
        alnumstr += char.lower()

reversed_str = ""
index = len(alnumstr)
while index > 0:
    reversed_str = reversed_str + alnumstr[index - 1]
    index = index -  1

if reversed_str == alnumstr:
    print("True")
else:
    print("False")

