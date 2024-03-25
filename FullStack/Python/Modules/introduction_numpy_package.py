import numpy as np

num_range = np.arange(16)

print(num_range)

# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])

print(num_range.reshape(4, 4))

# array([[ 0,  1,  2,  3],
#    [ 4,  5,  6,  7],
#    [ 8,  9, 10, 11],
#    [12, 13, 14, 15]])