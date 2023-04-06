tu_a=(1,2,3,'문자열')
print(tu_a)
print(tu_a[0])
print(tu_a[1])

# TypeError: 'tuple' object does not support item assignment
# tu_a[0] = 10

tu_b = 1,2,3,4,5
print(tu_b)


cpy_tu = tu_b
# id() 메모리에서 위치값을 반환함
print(id(cpy_tu))
print(id(tu_b))
tu_b = tu_b + (100,)
print(tu_b)
print()
print(id(tu_b))
print(id(cpy_tu))
print(type(tu_b))