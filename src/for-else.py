l = ['A', 'list', 'of', 'items', '.']
for word in l:
    if word == 'the':
        print('Found it!')
        break
else:
    print('Didn\'t find it')


l = ['A', 'list', 'of', 'the', 'other', 'items', '.']
for word in l:
    if word == 'the':
        print('Found it!')
        break
else:
    print('Didn\'t find it')
