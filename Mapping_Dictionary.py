dOfNames = {7 : 'sam', 8: 'john', 9: 'mathew', 10: 'riti', 11 : 'aadi', 12 : 'sachin'}
dOfNames = dict(map(lambda x: (x[0], x[1] + '_'), dOfNames.items()))
print('Modified Dictionary : ')
print(dOfNames)