from DiagonAlley import Shop

def merge_sort(lst, key):
    if len(lst) < 2:
        return lst[:]

    middle = len(lst)//2
    left = merge_sort(lst[:middle], key)
    right = merge_sort(lst[middle:], key)
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if Shop.items[key][left[i]]["price"] <= Shop.items[key][right[j]]["price"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend((right[j:]))
    return result