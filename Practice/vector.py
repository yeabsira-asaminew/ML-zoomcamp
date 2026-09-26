import numpy as np

u = np.array([
    [1, 0, 3],
    [2, 3, 5],
    [1, 3, 0]
])

v = np.array([
    [1, 0],
    [3, 1],
    [1, 1]
])

def vector_multip(u, v):
    result = u.dot(v)
    
    return result

def dot_multiplication(u, v):
    assert u.shape[1] == v.shape[0]
    
    rows_u = u.shape[0] 
    rows_v = v.shape[0]
    columns_u = u.shape[1]
    columns_v = v.shape[1]
    
    result = np.zeros((rows_u, columns_v))
    
    for i in range(rows_u):
        for j in range(columns_v):
            for k in range(columns_u):
                
                result[i, j] = result[i, j] + u[i, k] * v[k, j]
                
    return result


if np.array_equal(dot_multiplication(u, v), vector_multip(u, v)):
    print("Equal")
else:
    print("Not Equal")
                
                