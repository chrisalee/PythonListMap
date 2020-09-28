



# creating the list###################################################
# creating the list###################################################
# creating the list###################################################
class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class List(object):
    def __init__(self, head_node=None):
        self.head_node = head_node

    # this isn't strictly required, just allows the list to be printed
    def __str__(self):
        result = '['
        current_node = self.head_node
        is_first = True
        while current_node:
            if is_first:
                is_first = False
            else:
                result += ','
            result += str(current_node.value)
            current_node = current_node.next_node
        result += ']'
        return result

    def head(self):
        return self.head_node.value

    def tail(self):
        if self.is_empty():
            raise Exception('An empty list does not have a tail.')
        else:
            return List(self.head_node.next_node)

    # note that this is O(1)
    def prepend(self, value):
        new_head_node = Node(value, self.head_node)
        self.head_node = new_head_node

    # note that this is O(n)
    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head_node = new_node
        else:
            last_node = self.head_node

            while last_node.next_node:
                last_node = last_node.next_node

            last_node.next_node = new_node

    def is_empty(self):
        return self.head_node is None
# ########################################################
# ########################################################
# start of the mapping and the equation to solve

def polynomial(x):
    return 3 * x * x - 5 * x + 1


def map_list(the_function, the_list):
    if the_list.is_empty():
        return List()
    else:
        new_list = map_list(the_function, the_list.tail())
        new_list.prepend(the_function(the_list.head()))
        return new_list


some_numbers = List()
some_numbers.append(32)
some_numbers.append(57)
some_numbers.append(16)
some_numbers.append(8)
some_numbers.append(38)
print(map_list(polynomial, some_numbers))


# another way ##########################################################
def map(the_function, the_list):
    new_list = List()
    current_list = the_list
    while not current_list.is_empty():
        new_list.append(the_function(current_list.head()))
        current_list = current_list.tail()
    return new_list 