def capitalize_words(sentence):
    words = sentence.split(' ')
    # Bug fixed: modify the words list in-place
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return ' '.join(words)

print(capitalize_words("hello world python"))
