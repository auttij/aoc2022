import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(arr):
	count = 0
	for a, b, c, d in arr:
		if a <= c and c <= b and a <= d and d <= b:
			count += 1
		elif c <= a and a <= d and c <= b and b <= d:
			count += 1
	return count

@timer
@print_result
def exercise2(arr):
	count = 0
	for a, b, c, d in arr:
		if (a <= c and c <= b) or (a <= d and d <= b):
			count += 1
		elif (c <= a and a <= d) or (c <= b and b <= d):
			count += 1
	return count

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_int_tuple_arr, args)
	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
