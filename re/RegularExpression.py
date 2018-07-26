import re


def multi_re_find(patterns, phrase):
    for pattern in patterns:
        print('Searching for the "{}" in phrase...'.format(pattern))
        print(re.findall(pattern, phrase))
        print('\n')


patt = ['sd*',
        'sd+',
        'sd?',
        'sd{2}',
        'sd{1,2}',
        '[^!.?, ]+']

text = "sssdddd dsdsdsdsd sdsdsdsd sssssddddd ssdddssddssddd sdsdsd sdsdsd sdsdsdsdssdddssdd sddddd sd sdddddddd"
# multi_re_find(patt, text)

s = "RegExr v3 was created by gskinner.com, and is proudly hosted by Media Temple. " \
    "Edit the Expression & Text to see matches. Roll over matches or the expression for details. " \
    "PCRE & Javascript flavors of RegEx are supported. The side bar includes a Cheatsheet, full Reference, and Help. " \
    "You can also Save & Share with the Community, and view patterns you create or favorite in My Patterns. " \
    "Explore results with the Tools below. Replace & List output custom results. Details lists capture groups. " \
    "Explain describes your expression in plain English."

print(re.findall("[^.!,? ]+", s))

