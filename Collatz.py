
# NOTE the storage_dict class and the decorator dec_header
# aren/t used in the actual functions anywhare and don't change
# the result either 

# class storage_dict:
#     def __init__(self):
#         self.storage = {}

#     def add(self, key, val):
#         self.storage[key] = val

#     def isin(self, obj):
#         if obj in self.storage:
#             return True
#         return False

# storage = storage_dict()

# def dec_header(storage=storage):
#     # ensures that we dont have
#     # the same number set to
#     # different nodes
#     def dec(cla):
#         def inner(num):
#             if not storage.isin(num):
#                 num_node = cla(num)
#                 storage.add(num_node.number, num_node)
#                 return num_node
#             else:
#                 return storage.storage[num]
#         return inner
#     return dec


# @dec_header()
class _node:
    """
    Just a node initialization for
    the linked list
    """
    def __init__(self, number: int) -> None:

        self.number = number
        self.next = None


class List:
    """
    Linked list that stores a list of
    integers
    """
    def __init__(self, num: int) -> None:
        self.first = _node(num)
        self.loe = [num] # loe -- list of elements

    def add_num(self, input: int) -> None:
        """
        the method adds a number to the List
        """
        node = self.first
        while node.next is not None:
            node = node.next 
        node.next = _node(input)
        self.loe = self._contains()

    def add_node(self, inp_node: _node) -> None:
        """
        Adds a node in the linked list
        """
        node = self.first
        while node.next is not None:
            node = node.next
        node.next = inp_node
        self.loe = self._contains()

    def isin(self, inp: int) -> bool:
        """
        Checks if the element is in the list
        """ 
        node = self.first
        while node.next is not None:
            if node.number == inp:
                return True
            node = node.next
        
        if node.number == inp:
            return True
        return False

    def _contains(self) -> list[int]: 
        '''
        returns a list of elements
        contained in the linked list
        '''
        ement_node = self.first
        output = []
        while ement_node.next is not None:
            output.append(ement_node.number)
            ement_node = ement_node.next
        output.append(ement_node.number)
        return output

    def __str__(self) -> str:
        '''
        prints the  linked list 
        where the values are separated
        with "->"
        '''
        str_out = ''
        node = self.first
        while node.next is not None:
            str_out += f'{node.number} -> '
            node = node.next        
        str_out += f'{node.number}'
        return str_out
        
class Collatz:
    """
    Class for the Collatz cojecture function
    where the initial parameters define the
    actual function of the form of
    f(x) = mx + b and cal just mapps the
    corresponding output to the input
    """

    def __init__(self, coeff: int, const: int):
        self.coeff = coeff
        self.const = const

    def cal(self, inp: int) -> int:
        """
        if inp odd, return the output
        of mx + b but if even, devide by 2
        """

        if inp % 2 == 1:
            return self.coeff * inp + self.const
        return int(inp / 2)

def pathbuilder(itr: int, f: Collatz) -> list[List]:
    '''
    Builds the path from the first number
    up untill presumable second last (before 1)
    and if one of these numbers starts with a number
    that is already present in some other sequence (path)
    it removes it from the list to avoid repetitions
    '''

    outlist = []
    for i in range(1, itr+1):
        if i != 1:
            compare_list = []
            for llist in outlist:
               compare_list += llist.loe
            compare_list = list(set(compare_list)) 

            if i not in compare_list:
                val = i
                L_i = List(i)
                outlist.append(L_i)
                while f.cal(val) not in L_i.loe:
                    L_i.add_num(f.cal(val))
                    val = f.cal(val)

        else:
            val = i
            L_1 = List(1)
            outlist.append(L_1)
            # the while loop ensures that
            # the calculation doesn't loop
            while f.cal(val) not in L_1.loe:
                L_1.add_num(f.cal(val))
                val = f.cal(val)

    big_comparison_list = []
    for ement in outlist:
        big_comparison_list += ement.loe

    for element in outlist:
        if big_comparison_list.count(element.first.number) > 1:
            outlist.remove(element)

    return outlist

def pathfinder_test(pathbuilder_output_list, itr) -> bool:
    '''
    Just tests that all the values up until
    the itr parameter are preset in at
    least one of the sequences (linked lists).
    '''
    outstring = ''
    for llist in pathbuilder_output_list:
        outstring += ' ' + llist.__str__()  
    for i in range(1, itr+1):
        if f' {i} ' not in outstring:
            return False
        return True
    
    
    
