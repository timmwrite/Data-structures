#challenge one


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


#challenge 2

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



#Challenge 3


class Check_Pair():

    """Check_pair checks the smallest pair, one from list1 and one from list2"""
    """The smallest differencee will be given by -1-135 which is equal to -136"""
    def __init__(self):
        self.list1 = [-1, 5, 10, 20, 28, 3]
        self.list2 = [26, 134, 135, 15, 17]
        self.pair = []


    def check_smallest_list1(self, list1):

        """ 
            Check_smallest_list1 checks the smallest item in list1.

            Par:
                List1 is a list of iterable items.

            Returns:
                    Appends the smallest item to a new list (Pair).

            Run Time: 
                    Linear Time — O(n)
                    
        
        """
        for i in range(len(self.list1)):
            a = self.list1.sort()
            self.pair.append(a[0])


    def check_smallest_list2(self, list2):

        """ 
            Check_smallest_list1 checks the smallest item in list2.

            Par:
                List2 is a list of iterable items.

            Returns:
                    Appends the smallest item to a new list (Pair).

            Run Time: 
                    Linear Time — O(n)

        
        """
        for i in range(len(self.list2)):
            b = self.list2.sort()
            self.pair.append(b[4])



             



