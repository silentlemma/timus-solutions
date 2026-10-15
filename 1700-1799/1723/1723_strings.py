from collections import Counter

# every occurrence of a spell starts with an occurrence of its first
# letter, so a most frequent single letter is a strongest spell
print(Counter(input().strip()).most_common(1)[0][0])
