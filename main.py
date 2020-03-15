from digital_funcion import DigitalFunction
from expression_builder import ExpressionBuilder
from function_worker import FunctionWorker

# Declaring a new Digital Function: 
# Function(number_of_variables, tuple_of_minterm_decimal_numbers, optional_name_of_function)
my_func = DigitalFunction(4, (0,1,2,3,5,7,8,9,11,14), 'Y')
# Warning: Using a wrong value for number_of_variables may result in Errors

# A funtion worker to do all operations
my_func_worker = FunctionWorker(my_func)
generations = my_func_worker.get_generations()

generations_combined = generations["combined"]
generations_uncombined = generations["uncombined"]

#Printing of results

print("Generations of combined minterms")
for gen in generations_combined:
    print(gen, end="\n")
print()
print("PIs derived from uncombined items")
print(generations_uncombined)

print("Prime Implicants")
print(my_func_worker.get_PIs(), end="\n")

print("Essential Prime Implicants")
print(my_func_worker.get_essential_PIs(), end="\n")

print("Expression for function")
expression = ExpressionBuilder(my_func_worker)

print(expression.parse_essential_PI(), end="\n")
print("Half expression")
print(expression.bool_expr(), end="\n")
print("Full expression")
print(expression.bool_expr_full())