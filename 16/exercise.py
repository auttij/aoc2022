import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from aocHelpers.helpers import dfs
from functools import lru_cache
from itertools import chain


def floydWarshall(targets, pressures, ind):
	dist = [[999999 for i in range(len(pressures))] for j in range(len(pressures))]
	for vertex in targets:
		targs = targets[vertex]
		for target in targs:
			dist[ind[vertex]][ind[target]] = 1
		dist[ind[vertex]][ind[vertex]] = 0
		for k in range(1, len(pressures)):
			for i in range(1, len(pressures)):		
				for j in range(1, len(pressures)):
					if dist[i][j] > dist[i][k] + dist[k][j]:
						dist[i][j] = dist[i][k] + dist[k][j]
	return dist
	
@timer
@print_result
def exercise(arr):
	targets = { a: c for a, b, c in arr } 
	pressures = { a: int(b) for a, b, c in arr }
	ind = { a: i for i, (a, b, c) in enumerate(arr)}
	dist = floydWarshall(targets, pressures, ind)
	
	start = list(targets.keys()).index('AA')
	targets = [c for a, b, c in arr]
	pressures = [int(b) for a, b, c in arr]

	def chooseOne(xl):
		for i in range(len(xl)):
			yield (xl[i], xl[:i] + xl[i+1:])

	def gen(cur, rest, time):
		for i, rr in chooseOne(rest):
			if dist[cur][i] < time:
				yield pressures[i] * (time - dist[cur][i] - 1) + dfs(i, rr, time - dist[cur][i] - 1)
					
	@lru_cache(maxsize=256000)
	def dfs(cur, rest, time):
		return max(gen(cur, rest, time), default=0)

	def gen2(cur, rest, time):
		for i, rr in chooseOne(rest):
			if dist[cur][i] < time:
				yield pressures[i] * (time - dist[cur][i] - 1) + dfs2(i, rr, time - dist[cur][i] - 1)

	@lru_cache(maxsize=256000)
	def dfs2(cur, rest, time):
		return max(gen2(cur, rest, time), default=dfs(start, rest, 26))

	l = tuple(filter(lambda x: pressures[x] > 0, map(lambda x: x[0], enumerate(pressures))))
	
	print('1', dfs(start, l, 30))
	print('2', dfs2(start, l, 26))


# @timer
# @print_result
# def exercise2(arr):
# 	pass

def main(args=None):
	input = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	arr = []
	for line in input:
		a = line.split()
		subArr = [a[1], a[4].split("=")[1][:-1]]
		subArr.append("".join(a[9:]).split(","))
		arr.append(subArr)
	# print(arr)
	exercise(arr.copy())
	# exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
