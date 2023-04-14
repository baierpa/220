# read the text from file
file = open('alice.txt', 'r')
text = file.read()
# make everything lowercase
lower_text = text.lower()
# remove punctuation
for ch in '~!@#$%^&*()_+{}|:"<>?`-=[]\\;\',./':
    lower_text = lower_text.replace(ch, ' ')
# split text into words
words = lower_text.split()
# count the words -> use a dictionary!
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
# sort the counts
count_list = list(count.items())
print(count_list)
def count_sort(tup):
    return tup[1]

count_list.sort(key=count_sort)
count_list.reverse()
print(count_list)
# print top 5
