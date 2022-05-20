import os
import inspect
import sys


def run_main(main_function):
	
	required_attribute_number = len(inspect.signature(main_function).parameters)
	name = inspect.getmodule(main_function).__name__
		
	def wrapper(*args, **kwargs):
		if name == "__main__":
			if required_attribute_number > 0:
				parameters = {num: value for num, value in enumerate(sys.argv)}
				return_value = main_function(parameters)
				sys.exit(return_value)
			else:
				return_value = main_function()
				sys.exit(return_value)

	return wrapper()
