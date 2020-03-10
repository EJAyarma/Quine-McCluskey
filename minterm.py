class Minterm():
    name = None
    value_bin = None
    value_bits = None
    def __init__(self, dec_num=None, num_var=None):
        self.combined = False
        self.value_dec = str(dec_num)
        if not dec_num is None:
            self.name = "m" + str(dec_num) + " "
            self.value_bin = bin(dec_num)[2:len(bin(dec_num))].zfill(num_var)
        if not self.value_bin is None:
            self.value_bits = [bit for bit in self.value_bin]
    
    def __repr__(self):
        return f"m{self.value_dec}({self.value_bin})"

    def __eq__(self, minterm_2):
        return self.value_bin == minterm_2.value_bin

    def __hash__(self):
        h = 0
        dec = self.value_dec.split(".")
        for i in dec:
            h += int(i)
        return h
