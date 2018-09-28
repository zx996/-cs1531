strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
for i in range(len(strings)):
    sentence += strings[i] +' '
sentence = sentence[:-1]
print(sentence)
#print(' '.join(strings))
