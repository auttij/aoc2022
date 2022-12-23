def transpose(matrix):
	rows = len(matrix)
	column = len(matrix[0])
	result = [[0 for i in range(rows)] for j in range(column)]

	for r in range(rows):
		for c in range(column):
			#here we are grabbing the row data of matrix and putting it in the column on the result
			result[c][r] = matrix[r][c]
	return result

from collections import deque
def bfs(grid, start, end, cmp):
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
				and cmp(grid[x + dx][y + dy], grid[x][y])
			):
				q.append(((x + dx, y + dy), dist + 1))
	return float("inf")

def dfs(grid, start, end, cmp):
	stack = []
	stack.push(start)
	seen = set()
	while stack:
		pos = stack.pop(-1)
		if pos == end:
			return stack
		if pos in seen:
			continue
		seen.add(pos)
		x, y = pos
		for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
			if (
				0 <= x + dx < len(grid)
				and 0 <= y + dy < len(grid[0])
				and cmp(grid[x + dx][y + dy], grid[x][y])
			):
				stack.append((x + dx, y + dy))

def binarySearch(arr, target):
	lo, hi = 0, len(arr) - 1
	while lo <= hi:
		m = (lo + hi) // 2
		if arr[m] < target:
			lo = m + 1
		elif arr[m] > target:
			hi = m - 1
		else:
			return m
	return -1

def adjacent(pos):
    for axis in range(len(pos)):
        for d in (-1, 1):
            q = list(pos)
            q[axis] += d
            yield tuple(q)

from itertools import product
def neighborsGeneral(pos):
	dimensions = len(pos)
	combinations = product([-1, 0, 1], repeat=dimensions)
	for iter in combinations:
		if not any(iter):
			continue
		yield tuple(sum(i) for i in zip(iter, pos))

def neighbors2d(pos):
	for r in [-1, 0, 1]:
		for c in [-1, 0, 1]:
			if r != 0 or c != 0:
				yield (pos[0] + r, pos[1] + c)
