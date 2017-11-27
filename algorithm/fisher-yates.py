from random import randrange


def shuffle(items):
    i = items.__len__()
    while i > 1:
        j = randrange(i)
        i -= 1
        items[j], items[i] = items[i], items[j]


def shuffle_sattolo(items):
    """
 Sattolo's algorithm
 the random number j is chosen from the range between 1 and i−1 (rather than between 1 and i) inclusive
    :rtype: object
    """
    k = items.__len__()
    while k > 1:
        k -= 1
        f = randrange(k)
        items[k], items[f] = items[f], items[k]


items = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
shuffle(items)
print('fisher-yates: '+str(items))

arr = []
for i in items:
    arr.append(i.lower())
shuffle_sattolo(arr)
print('sattolo: '+str(arr))
