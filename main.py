from minterm import Minterm
from digital_funcion import DFGenerator
from queue import Queue
from collections import deque

def get_combination_index(minterm_1, minterm_2):
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

def combine_minterms(minterm_1, minterm_2):
    common_index = get_combination_index(minterm_1, minterm_2)
    if common_index == -1:
        return
    new_minterm = Minterm()
    new_minterm.name = (minterm_1.name + minterm_2.name).strip()
    new_minterm.value_bits = minterm_1.value_bits[:]
    if not common_index is None:
        new_minterm.value_bits[common_index] = "_"
    new_minterm.value_dec = '.'.join([minterm_1.value_dec, minterm_2.value_dec])
    new_value_bits = ""
    for bit in new_minterm.value_bits:
        new_value_bits += bit
    new_minterm.value_bin = new_value_bits
    return new_minterm

def do(que):
    pass

def gen_offspring(que):
    temp_que = deque()
    current_group = que.popleft()
    while(len(que) > 0):
        next_group = que[0]
        combined_minterms = []
        for minterm_1 in current_group:
            for minterm_2 in next_group:
                new_minterm = combine_minterms(minterm_1, minterm_2)
                if not new_minterm is None:
                    combined_minterms.append(new_minterm)
        if len(combined_minterms) != 0:
            temp_que.append(list(set(combined_minterms)))
        current_group = que.popleft()
    return temp_que

m1 = Minterm(4, 4)
print("Bin value:", m1.value_bin)
print("Bits value:", m1.value_bits)
print("Name:", m1.name)
print("Dec value:", m1.value_dec)