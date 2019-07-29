
class Check_Pair():

    """Check_pair checks the smallest pair, one from list1 and one from list2"""
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
            for x in a:
                self.pair.append(a[:1])


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
            for x in b:
                self.pair.append(b[:1])



