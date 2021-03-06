from collections import deque

from minterm import Minterm


class FunctionWorker():
    """
    This class contains functions for all middle computations 
    The constructor takes a DigitalFunction Object
    """

    minterms_grouped = {}
    process_queue = deque()

    def __init__(self, digital_function):
        self.digital_function = digital_function
        self.num_var = digital_function.num_var
        self.variables = digital_function.variables
        self.minterms_decimal = digital_function.minterms_decimal
        self.minterms = [Minterm(num, self.num_var) for num in self.minterms_decimal]


    def populate_queue(self):
        """
        Add the groups of Minterms to a queue for other operations
        """
        groups = list(self.minterms_grouped.values())
        for group in groups:
            if len(group) != 0:
                self.process_queue.append(group)

    
    def group_minterms(self):
        """
        Group Minterms according to the number of 1s in their binary value
        """
        for i in range(len(self.variables)+1):
            group_key = "G"+str(i)
            group_list = [n for n in self.minterms if n.value_bin.count("1") == i]
            self.minterms_grouped[group_key] = group_list
        self.populate_queue()


    def get_combination_index(self, minterm_1, minterm_2):
        """
        Find the index where two Minterms differ only in one position
        """
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
        """
        Perform combination of Minterms
        """
        common_index = self.get_combination_index(minterm_1, minterm_2)
        if common_index == -1:
            return
        new_minterm = Minterm()
        new_minterm.name = (minterm_1.name + minterm_2.name).strip()
        new_minterm.value_bits = minterm_1.value_bits[:]
        new_minterm.value_bits[common_index] = "_"
        new_minterm.value_dec = '.'.join([minterm_1.value_dec, minterm_2.value_dec])
        new_value_bits = ""
        for bit in new_minterm.value_bits:
            new_value_bits += bit
        new_minterm.value_bin = new_value_bits
        return new_minterm


    def derive_generation(self, que):
        """
        Perform all possible combination of minterms
        returns a tuple of combined_minterms
        and uncombined_minterms
        """
        # Use queue to store groups of minterms that combine
        # and those that do not. The queue has lists as data elements

        combined_que = deque() 
        uncombined_que = deque() 
        current_group = que.popleft()
        while(len(que) > 0):
            next_group = que[0]
            combined_minterms = []
            # Get combined minterms
            for minterm_1 in current_group:
                for minterm_2 in next_group:
                    new_minterm = self.combine_minterms(minterm_1, minterm_2)
                    if not new_minterm is None:
                        combined_minterms.append(new_minterm)
                        minterm_1.combined = minterm_2.combined = True
            if len(combined_minterms) != 0:
                combined_que.append(list(set(combined_minterms)))
            # Get uncombined minterms before last group
            for minterm in current_group:
                if not minterm.combined:
                    uncombined_que.append(minterm)
            current_group = que.popleft()
            # Get uncombined minterms in last group
            if len(que) == 0:
                for minterm in current_group:
                    if not minterm.combined:
                        uncombined_que.append(minterm)
        return combined_que, uncombined_que


    def get_generations(self):
        """ Generate all stages of combinations 
        """
        self.group_minterms() 
        combined_generations = [] # Store generation of combined mineterms
        uncombined_generations = [] # Store generation of uncombined minterms
        combined_gen = self.process_queue
        uncombined_gen = deque()
        while(len(combined_gen) > 0):
            # Convert queue of lists into list of lists
            combined_generations.append(list(combined_gen.copy()))
            uncombined_generations.append(list(uncombined_gen))
            combined_gen, uncombined_gen = self.derive_generation(combined_gen)
        return {"combined":combined_generations, "uncombined":uncombined_generations}
    

    def get_PIs(self):
        """
        Group all PIs from both combined minterms
        and uncombined minterms in a list
        """
        PIs = []
        generations = self.get_generations()
        combined_gens = generations["combined"]
        uncombined_gens_PIs = generations["uncombined"]
        # The last generation is a list of lists containing PIs
        # derived from combined minterms
        combined_gens_PIs = combined_gens.pop()
        # PIs from generation of combined minterms
        while len(combined_gens_PIs) > 0:
            PIs.extend(combined_gens_PIs.pop())
        # PIs from generation of uncombined minterms
        while len(uncombined_gens_PIs) > 0:
            PIs.extend(uncombined_gens_PIs.pop())
        return PIs

    
    def get_essential_PIs(self):
        """
        Filter PIs to get EPIs
        """
        essential_PIs = []
        PIs = self.get_PIs()
        # Count occurrences of PIs in all minterms
        # As a guide, the decimal_value of a PI is a string that contains the decimal value of
        # each minterm that combined i.e. "1.3.4.2" 
        minterm_counters = {minterm.value_dec: 0 for minterm in self.minterms}
        for PI in PIs:
            for key in minterm_counters.keys():
                if PI.value_dec.__contains__(key):
                    minterm_counters[key] += 1
        # Essential PIs have single occurrences in only one minterm
        # PIs that have only 1 count of a particular minterm 
        # are considered as essential PIs
        for key in minterm_counters.keys():
            if minterm_counters[key] == 1:
                for PI in PIs:
                    if PI.value_dec.__contains__(key):
                        essential_PIs.append(PI)
        return list(set(essential_PIs))
