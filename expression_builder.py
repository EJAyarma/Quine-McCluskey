from digital_funcion import DFGenerator

class ExpressionBuilder():
    def __init__(self, function_generator):
        self.EPIs = function_generator.get_essential_PIs()
        self.variables = function_generator.variables

    def parse_essential_PI(self):
        """
        Convert Essential PIs into product of variables"""

        products = []
        for EPI in self.EPIs:
            product = ""
            bits = EPI.value_bits
            for i in range (len(bits)):
                if bits[i] == "0":
                    product += (self.variables[i] + "'")
                elif bits[i] == "1":
                    product += self.variables[i]
            products.append(product)
        return products
    

    def build_bool_expr(self):
        products = self.parse_essential_PI()
        boolean_expression = ""
        for product in products:
            boolean_expression += product + " + "
        boolean_expression = boolean_expression.rstrip(" + ")
        return boolean_expression
    

my_func = DFGenerator(4, (0,1,2,3,5,7,8,9,11,14))
print(my_func)
expression = ExpressionBuilder(my_func)
print(expression.EPIs)
print(expression.parse_essential_PI())
print(expression.build_bool_expr())
