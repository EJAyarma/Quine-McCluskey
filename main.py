def get_minterms_binary(num_literals, minterm_dec):
        minterms_binary = []
        for i in minterm_dec:
            zero_deciciency = (num_literals-len(bin(i)[2:len(bin(i))]))
            binary_number = bin(i)[2:len(bin(i))]
            minterms_binary.append("0"*zero_deciciency + binary_number)
        return minterms_binary;

num_literals = 4;
minterms_decimal = (0, 1, 3, 7, 8, 9, 11, 15)
a = get_minterms_binary(num_literals, minterms_decimal)
c = [[bit for bit in num] for num in a]
print(c)
b = [2, 2, 3, "d"]
b[3] = 8
print(b)