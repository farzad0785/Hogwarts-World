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
            if  left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    elif key == "potions":
        while i < len(left) and j < len(right):
            if left[i][1]["object"] < right[j][1]["object"]:
                result.append(left[i])
                i += 1
            elif left[i][1]["object"] > right[j][1]["object"]:
                result.append(right[j])
                j += 1
            else:
                if left[i][1]["object"].price <= right[j][1]["object"].price:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
    else:
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    result.extend(left[i:])
    result.extend((right[j:]))
    return result

def confirm_check():
    while True:
        try:
            confirm = int(input("1. Reconsider \n2. Seal thy pact \nThy decree: "))
            if confirm == 1:
                return True
            elif confirm == 2:
                return False
            else:
                print("Invalid. Enter command 1 or 2. ")
        except ValueError:
            print("Invalid. Enter command 1 or 2. ")