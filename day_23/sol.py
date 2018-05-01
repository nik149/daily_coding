M = input('Enter M: ')
N = input('Enter N: ')

mat = []
for i in range(0, M):
    mat.append(map(int, raw_input('Enter M values: ').split(' ')))
    
# 0 => tile on moved => -1
# 1 => wall
start = map(int, raw_input('Start Coordinate: ').split(' '))
end = map(int, raw_input('End Coordinate: ').split(' '))

def movement(mat, curCoord, direction):
    if(curCoord[0] == end[0] and curCoord[1] == end[1]):
        return 0
    elif(curCoord[1] == N or curCoord[0] == M or curCoord[0] == -1 or curCoord[1] == -1):
        return 99999
    elif (mat[curCoord[0]][curCoord[1]] == -1 or mat[curCoord[0]][curCoord[1]] == 1):
        return 99999
    else:
        newMat = [[mat[x][y] for y in range(len(mat[0]))] for x in range(len(mat))]
        newMat[curCoord[0]][curCoord[1]] = -1
        if(direction == 'l'):
            curCoord = [curCoord[0], curCoord[1] + 1]
        if(direction == 'r'):
            curCoord = [curCoord[0], curCoord[1] - 1]
        if(direction == 'u'):
            curCoord = [curCoord[0] - 1, curCoord[1]]
        if(direction == 'd'):
            curCoord = [curCoord[0] + 1, curCoord[1]]

        return 1 + min(movement(newMat, curCoord, 'l'), movement(newMat, curCoord, 'r'), movement(newMat, curCoord, 'u'), movement(newMat, curCoord, 'd'))

print min(movement(mat, start, 'l'), movement(mat, start, 'r'), movement(mat, start, 'u'), movement(mat, start, 'd'))
