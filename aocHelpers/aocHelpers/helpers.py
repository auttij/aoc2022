def transpose(matrix):
	rows = len(matrix)
	column = len(matrix[0])
	result = [[0 for i in range(rows)] for j in range(column)]

	for r in range(rows):
		for c in range(column):
			#here we are grabbing the row data of matrix and putting it in the column on the result
			result[c][r] = matrix[r][c]
	return result