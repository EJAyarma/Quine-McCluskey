from digital_funcion import DFGenerator
from expression_builder import ExpressionBuilder

my_func = DFGenerator(4, (0,1,2,3,5,7,8,9,11,14))

expression = ExpressionBuilder(my_func)
print(expression.EPIs)
print(expression.parse_essential_PI())
print(expression.build_bool_expr())
