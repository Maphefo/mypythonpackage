def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    out = items.copy() # in place protection on items
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]     # Swap!

    return out

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    len_i = len(items)
    if len_i == 1:
        return items

    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])

    return merge(i1, i2)

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    return items.sort()
