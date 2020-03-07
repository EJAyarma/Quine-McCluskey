from minterm import Minterm
from linked_list import LinkedList
def get_combination_index(minterm_1, minterm_2):
    uneq_index = None
    uneq_count = 0
    for i in range(len(minterm_1.value_bits)):
        if minterm_1.value_bits[i] != minterm_2.value_bits[i]:
            uneq_index = i
            uneq_count += 1
    if uneq_count == 1:
        return uneq_index
    else:
        return -1

def combine_minterms(minterm_1, minterm_2, common_index):
    new_minterm = Minterm()
    new_minterm.name = (minterm_1.name + minterm_2.name).strip()
    new_minterm.value_bits = minterm_1.value_bits
    new_minterm.value_bits[common_index] = "_"
    new_minterm.value_dec = '.'.join([minterm_1.value_dec, minterm_2.value_dec])
    new_value_bits = ""
    for bit in new_minterm.value_bits:
        new_value_bits += bit
    new_minterm.value_bin = new_value_bits
    return new_minterm

my_list = LinkedList()

my_list.add([7, 8, 9])
my_list.add([4, 5, 6])
my_list.add([1, 2, 3])
my_list.print_list()
her_list = LinkedList()
cur_group = my_list.root
while(not cur_group.next_node is None):
    next_group = cur_group.next_node
    for elem in cur_group.data:
        temp = []
        for i in range(len(next_group.data)):
            temp.append(elem+next_group.data[i])
    her_list.add(temp)
    cur_group = cur_group.next_node

her_list.print_list()
