elements = [3, 5, -4, 8, 11, 1, -1, 6]  
target  = 10

def check_pairs(elements, target = 10):

    check_index = {}
    for i in range(len(elements)):
        num = elements[i]
        pair = target - num
        if pair in check_index:
            return [pair, elements[i]]
        check_index[num] = i
    return 'No pairs found'