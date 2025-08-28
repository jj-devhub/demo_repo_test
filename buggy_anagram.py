def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())  # Bug fixed: handle case sensitivity

print(is_anagram("Listen", "silent"))
