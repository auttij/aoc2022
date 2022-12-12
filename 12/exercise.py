import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
from collections import deque

def parseGrid(arr):
	aList = []
	start = end = None
	for i, row in enumerate(arr):
		for j, v in enumerate(row):
			if v == "S":
				start = (i, j)
				aList.append((i, j))
				arr[i][j] = "a"
			elif v == "E":
				end = (i, j)
				arr[i][j] = "z"
			elif v == "a":
				aList.append((i, j))
	return arr, start, end, aList

def bfs(grid, start, end):
    q = deque()
    q.append((start, 0))
    seen = set()
    while q:
        pos, dist = q.popleft()
        if pos == end:
            return dist
        if pos in seen:
            continue
        seen.add(pos)
        x, y = pos
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if (
                0 <= x + dx < len(grid)
                and 0 <= y + dy < len(grid[0])
                and ord(grid[x + dx][y + dy]) - ord(grid[x][y]) <= 1
            ):
                q.append(((x + dx, y + dy), dist + 1))
    return float("inf")

@timer
@print_result
def exercise1(GRID, START, END, _):
	return bfs(GRID, START, END)

@timer
@print_result
def exercise2(GRID, _, END, A_LIST):
	out = [bfs(GRID, a, END) for a in A_LIST]
	return min(out)

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	input = list(map(list, arr.copy()))
	GRID, START, END, A_LIST = parseGrid(input)

	exercise1(GRID, START, END, A_LIST)
	exercise2(GRID, START, END, A_LIST)

if __name__ == "__main__":
	main(argv[1:])
