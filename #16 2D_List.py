"""
1,2,3
4,5,6
7,8,9
"""
#we call this matrix and those are really important in data science and machine learning
#if you want to me a matrix like that you can use 2d list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
] 
print(matrix)

#we can access this matrix like this
matrix[0] [2] = 30
print(matrix[0])

#we also can iterate for loop over a matrix 
for row in matrix:
    for item in row:
        print(item)