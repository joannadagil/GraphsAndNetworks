def find_triangles(v, e):
    '''
    v - number of vertexes, from 0 to v-1
    e - adjacency matrix
    returns a list of triangles in the graph
    multiple edges are counted as multiple triangles
    '''
    triangles = []
    for a in range(v):
        for b in range(a+1, v):
            for c in range(b+1, v):
                n = e[a][b] * e[b][c] * e[c][a]
                #if n > 0: print("(", a," ", b , " ", c, ") = ", n)
                for _ in range(n): triangles.append((a,b,c))
                #print(triangles)
    return triangles


## Usage

v = 5
e = [[0 for _ in range(v)] for _ in range(v)]

e[0][1] += 1; e[1][0] += 1
e[0][3] += 1; e[3][0] += 1
e[1][3] += 1; e[3][1] += 1
e[1][2] += 1; e[2][1] += 1
e[2][3] += 1; e[3][2] += 1
e[0][2] += 1; e[2][0] += 1
e[3][4] += 1; e[4][3] += 1

#        1
#      / | \
#     /  |  \
#    0-------2
#     \  |  /
#      \ | /
#        3---4


print(len(find_triangles(v, e)))

# multiple edges
e[0][2] += 1; e[2][0] += 1

#        1
#      / | \
#     /  |  \
#    0=======2
#     \  |  /
#      \ | /
#        3---4

print(len(find_triangles(v, e)))
