def rotate(matrix):
	j = 0
	leng = cur = len(matrix) -1 
	for j in range(len(matrix)//2):
		
		for i in range(cur):
			i += j
			temp = matrix[j][i] # save up # =[1][1]
			matrix[j][i] = matrix[leng - i][j] # up: get lfet # [1][1]= [2][1]
			matrix[(leng - i)][j] = matrix[leng - j][leng - i] # left: get down #[2][1] = [2][2]
			matrix[leng - j][leng - i] = matrix[i][leng - j] # down: get right [2][2] = [1][2]
			matrix[i][leng - j] = temp # down
			for x in matrix:
				print(x)
			print('--------')
		print('##########')
		cur = cur - 2

	return matrix 
matrix2 = [[1,2],[3,4]]
matrix3 = [[1,2,3],[4,5,6],[7,8,9]]
matrix4 = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14 ,15 ,16]]
matrix5 = [[1, 2, 3, 4, 5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
matrix6 = [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]
res = rotate(matrix6)
for x in res:
	print(x)

