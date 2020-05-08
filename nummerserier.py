# + 1 
# 1 2 3 4 5
siffra = 1
print(siffra)

for x in range(10):
    siffra = siffra +1
    print(siffra)

# * 2 - 1
# 2 3 5 9
siffra = 2
print(siffra)

for x in range(10):
    siffra = siffra * 2 -1
    print(siffra)


# / 2
# 8192 4096 2048 1024
siffra = 8192
print(siffra)

for x in range(10):
    siffra = int(siffra / 2)
    print(siffra)


# x * x
# 1 4 9 16
siffra = 8192
print(siffra)

for x in range(1,10):
    siffra = x*x
    print(siffra)

# x * x
# 1 4 9 16
siffra = 8192
print(siffra)

for x in range(1,10):
    siffra = x*x
    print(siffra)

# 
# 1 1 2 3 5 8 
x = 1
y = 1
print(x)
print(y)

for z in range(1,10):
    temp = x + y
    x = y
    y = temp
    print(y)