# //comprehension is process of making the code shorter and easily understandble

names = ['ram', 'hari', 'bikram', 'markib', 'shiva']
l = []
for person in names:
    l.append(person)
print(l)


# this one line is same as to the upper appende line
print([person for person in names])

l = []
for person in names:
    l.append(person+" taught me")
print(l)

ratings = {
    "interstaller": 9,
    "dark knight": 5,
    "bikram": 9,
    "marvel heros": 8,

}

l = []
for movies in ratings:
    if ratings[movies] > 6:
        l.append(movies)

        print(l)

print([movies for movies in ratings if ratings[movies] > 6])
