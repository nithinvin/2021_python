def isIsomorphic(s: str, t: str) -> bool:
    chardict = {}
    index = 0
    slen = len(s)
    while index < slen:
        char = s[index]
        if char in chardict.keys():
            print(chardict[char], t[index])
            if chardict[char] != t[index]:
                return False
        else:
            if t[index] in chardict.values():
                return False
            chardict[char] = t[index]
        index += 1
    return True

sstr = "paper"
tstr = "title" # True
sstr1 = "egg"
tstr1 = "add" #True
sstr2 = "paper"
tstr2 = "tttle" #False
sstr3 = "foo"
tstr3 = "bar" #False
print("isIsomorphic returns", isIsomorphic(sstr2, tstr2))





