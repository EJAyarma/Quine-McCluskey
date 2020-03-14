class ExpressionBuilder():
    def __init__(self, function_builder):
        self.EPIs = function_builder.get_essential_PIs()
        self.variables = function_builder.variables

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
        return sorted(products)
    

    def build_bool_expr(self):
        products = self.parse_essential_PI()
        boolean_expression = ""
        for product in products:
            boolean_expression += product + " + "
        boolean_expression = boolean_expression.rstrip(" + ")
        return boolean_expression
