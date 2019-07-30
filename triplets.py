
elements = [12, 3, 1, 2, -6, 5, -8, 6] 
target  = 0

def check_pairs(elements, target = 0):
    
     """ 
            Check_smallest_list1 checks the smallest item in list1.

            Par:
                List1 is a list of iterable items.

            Returns:
                    Appends the smallest item to a new list (Pair).

            Run Time: 
                    Linear Time — O(n)
                    
        
        """

    check_index = {}
    for i, x in range(len(elements)):
        num = elements(sum([i],[x]))
        triplets = target - num
        if triplets in check_index:
            return [triplets, elements[i],[x]]
        check_index[num] = i,x
    return 'No triplets found'
