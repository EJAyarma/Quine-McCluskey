class DititalFunciton():
    num_literals  = int()
    literals = list()
    minterms_grouped = dict()
    minterms_decimal = tuple()
    minterms_binary = list()
    minterms_bits = list()

    def __init__(self, num_literals, minterms_decimal):
        self.num_literals = num_literals
        self.minterms_decimal = minterms_decimal;
        self.literals = [chr(i) for i in range(65, 65+num_literals)]
        self.minterms_binary = self.get_minterms_binary(self.num_literals, self.minterms_decimal)
        self.minterms_bits = [[bit for bit in num] for num in self.minterms_binary]

    def __repr__(self):
        print(f"DigitalFuction({self.literals})")

    def group_minterms(self):
        for i in range(len(self.literals)+1):
            group_key = "G"+str(i)
            group_list = [n for n in self.minterms_binary if n.count("1") == i]
            group_list_bits = [[bit for bit in num] for num in group_list]
            self.minterms_grouped[group_key] = group_list_bits


    def get_PIs(self):
        groups = self.minterms_grouped
        for i in range(len(groups)): # Loop through groups of known no. of ones
            for j in range(len(groups["G"+str(i)])): # loop throuh eles of  known no. ones
                uneq_positions = 0
                uneq_index = None
                for k in range(len(groups["G"+str(i)][j])): # Loop through binary digits
                    if groups["G"+str(i+1)][j]:
                        if groups["G"+str(i)][j][k] != groups["G"+str(i+1)][j][k]:
                            uneq_positions += 1
                            uneq_index = k
                if uneq_positions == 1:
                    groups["G"+str(i)][j][uneq_index] = "_"
                    groups["G"+str(i+1)][j][uneq_index] = "_"

    def get_EPIs():
        pass

    def work_solution():
        pass

    def get_minterms_binary(self, num_lits, minterm_dec):
        minterms_binary = []
        for i in minterm_dec:
            zero_deficiency = num_lits-len(bin(i)[2:len(bin(i))])
            binary_number = bin(i)[2:len(bin(i))]
            minterms_binary.append("0"*zero_deficiency + binary_number)
        return minterms_binary;

my_digit_func = DititalFunciton(4, (0, 1, 3, 7, 8, 9, 11, 15))
my_digit_func.group_minterms()
my_digit_func.get_PIs()
print(my_digit_func.minterms_grouped)