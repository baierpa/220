def word_sort(tup):
    return tup[1]

# read the text from the file
file = open('alice.txt', 'r')
text = file.read()
# make everything lowercase
text_lower = text.lower()
# remove all punctuation
for ch in '~!@#$%^&*()_+{}|:"<>?`-=[]\\;\',./':
    text_lower = text_lower.replace(ch, ' ')
# split into words
words = text_lower.split()
# count the words -> dictionary!
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
# sort
count_list = list(count.items())
count_list.sort(key=word_sort)
count_list.reverse()
print(count_list)
# print top 5

