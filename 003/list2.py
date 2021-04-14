items=[0,1,2,3,4,5,6,7,8,9,10]
print(items[-2]) #gives second last value
print(len(items))
print(items[:3]) #gives the first 3 value [0,1,2] //this is basically the slicing in python
print(items[:]) # gives all values
print(items[0:-1])
print(items[5:])
print(items[0:10:2])
print("============")


print(items[0::2])  
print("============")

print(items[::-1]) #this reveress any array
print("============")

print(items[5:0:-1]) #reverse an array from the any point index of an array
print("============")
for i in range(len(items)):
    print(items[0:i])
    
print("============")


size=3
for i in range(len(items)):
    print(items[i:i+size])