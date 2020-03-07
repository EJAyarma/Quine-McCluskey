from node import Node
from queue import Queue
from minterm import Minterm

class DFGenerator():
    minterms_grouped = dict()
    process_que = Queue()

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

    def populate_queue():
        for key, value in self.minterms_grouped.items():
            self.process_que.enqueue[value]

    def get_PIs(self):
        pass

    def get_EPIs():
        pass

    def work_solution():
        pass

    def get_minterms_binary(self, num_lits, minterm_dec):
        minterms_binary = []
        for i in minterm_dec:
            bin_num = bin(i)[2:len(bin(i))].zfill(num_lits)
            minterms_binary.append(bin_num)
        return minterms_binary

my_digit_func = DFGenerator(4, (0, 1, 3, 7, 8, 9, 11, 15))
my_digit_func.group_minterms()
my_digit_func.get_PIs()
print(my_digit_func.minterms_grouped)
print(my_digit_func)
print(my_digit_func.process_que)