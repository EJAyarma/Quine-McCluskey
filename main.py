from minterm import Minterm
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

def combine_minterms(minterm_1, minterm_2):
    new_minterm = Minterm()
    new_minterm.name = (minterm_1.name + minterm_2.name).strip()
    new_minterm.value_bits = minterm_1.value_bits
    new_minterm.value_dec = minterm_1.value_dec + minterm_2.value_dec
    new_value_bits = ""
    for bit in minterm_1.value_bits:
        new_value_bits += bit
    new_minterm.value_bin = new_value_bits
    return new_minterm

a = Minterm(4, 4)
b = Minterm(5, 4)
ind = get_combination_index(a, b)
b.value_bits[ind] = a.value_bits[ind] = '_'
print(a, b)
c = combine_minterms(a, b)
print(a==b)

