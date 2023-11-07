input_file = open("input.txt", "r")
output_file = open("output.txt", "w")


# Multiplication of two matrices
def matrix_multiply(first, second):
	if len(first[0]) != len(second):
		print("Error: the dimensional problem occurred")
		input_file.close()
		output_file.close()
		exit(1)
	result = []
	for i in range(len(first)):
		result.append([])
		for j in range(len(second[0])):
			result[i].append(0)
			for s in range(len(first[0])):
				result[i][j] += first[i][s] * second[s][j]
	return result


# Addition of two matrices
def matrix_addition(first, second):
	if len(first) != len(second) or len(first[0]) != len(second[0]):
		print("Error: the dimensional problem occurred")
		input_file.close()
		output_file.close()
		exit(1)
	result = []
	for i in range(len(first)):
		result.append([])
		for j in range(len(first[0])):
			result[i].append(first[i][j] + second[i][j])
	return result


# Subtraction one matrix from other
def matrix_subtraction(first, second):
	if len(first) != len(second) or len(first[0]) != len(second[0]):
		print("Error: the dimensional problem occurred")
		input_file.close()
		output_file.close()
		exit(1)
	result = []
	for i in range(len(first)):
		result.append([])
		for j in range(len(first[0])):
			result[i].append(first[i][j] - second[i][j])
	return result


# Multiplication matrix by scalar
def matrix_scalar_multiply(scalar, matrix):
	result = []
	for i in range(len(matrix)):
		result.append([])
		for j in range(len(matrix[0])):
			result[i].append(scalar * matrix[i][j])
	return result


# Transpose of matrix
def transpose(matrix):
	result = []
	for i in range(len(matrix[0])):
		result.append([])
		for j in range(len(matrix)):
			result[i].append(matrix[j][i])
	return result


# Matrix for elimination some element of matrix
def elimination_matrix(matrix, row, col):
	result = []
	for i in range(len(matrix)):
		result.append([])
		for j in range(len(matrix[0])):
			if i == row and j == col:
				result[i].append(-matrix[i][j]/matrix[j][j])
			elif i == j:
				result[i].append(1)
			else:
				result[i].append(0)
	return result


# Identity matrix
def identity(size):
	I = []
	for i in range(size):
		I.append([])
		for j in range(size):
			if j == i:
				I[i].append(1)
			else:
				I[i].append(0)
	return I


# Matrix for changing rows of matrix
def permutation_matrix(size, row1, row2):
	result = identity(size)
	result[row1], result[row2] = result[row2], result[row1]
	return result


# Getting inverse of matrix
def inverse(matrix):
	identity_matrix = identity(len(matrix))

	for i in range(len(matrix)):
		max_ii = matrix[i][i]
		max_row = i
		for j in range(i + 1, len(matrix)):
			if abs(matrix[j][i]) > abs(max_ii):
				max_ii = matrix[j][i]
				max_row = j
		if max_row != i:
			p = permutation_matrix(len(matrix), i, max_row)
			matrix = matrix_multiply(p, matrix)
			identity_matrix = matrix_multiply(p, identity_matrix)

		for j in range(i + 1, len(matrix)):
			if matrix[j][i] == 0:
				continue
			e = elimination_matrix(matrix, j, i)
			matrix = matrix_multiply(e, matrix)
			identity_matrix = matrix_multiply(e, identity_matrix)

	for i in range(len(matrix) - 1, 0, -1):
		if matrix[i][i] == 0:
			continue
		for j in range(i - 1, -1, -1):
			if matrix[j][i] == 0 or matrix[j][j] == 0:
				continue
			e = elimination_matrix(matrix, j, i)
			matrix = matrix_multiply(e, matrix)
			identity_matrix = matrix_multiply(e, identity_matrix)

	for i in range(len(matrix)):
		scale = 1.0 / matrix[i][i]
		matrix[i][i] = 1.0
		for j in range(len(matrix)):
			identity_matrix[i][j] = scale * identity_matrix[i][j]

	return identity_matrix


# Function that finds the least negative in c
def find_least_negative(matrix):
	result = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] < result:
				result = matrix[i][j]
	return abs(result)


