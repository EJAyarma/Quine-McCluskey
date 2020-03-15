from digital_funcion import DigitalFunction
from expression_builder import ExpressionBuilder
from function_worker import FunctionWorker

my_func = DigitalFunction(4, (0,1,3,7,8,9,11,15), 'Y')
my_func_worker = FunctionWorker(my_func)
expression = ExpressionBuilder(my_func_worker)
print(my_func_worker.get_PIs())
print(expression.parse_essential_PI())
print(expression.bool_expr())
print(expression.bool_expr_full())
print([my_func])