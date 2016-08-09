import random

#rotList will left rotate a list by specified indices
def rotList(seq, n):
	return seq[n:]+seq[:n]

#defaultGame generates a default solvable sudoku configuration
def defaultGame():
	numerals = range(1,10)					#numerals are 1-9
	game = []
	for blocks in xrange(3):				#Each 3x3 block should have all numerals
		for rows in xrange(3):				#Each row should have all numerals
			numerals = rotList(numerals, 3) #Next 3 elements in next row of current block
			game.append(numerals)
		numerals = rotList(numerals, 1)		#Different elements in the next block
	return game

#randomizeRows will shuffle the order of rows in a 9x9 matrix
#shuffling will happen for rows in 3 sub-blocks of 3-rows each
def randomizeRows(matrix):
	for blocks in xrange(3):
		begRow = blocks * 3
		endRow = begRow + 3
		matrix[begRow:endRow] = random.sample(matrix[begRow:endRow], 3)
	return matrix

#randomizeCols will shuffle the order of columns in a 9x9 matrix
#shuffling will happen for rows in 3 sub-blocks of 3-columns each
#output will be a transposed matrix with shuffled columns
def randomizeCols(matrix):
	newMatrix = map(list, zip(*matrix))
	return randomizeRows(newMatrix)

#maskedGame masks a solved game to convert it into a puzzle
def maskedGame(game, displayCells):
	newGame = []
	totalCells = 81.0
	for row in xrange(9):
		currentRow = []
		for col in xrange(9):
			threshold = displayCells / totalCells
			if random.random() < threshold:
				currentRow.append(game[row][col])
				displayCells -= 1
			else:
				currentRow.append(0)
			totalCells -= 1.0
		newGame.append(currentRow)
	return newGame

#create a new game matrix by transforming the default game
def sudoku():
	return randomizeCols(randomizeRows(defaultGame()))

if __name__ == "__main__":
	game = sudoku()
