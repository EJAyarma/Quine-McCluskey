class Minterm():
    def __init__(self, d=None, num_var=None):
        self.combined = False
        self.value_dec = d
        self.value_bin = bin(d)[2:len(bin(d))].zfill(num_var)
        self.value_bits = [bit for bit in self.value_bin]
    
    def __repr__(self):
        return f"m{self.value_dec}({self.value_bin})"