from random import randint

l = []

for i in range(0, 100000000, 10):
    l.append(randint(0, 10) + i)

idx = randint(0, 10000000)
num = l[idx]


def binary_search(l, iskat, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if iskat == l[mid]:
            return mid
        elif iskat < l[mid]:
            return binary_search(l, iskat, start, mid -1)
        else:
            return binary_search(l, iskat, mid +1, stop)


iskat = num
start = 0
stop = len(l)
x = binary_search(l, iskat, start, stop)
if x == False:
    print('Item', iskat, 'not found!')
else:
    print('Item', iskat, 'found at index', x)
