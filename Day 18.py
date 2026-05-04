# DAY 18: 30 Days of python programming
import re

#Exercise Level 1

#1 Counting frequency of words

text = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = re.findall(r'\b\w+\b', text.lower())

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)

#2
text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
points = list(map(int, re.findall(r'-?\d+', text)))
min_point = min(points)
max_point = max(points)

distance = max_point - min_point

print("Points:", points)
print("Distance between farthest particles:", distance)