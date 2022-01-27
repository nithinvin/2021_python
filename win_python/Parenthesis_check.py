def isValid(s: str) -> bool:    
    mystack = []
    for char in s:
        if char == "(" or char == "{" or char == "[":
            mystack.append(char)            
            continue
        if char == ")" or char == "}" or char == "]":
            last_char = mystack.pop((len(mystack) - 1))
            if char == ")" and last_char == "(":
                continue
            elif char == "]" and last_char == "[":
                continue
            elif char == "}" and last_char == "{":
                continue
            else:
                return False        
    return True


myparstring1 = "(){}[]"
myparstring2 = "(}{}[]"
myparstring3 = "{}()[]"
myparstring4 = "{[(){}]}"
myparstring5 = "{[(){]]}"

print("isValid returns", isValid(myparstring5))
         