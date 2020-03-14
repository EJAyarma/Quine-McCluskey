from digital_funcion import DigitalFunction
from expression_builder import ExpressionBuilder
from function_worker import FunctionWorker

my_func = DigitalFunction(3, (0,2,3,4,5,6,7))
my_func_worker = FunctionWorker(my_func)
expression = ExpressionBuilder(my_func_worker)
print(my_func_worker.get_PIs())
print(expression.parse_essential_PI())
print(expression.build_bool_expr())