# Diagonalizing of x
def diagonalize(matrix):
	result = []
	if len(matrix[0]) != 1:
		for i in range(len(matrix[0])):
			result.append([])
			for j in range(len(matrix[0])):
				if j == i:
					result[i].append(matrix[0][i])
				else:
					result[i].append(0)
	else:
		for i in range(len(matrix)):
			result.append([])
			for j in range(len(matrix)):
				if j == i:
					result[i].append(matrix[i][0])
				else:
					result[i].append(0)
	return result


# Interior point method
def ipm(c, A, eps, alpha, point):
	d = diagonalize(point)
	actual_z = matrix_multiply(point, c)[0][0]

	while True:
		A_new = matrix_multiply(A, d)
		c_new = matrix_multiply(d, c)
		# P = I - A_new^T * (A_new * A_new^T)^-1 * A_new
		P = matrix_subtraction(identity(num_of_xs), matrix_multiply(matrix_multiply(transpose(A_new),
		    inverse(matrix_multiply(A_new, transpose(A_new)))), A_new))
		c_p = matrix_multiply(P, c_new)
		v = find_least_negative(c_p)
		# If there is no negative values in c_p method is not applicable
		if v == 0:
			output_file.write("The method is not applicable!")
			input_file.close()
			output_file.close()
			exit(1)
		x_new = matrix_addition([[1] for _ in range(num_of_xs)], matrix_scalar_multiply(alpha / v, c_p))
		# Return to default coordinates
		point = matrix_multiply(d, x_new)
		d = diagonalize(point)
		# Repeat iterations until difference between solutions is less than given epsilon
		if (matrix_multiply(transpose(point), c)[0][0] - actual_z) < eps:
			return matrix_multiply(transpose(point), c)[0][0], point
		else:
			actual_z = matrix_multiply(transpose(point), c)[0][0]


# Initial point calculation
# X's used in c we equate to 0, slacks we use to make equations in A equal to values in b
def calculate_initial_point(c, A, b):
	ip = [0 for x in range(len(c))]
	num_of_ones = 0
	for i in range(len(c)):
		if c[i][0] != 0:
			ip[i] = 1.0
			num_of_ones += 1
	for i in range(len(b)):
		need = b[i]
		for j in range(len(c)):
			need -= A[i][j]*ip[j]
		ip[i+num_of_ones] = need
		# If any of x's is less than 0 in initial point then it is not applicable
		if need < 0:
			output_file.write("The method is not applicable!")
			input_file.close()
			output_file.close()
			exit(1)
	return [ip]


# Reading input as lines
input_list = input_file.read()
# Making float's from strings
input_list = [[float(number) for number in line.split(" ")] for line in input_list.split("\n")]

# Splitting data into separate elements
c = [[number] for number in input_list[0]]
num_of_xs = len(c)
A = input_list[1:-2]
b = input_list[-2]
eps = input_list[-1][0]

# Caluclating initial point
initial_point = calculate_initial_point(c, A, b)

# Calculating and outputting answer, when alpha is equal to 0.5
ans_alpha05 = ipm(c, A, eps, 0.25, initial_point)
output_file.write("Initial point:\n")
for i in range(num_of_xs):
	output_file.write(f"x{i+1}: {initial_point[0][i]}\n")
output_file.write("\nWith alpha = 0.5:\n")
output_file.write("Z: " + str(round(ans_alpha05[0], 6)) + "\n")
for i in range(num_of_xs):
	output_file.write(f"x{i+1}: {round(ans_alpha05[1][i][0], 6)}\n")

# Calculating and outputting answer, when alpha is equal to 0.9
ans_alpha09 = ipm(c, A, eps, 0.9, initial_point)
output_file.write("\nWith alpha = 0.9:\n")
output_file.write("Z: " + str(round(ans_alpha09[0], 6)) + "\n")
for i in range(num_of_xs):
	output_file.write(f"x{i+1}: {round(ans_alpha09[1][i][0], 6)}\n")

# Closing files
input_file.close()
output_file.close()
