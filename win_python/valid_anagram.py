def prepareDict(m: str):
    m_dict = {}
    for char in m:
        if char in m_dict.keys():
            m_dict[char] += 1
        else:
            m_dict[char] = 1
    return m_dict    

def isAnagram(s: str, t: str) -> bool:
    s_dict = prepareDict(s)
    t_dict = prepareDict(t)
    print(s_dict)
    print(t_dict)
    if len(s_dict) != len(t_dict):
        return False
    for key in s_dict:
        if key in t_dict.keys() and s_dict[key] == t_dict[key]:
            continue
        else:
            return False
    return True

print('isAnagram returns', isAnagram("anagram", "nagarambbb"))
print('isAnagram returns', isAnagram("car", "rat"))