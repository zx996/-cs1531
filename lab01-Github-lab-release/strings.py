strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
for i in range(len(strings)):
    sentence += strings[i] +' '
sentence.strip()
print(sentence)
print(' '.join(strings))
