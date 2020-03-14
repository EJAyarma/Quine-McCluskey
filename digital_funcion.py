from minterm import Minterm

class DigitalFunction():

    def __init__(self, num_var, minterms_decimal):
        self.num_var = num_var
        self.minterms_decimal = minterms_decimal
        self.variables = tuple([chr(i) for i in range(65, 65+num_var)])
        self.minterms = [Minterm(i, num_var) for i in minterms_decimal]


    def __repr__(self):
        return f"DigitalFuction{self.variables} "