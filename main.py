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

my_list.add([Minterm(0, 4)])
my_list.add([Minterm(1, 4), Minterm(8, 4)])
my_list.add([Minterm(3, 4), Minterm(9, 4)])
my_list.add([Minterm(7, 4), Minterm(11, 4)])
my_list.add([Minterm(15, 4)])
def do(llist):
    temp_llist = LinkedList()
    current_group = llist.root
    while((not current_group.next_node == None)):
        combined = 0
        next_group = current_group.next_node
        PI_IMAGE = []
        for minterm_1 in current_group.data:
            for minterm_2 in next_group.data:
                com_index = get_combination_index(minterm_1, minterm_2)
                if com_index != -1:
                    new_minterm = combine_minterms(minterm_1, minterm_2, com_index)
                    PI_IMAGE.append(new_minterm)
                    combined += 1
        temp_llist.add(PI_IMAGE)
        current_group = next_group
    return [temp_llist, combined]

my_list.print_list()
combined = 0
new_list = LinkedList()
while(True):
    new_list, combined = do(my_list)
    if combined == 0:
        break
    else:
        my_list = new_list

my_list.print_list()