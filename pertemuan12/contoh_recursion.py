# versi rekursi
def faktorial(n):
    if n == 1:
        return 1
    return n * faktorial(n-1)

# versi iteratif
def faktorial_i(n):
    acc = 1
    for i in range(1,n+1):
        acc = acc * i
    return acc

#print("1000!: ", faktorial(1000))
print("1000!: ", faktorial_i(1000))