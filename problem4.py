a = [1, 2, 3, 4 ,5]
b = a

# Change the 4th index in b
b[4] = 7

print(id(a))
print(id(b))
print(a) # Remember we did not explicitly make changes to a.

"""
2278459070720
2278459070720
[1, 2, 3, 4, 7]
"""