# list in python is like an array
l=[1,2,3,6,5]
mix=[1,2,'jello',True,3.5,[12,12,9,4]]
print(l)
print("=========")
print(mix)
print(mix[5 ])

l.append(9)
print(l)
l.insert(1,4)
print(l)
l.remove(1)
print(l)
l.sort()
print(l)

mix.reverse()
print(mix)

for items in mix:
    print(items)