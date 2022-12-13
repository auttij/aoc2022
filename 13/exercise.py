import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from itertools import chain

def cmpList(a, b):
	if len(a) == 0 and len(b) > 0:
		return 1
	elif len(a) > 0 and len(b) == 0:
		return -1
	elif len(a) == len(b) == 0:
		return 0

	av, bv = a[0], b[0]
	# print(av, bv)
	if type(av) == type(bv) == int:
		if av < bv:
			# print(a, b, av, bv)
			return 1
		elif av > bv:
			return -1
		else:
			return cmpList(a[1:], b[1:])
	elif type(av) == type(bv) == list:
		v = cmpList(av, bv)
		if v in [-1, 1]:
			return v
		return cmpList(a[1:], b[1:])
	elif type(av) == list and type(bv) == int:
		v = cmpList(av, [bv])
		if v in [-1, 1]:
			return v
		return cmpList(a[1:], b[1:])
	
	elif type(av) == int and type(bv) == list:
		v = cmpList([av], bv)
		if v in [-1, 1]:
			return v
		return cmpList(a[1:], b[1:])
	# print('err')

@timer
@print_result
def exercise1(arr):
	correctPairs = []
	for i, pair in enumerate(arr):
		a, b = pair
		c = cmpList(a, b)
		# print('comparison', c)
		if c == 1:
			correctPairs.append(i + 1)
	# print(correctPairs)
	return sum(correctPairs)

from functools import cmp_to_key

@timer
@print_result
def exercise2(arr):
	decoders = [[[2]], [[6]]]
	input = list(chain(*arr))
	input.extend(decoders)
	s = sorted(input, key=cmp_to_key(cmpList), reverse=True)
	return (s.index(decoders[0]) + 1) * (s.index(decoders[1]) + 1)

def main(args=None):
	s = init(path.dirname(__file__), inputs.read_to_str, args)
	pairs = s.split('\n\n')
	arr = [[eval(i) for i in line.split()] for line in pairs]
	# print(arr)

	exercise1(arr.copy())
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
