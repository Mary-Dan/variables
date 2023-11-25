# 1
x = 6
y = 2
z = y
y = x
x = z
print(x,y)

# 2
x, y = y, x
print(x,y)

# 3
x = y + x
y = x - y
x = x - y
print(x,y)