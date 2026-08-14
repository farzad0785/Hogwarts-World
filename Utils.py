from DiagonAlley import Shop
from Spells import Spell


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
    if key == "wands":
        while i < len(left) and j < len(right):
            if  left[i][0] >= right[j][0]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    elif key == "potions":
        while i < len(left) and j < len(right):
            if left[i][0] > right[j][0]:
                result.append(left[i])
                i += 1
            elif left[i][0] < right[j][0]:
                result.append(right[j])
                j += 1
            else:
                if left[i][0].price >= right[j][0].price:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
    else:
        while i < len(left) and j < len(right):
            if Spell.spells[key][left[i][0]]["amount"] <= Shop.items[key][right[j][0]]["amount"]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    result.extend(left[i:])
    result.extend((right[j:]))
    return result