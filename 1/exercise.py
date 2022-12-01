import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init

@timer
@print_result
def exercise1(arr):
	return max([sum(map(int, i.split())) for i in arr.split("\n\n")])

@timer
@print_result
def exercise2(arr):
	elves = sorted([sum(map(int, i.split())) for i in arr.split("\n\n")])
	return sum(elves[-3:])

def main(args=None):
	input = init(path.dirname(__file__), inputs.read_str, args)
	exercise1(input)
	exercise2(input)

if __name__ == "__main__":
	main(argv[1:])
