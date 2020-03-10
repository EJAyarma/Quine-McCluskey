from minterm import Minterm
from linked_list import LinkedList

class DFGenerator():
    minterms_grouped = dict()
    process_linked_list = LinkedList()

    def __init__(self, num_var, minterms_decimal):
        self.num_var = num_var
        self.minterms_decimal = minterms_decimal
        self.literals = [chr(i) for i in range(65, 65+num_var)]
        self.minterms = [Minterm(i, num_var) for i in minterms_decimal]

    def __repr__(self):
        return f"DigitalFuction({self.literals})"

    def group_minterms(self):
        for i in range(len(self.literals)+1):
            group_key = "G"+str(i)
            group_list = [n for n in self.minterms if n.value_bin.count("1") == i]
            self.minterms_grouped[group_key] = group_list

    def populate_queue(self):
        groups = list(self.minterms_grouped.values())
        for i in range(len(groups)-1, -1, -1):
            self.process_linked_list.add(groups[i])


    def get_combination_index(self, minterm_1, minterm_2):
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
    

    def combine_minterms(self, minterm_1, minterm_2, common_index):
        new_minterm = Minterm()
        new_minterm.name = (minterm_1.name + minterm_2.name).strip()
        new_minterm.value_bits = minterm_1.value_bits[:]
        new_minterm.value_bits[common_index] = "_"
        new_minterm.value_dec = '.'.join([minterm_1.value_dec, minterm_2.value_dec])
        new_value_bits = ""
        for bit in new_minterm.value_bits:
            new_value_bits += bit
        new_minterm.value_bin = new_value_bits
        return new_minterm
 
    def get_PIs(self, process_list=None):
        uncombined_minterms = []
        combinations = 0
        temp_process_llist = LinkedList()
        if not process_list is None:
            current_group = process_list.root
        else:
            current_group = self.process_linked_list.root
        while(not (current_group.next_node is None)):
            next_group = current_group.next_node
            PI_IMAGE = []
            for j in range(len(current_group.data)):
                PI_IMAGE.clear()
                minterm_1 = current_group.data[j]
                for i in range(len(next_group.data)):
                    minterm_2 = next_group.data[i]
                    com_index = self.get_combination_index(minterm_1, minterm_2)
                    if com_index != -1:
                        new_minterm = self.combine_minterms(minterm_1, minterm_2, com_index)
                        PI_IMAGE.append(new_minterm)
            temp_process_llist.add(PI_IMAGE)
            current_group = next_group
        return temp_process_llist


    def get_EPIs():
        pass

    def work_solution():
        pass

my_digit_func = DFGenerator(4, (0, 1, 3, 7, 8, 9, 11, 15))
my_digit_func.group_minterms()
my_digit_func.populate_queue()
my_digit_func.process_linked_list.print_list()
print(my_digit_func.process_linked_list.root.next_node)
generations = []
l1 = my_digit_func.get_PIs()
generations.append(l1)
l2 = my_digit_func.get_PIs(l1)
generations.append(l2)
l3 = my_digit_func.get_PIs(l2)
generations.append(l3)
l4 = my_digit_func.get_PIs(l3)
generations.append(l4)

for gen in generations:
    gen.print_list()
