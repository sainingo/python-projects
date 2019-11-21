#program that returns a list that contains only the elements that are common
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

#correct format
for elements in a:
    if elements in b:
        c.append(elements)

print(c)

#incorrect
for elements in a and b:
    c.append(elements)

print(c)



