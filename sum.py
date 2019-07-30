elements = [3, 5, -4, 8, 11, 1, -1, 6]  
target  = 10

def check_pairs(elements, target = 10):

 """ 
            Check_pairs of the sum total (target)

            Par:
                Elements is a list of iterables.
                
                Target is the sum total of the two pairs in the iterables.

            Returns:
                    The two pairs whose sum equals to the target give.

            Run Time: 
                    Linear Time — O(n)
                    
        
        """

    check_index = {}
    for i in range(len(elements)):
        num = elements[i]
        pair = target - num
        if pair in check_index:
            return [pair, elements[i]]
        check_index[num] = i
    return 'No pairs found'
