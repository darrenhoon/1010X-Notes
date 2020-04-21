##DYNAMIC PROGRAMMING NOTES##
## Very useful to turn exponential time complexity code into polylinear time##
## compilation of qns worth examining over. for my own revision ##


## METHOD 1: MEMOIZATION##
## Idea is to keep keys with calculated values inside a dictionary so that the
## algo does not have to re-calculate a value that has already been calcuated before

'''situation where we need to find the total no. of unique paths from point A to point B'''
table = {}  # table to memoize computed values

def memoize(f,*args):
    if args in table:
        return table[args]
    else:
        result = f(*args)
        table[args] = result
        return result
    
def num_of_paths(n, m):
    
    def function(x,y):
        if (x,y) in table:
            return table[(x,y)]
        
        elif x==0 or y == 0:
            return 1
        else:
            return memoize(function,x,y-1) + memoize(function,x-1,y)
        
    return memoize(function,n-1,m-1)

num_of_paths(3, 3) ##should return 6
print(table)




'''Interesting variation to the question where the person now needs to navigate across a field with areas to avoid'''
maze1 = ((1, 1, 1, 1, 1, 1, 1, 1, 0, 1),
         (1, 0, 0, 1, 1, 1, 0, 0, 1, 1),
         (0, 1, 1, 1, 0, 0, 1, 1, 1, 0),
         (1, 1, 0, 1, 1, 1, 1, 0, 1, 1),
         (0, 1, 0, 1, 0, 0, 1, 0, 1, 0),
         (1, 0, 1, 1, 1, 1, 0, 1, 1, 1),
         (1, 1, 0, 1, 0, 1, 0, 0, 1, 1),
         (0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
         (1, 0, 1, 0, 0, 1, 1, 0, 1, 1),
         (1, 0, 1, 1, 1, 0, 1, 0, 1, 0),
         (1, 1, 0, 1, 0, 1, 0, 1, 1, 1))


maze2 = ((1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1))

maze3 = ((1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 0),
         (1, 0, 0, 1))

table = {}
    
def num_of_paths(maze):

    n = len(maze) #rows
    m = len(maze[0]) #columns

    #first row
    for j in range(m):
        if maze[0][j]:
            table[(0,j)] =1
        else:
            for k in range(j,m):
                table[(0, k)] = 0
            break

    #first column
    for i in range(n):
        if maze[i][0]:
            table[(i,0)] =1
        else:
            for p in range(i,n):
                table[(p, 0)] = 0
            break

    for row in range(1, n):
        for col in range(1, m):
            if not maze[row][col]:
                table[(row, col)] = 0
            else:
                table[(row, col)] = table[(row-1,col)] + table[(row, col-1)]

    return table[(n-1, m-1)]

num_of_paths(maze1) #should be 2
num_of_paths(maze2) #should be 3003
print(table)

''' Pascal's Triangle using a list to keep track of values and theory to reduce complexity as opposed to recursion
recursive version:
def pascal(row, col):
    if col == 1 or col == row:
        return 1
    else:
        return pascal(row - 1, col) + pascal(row - 1, col - 1)
'''
def faster_pascal(row, col):
    first_line = [1,]*(col)
    table = []
    for i in range(row):
        table.append(first_line.copy())
    for j in range(1, col):
        table[0][j] = 0
    for k in range(1, row):
        for l in range(1, col):
            table[k][l] = table[k-1][l-1] + table[k-1][l]
    return table[row-1][col-1]


