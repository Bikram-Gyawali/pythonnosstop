list1 = [1, 2, 3, 4, 5]
list2 = ['ram', 'hari', 'cat', 'dog', 'bird']

zipped = list(zip(list1, list2))
print(zipped)
#  if any list has more values than other then the lst element or item is trunchteed cut off the list with less items are the result of the length to be output

unzipped = list(zip(*zipped))
print(unzipped)


# for (l1, l2) in zip(list1, list2):
#     print(l1)
#     print(l2)

items = ['apple', 'banana', 'melon', 'orange']
counts = [3, 4, 5, 9]
prices = [10, 20, 10, 30]
sentences = []
for (item, count, price) in zip(items, counts, prices):
    item, count, price = str(item), str(count), str(price)
    sentence = "i bought "+count+' ' + item+'s at'+price+' rupee each .'
    sentences.append(sentence)
print("=============")
print(sentences)
