# name = input("Hey what's your name: ")


# age = input("What's your age: ")
# occupation = input("What's your occupation: ")
#
# print("Hey {}, you are {} yrs old. And your occupation is {}".format(name, age, occupation))
# print("Hey %s, you are %s yrs old. And your occupation is %s" %(name, age, occupation))
# print(f"Hey {name}, you are {age} yrs old. And your occupation is {occupation}")

# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.casefold())
# print(name.swapcase())

# def longest_consec(strarr, k):
#     longest_str = ""
#     # your code
#     for i in range(len(strarr) - (k - 1)):
#         temp_str = ""
#         for j in range(i, i + k):
#             temp_str += strarr[j]
#         if len(temp_str) > len(longest_str):
#             longest_str = temp_str
#
#     return longest_str
#
#
# print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))

# def check_str(string):
#     count_o = 0
#     count_x = 0
#     for s in string:
#         if s == 'O' or s == 'o':
#             count_o += 1
#         elif s == 'X' or s == 'x':
#             count_x += 1
#
#     return count_o == count_x
#
# print(check_str("XxOooOO"))

def check_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


def anagrams(word, words):
    anagram = []
    for i in words:
        if check_anagram(i, word):
            anagram.append(i)
    return anagram


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(['aabb', 'bbaa'])
