strings = ["flower","flow","floght", "floid"]

def longestCommonPrefix(strs: list[str]) -> str:
    common_prefix = ""
    for charindex, char in enumerate(strs[0]):
        letter_matched = True    
        for str in strs:
            if char == str[charindex]:
                continue
            else:
                letter_matched = False            
        if letter_matched == True:
            common_prefix = common_prefix + char
        else:
            break #This character did not match. Exit loop
    return common_prefix


prefix = longestCommonPrefix(strs = strings)
print("Prefix is", prefix)
    
