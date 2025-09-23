# 0 - 100
for i in range(101):
    print(i, end=', ')
print()
print()

# 1 - 100
for i in range(1, 101):
    print(i, end=', ')
print()
print()

# 1,3,5,..,99
for i in range(1,101,2):
    print(i, end=', ')
print()
print()

# 100,99,98,...,1
for i in range(100,0,-1):
    print(i, end=', ')
print()
print()

# 100,99,98,...,0
for i in range(100,-1,-1):
    print(i, end=', ')
print()
print()

# 100,98,96,94,...,0
for i in range(100,-1,-2):
    print(i, end=', ')
print()
print()

# 1,2,3,4,5
# 1,2,3,4,5
# 1,2,3,4,5
# 1,2,3,4,5
# 1,2,3,4,5
for i in range(1,6):
    for j in range(1,6):
        print(j, end=', ')
    print()
print()
print()

# 1
# 2, 2
# 3, 3, 3
# 4, 4, 4, 4
# 5, 5, 5, 5, 5
for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=', ')
    print()
print()
print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=', ')
    print()
print()
print()

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
for i in range(1,6):
    for j in range(1,6-i+1):
        print(j, end=', ')
    print()
print()
print()