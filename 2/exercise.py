import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

mapping = { 'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3 }
def mapper(l):
	return mapping[l[0]], mapping[l[1]]

@timer
@print_result
def exercise1(arr):
	output = 0
	for a, b in map(mapper, arr):
		if b - 1 == a or (b == 1 and a == 3):
			output += 6
		if b == a:
			output += 3
		output += b

	return output

@timer
@print_result
def exercise2(arr):
	output = 0
	for a, b in map(mapper, arr):
		if b == 1:
			played = a - 1
			if played == 0:
				played = 3
			output += played
		if b == 2:
			output += a + 3
		if b == 3:
			played = a + 1
			if played == 4:
				played = 1
			output += played + 6
	return output

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_pair_arr, args)
	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
