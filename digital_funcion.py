
class DigitalFunction():

    def __init__(self, num_var, minterms_decimal, name=None):
        self.name = name
        self.num_var = num_var
        self.minterms_decimal = minterms_decimal
        self.variables = tuple([chr(i) for i in range(65, 65+num_var)])


    def __repr__(self):
        return f"<DigitalFuction{self.minterms_decimal}, {self.num_var} vars>"

    def __str__(self):
        ind_vars = ', '.join(self.variables)
        if not self.name is None:
            return f"{self.name}({ind_vars})"
        else:
            return f"DigitalFuction({ind_vars})"