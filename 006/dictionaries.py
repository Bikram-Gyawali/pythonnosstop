dictionary = {
    "price": 140,
    "type": "fruit"
}

contacts = {
    "hari": [' 9-88723567', 'hari123@gmail.com'],
    'syam': {'phone': '1233332434', 'email': 'syam2132@gmail.com'},
    'ram': 9228718112
}

print(dictionary['type'])

groc = {'banana': 10}
print(groc['banana'])

# or we canget like
print(dictionary.get('price'))

# print(contacts)

sentence = 'i like the way you look at me .i have the fay to hook at you to'

countWord = {
    'i': 2,
    "the": 2,
    "you": 2

}
print(list(countWord.items()))
print(list(countWord.keys()))
print(list(countWord.values()))

countWord.pop('i')  # it will delete i from the dictionary
print(list(countWord.keys()))
countWord['bikram'] = 3
print(countWord)
