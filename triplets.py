
elements = [12, 3, 1, 2, -6, 5, -8, 6] 
target  = 0

def check_pairs(elements, target = 0):
    
    """ 
            Check_pairs of the sum total (target)

            Par:
                Elements is a list of iterables.
                
                Target is the sum total of the three items in the iterables.

            Returns:
                    Three umbers whose sum equals to the target give.

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
