def is_anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)


print(f"Is 'iceman' an anagram of 'cinema'? {is_anagram('iceman', 'cinema')}")
print(f"Is 'leaf' an anagram of 'tree'? {is_anagram('leaf', 'tree')}")
