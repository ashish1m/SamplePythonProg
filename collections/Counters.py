from collections import Counter

# counting number of elements occurrence in list
l = [1, 2, 2, 3, 3, 4, 8, 4, 5, 6, 7, 8, 8, 7, 8, 9, 8, 8]
print(Counter(l))

# counting number of letters's occurrence in a string
s = "Hello world"
print(Counter(s))

# counting number of word in a string
sentence = "This is python and I love python"
print(Counter(sentence.split()))
