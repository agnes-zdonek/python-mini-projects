matrix = List[List[int]]

m1 : matrix = [[1,0],
               [0,1]]

m2 : matrix = [[1, 2],
               [3, 2]]

m3 : matrix = [[2, 3, 1],
               [1, 2, 3]]

def size(m : matrix)->Tuple[int,int]:
    """ """
    line : int = 0
    li : List[int]
    for li in m:
        line = line + 1

    column : int = len(m[0])
    
    return line, column

assert size(m1) == (2, 2)
assert size(m2) == (2, 2)
assert size(m3) == (2, 3)

def get_line(m : matrix, n : int)->List[int]:
    """n - number of a line, number of lines goes from 1"""
    return m[n-1]

assert get_line(m1, 1) == [1,0]
assert get_line(m3, 2) == [1, 2, 3]

def get_column(m : matrix, n : int)->List[int]:
    """n - number of a column, number of columns goes from 1"""
    res : List[int] = []
    l : List[int] 
    for l in m:
        i : int
        for i in range(len(l)):
            if i == (n-1):
                res.append(l[i])
    return res

assert get_column(m1, 2) == [0, 1]
assert get_column(m2, 1) == [1, 3]
assert get_column(m3, 3) == [1, 3]

def line_x_column(l : List[int], c : List[int])->int:
    """multiplies given line with a given column"""
    res : int = 0
    i : int
    for i in range(len(l)):
        res = res + l[i]*c[i]
    return res

ligne1 : List[int] = [0,1]
ligne2 : List[int] = [2,3]
ligne3 : List[int] = [4,1]
assert line_x_column(ligne1, ligne2) == 3
assert line_x_column(ligne2, ligne3) == 11

def multiply(m1 : matrix, m2 : matrix)->matrix:
    """ """
    res : matrix = []
    
    line_size,_ = size(m1)
    _,column_size = size(m2)
    i : int

    current_line : List[int] = []
    
    for i in range(1, line_size+1):
        line : List[int] = get_line(m1, i)
        j : int
        for j in range(1, column_size+1):
            column : List[int] = get_column(m2,j)
            current_line.append(line_x_column(line, column))
        res.append(current_line)
        current_line = []

    return res
        
    
assert multiply(m2, m1) == m2
assert multiply(m2, m3) == [[4,7,7], [8,13,9]]

def multiplication(m1 : matrix, m2 : matrix)->matrix:
    """ """
    l1, c1 = size(m1)
    l2, c2 = size(m2)
    if c1!=l2:
        return [[]] #if we cannot multiply return an empty matrix
    else:
        return multiply(m1,m2)


m4 : matrix = [[1,2], [3,4], [5,6], [7,8]]
assert multiplication(m1,m4) == [[]]


def transpose(m : matrix)->matrix:
    """ """
    _, column = size(m)
    res : matrix = []

    i : int
    for i in range(1, column+1):
        new_line : List[int] = get_column(m, i)
        res.append(new_line)

    return res


assert transpose(m1) == m1
assert transpose(m2) == [[1,3],
                         [2,2]]
assert transpose(m3) == [[2,1],
                         [3,2],
                         [1,3]]
assert transpose(m4) == [[1,3,5,7],
                         [2,4,6,8]]
        
