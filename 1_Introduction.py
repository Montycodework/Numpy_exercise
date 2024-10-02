# import numpy as np
# import time
# import sys

# SIZE = 1000000

# # arr1 = np.array([1,2,3,4])

# a = range(SIZE)
# print(sys.getsizeof(5)* len(a)) # Size of a list

# arr1 = np.arange(SIZE)
# print(arr1.size* arr1.itemsize) # size of a numpy array


# # -------------Time taken-------------

# l1 = range(SIZE)
# l2 = range(SIZE)

# arr1 = np.arange(SIZE)
# arr2 = np.arange(SIZE)

# start = time.time()
# result1 = [(x+y) for x,y in zip(l1,l2)]
# print(f"Python list took: {(time.time() - start)*1000}")

# start = time.time()
# result2 = arr1 + arr2
# print(f"Python list took: {(time.time() - start)*1000}")

# ---------------------------------------------------------------------------------

import numpy as np

print(np.__version__)

