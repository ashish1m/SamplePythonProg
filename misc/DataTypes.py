# === Immutable ===
# Numbers --> Integer, Float & Complex(3 + 2j)
# Strings --> 'David' or "David"
# --> Concatenation
# --> Repetition
# --> Slicing
# --> Indexing
# Tuples --> (1, "a", 3)

# === Mutable ===
# List --> [1, 'b', 3]
# Dictionaries --> {1: 'a', 'b': 3, 3 : "David"}
# Sets --> {2, 4, 5, 6, 7}


def censor(text, word):
    star = "*" * len(word)
    text = text.replace(word, star)
    return text

l = [3, 6, 4, 2]
l.sort()
print(l)