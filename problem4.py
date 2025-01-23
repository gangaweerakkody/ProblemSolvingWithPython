a = [x * 2 for x in range(10)]
b = (x * 2 for x in range(10))

print(a)
print(b)

"""
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
<generator object <genexpr> at 0x7f61f8808b50>
"""
