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
        if not common_index is None:
            new_minterm.value_bits[common_index] = "_"
        new_minterm.value_dec = '.'.join([str(minterm_1.value_dec), str(minterm_2.value_dec)])
        new_value_bits = ""
        for bit in new_minterm.value_bits:
            new_value_bits += bit
        new_minterm.value_bin = new_value_bits
        return new_minterm


    def derive_generations(self, que):
        temp_que = deque()
        current_group = que.popleft()
        while(len(que) > 0):
            next_group = que[0]
            combined_minterms = []
            for minterm_1 in current_group:
                for minterm_2 in next_group:
                    new_minterm = self.combine_minterms(minterm_1, minterm_2)
                    if not new_minterm is None:
                        combined_minterms.append(new_minterm)
            if len(combined_minterms) != 0:
                temp_que.append(list(set(combined_minterms)))
            current_group = que.popleft()
        return temp_que

    def get_generations(self):
        generations = []
        gen = self.derive_generations(self.process_queue)
        print(gen)
        while(len(gen) > 0):
            generations.append(gen.copy())
            gen = self.derive_generations(gen)
        return generations

    def get_EPIs():
        pass

    def work_solution():
        pass

my_func = DFGenerator(3, (0, 2, 3, 4, 5, 6, 7))
my_func.group_minterms()
my_func.populate_queue()
a = my_func.get_generations()
for i in a:
    print(i)