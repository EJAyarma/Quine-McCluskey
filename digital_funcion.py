from minterm import Minterm
from collections import deque

class DFGenerator():
    minterms_grouped = dict()
    process_queue = deque()


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
        self.populate_queue()


    def populate_queue(self):
        groups = list(self.minterms_grouped.values())
        for group in groups:
            if len(group) != 0:
                self.process_queue.append(group)


    def get_combination_index(self, minterm_1, minterm_2):
        uneq_index = None
        uneq_count = 0
        for i in range(len(minterm_1.value_bits)):
            if minterm_1.value_bits[i] != minterm_2.value_bits[i]:
                uneq_index = i
                uneq_count += 1
        if uneq_count == 1:
            return uneq_index
        elif uneq_count == 0:
            return None
        else:
            return -1


    def combine_minterms(self, minterm_1, minterm_2):
        common_index = self.get_combination_index(minterm_1, minterm_2)
        if common_index == -1:
            return
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


    def derive_generations(self, que):
        """
        Perform all possible combination of minterms
        returns a tuple of deque(combined_minterms)
        and deque(uncombined_minterms)
        """
        # Use deque() to store groups of minterms that combine
        # and those that do not. deque() contains lists
        combined_que = deque() 
        uncombined_que = deque() 
        current_group = que.popleft()
        while(len(que) > 0):
            next_group = que[0]
            combined_minterms = []
            # Get combined minterms
            for minterm_1 in current_group:
                for minterm_2 in next_group:
                    new_minterm = self.combine_minterms(minterm_1, minterm_2)
                    if not new_minterm is None:
                        combined_minterms.append(new_minterm)
                        minterm_1.combined = minterm_2.combined = True
            if len(combined_minterms) != 0:
                combined_que.append(list(set(combined_minterms)))
            # Get uncombined minterms before last group
            for minterm in current_group:
                if not minterm.combined:
                    uncombined_que.append(minterm)
            current_group = que.popleft()
            # Get uncombined minterms in last group
            if len(que) == 0:
                for minterm in current_group:
                    if not minterm.combined:
                        uncombined_que.append(minterm)
        return combined_que, uncombined_que

    def get_generations(self):
        """ Generate all stages of combinations """
        self.group_minterms() # According to number of 1s
        # Use a lists to store
        combined = []
        uncombined = []
        gen_combined = self.process_queue
        gen_uncombined = deque()
        while(len(gen_combined) > 0):
            # Convert deque() of lists into list of lists
            combined.append(list(gen_combined.copy()).pop())
            uncombined.append(list(gen_uncombined))
            gen_combined, gen_uncombined = self.derive_generations(gen_combined)
        return combined, uncombined

    
    def get_PIs(self):
        PIs = []
        combined, uncombined = self.get_generations()
        # The last generation is a list containing PIs
        # derived from combined minterms
        PIs.extend(combined.pop())
        for minterms in uncombined:
            if len(minterms) > 0:
                PIs.extend(uncombined.pop())
        return PIs


    def get_essential_PIs():
        pass


    def work_solution():
        pass

<<<<<<< HEAD
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
=======
my_func = DFGenerator(4, (0,1,2,3,9,10, 4, 5, 6))

print(my_func.get_PIs())
>>>>>>> fix
