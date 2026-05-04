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

#Exercise Level 2

#1 Checking for valid python variable name
def is_valid_variable(name):
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    print(bool(re.match(pattern, name)))

#Exercise Level 3

#1
sentence = '%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'
cleaned = re.sub(r'[^A-Za-z\s.!?]', '', text)
cleaned = re.sub(r'\s+', ' ', cleaned).strip()

words = re.findall(r'\b[A-Za-z]+\b', cleaned)

unique_words = set(words)
result = []

for word in unique_words:
    count = len(re.findall(rf'\b{word}\b', cleaned))
    result.append((count, word))

result.sort(reverse=True) # sort and return top 3
print(result[0:3])
