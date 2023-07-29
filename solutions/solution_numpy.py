# solutions.py

import numpy as np


def create_arrays():

    arr1 = np.random.normal(0, 1, (5,5))

    arr2 = np.ones((3,3,3))

    arr3 = np.array([[1,2,3], [4,5,6], [7,8,9]])

    return arr1, arr2, arr3


def array_operations(arr):

    det = np.linalg.det(arr)

    inv = np.linalg.inv(arr)

    pow = arr**3

    return det, inv, pow


def indexing_slicing(arr):

    subarr = arr[:5,:5]

    cols = arr[:, ::2]

    diag = np.trace(arr)

    return subarr, cols, diag


def arithmetic_operations(arr1, arr2):

    sine = np.sin(arr1)

    matmul = arr1 @ arr2

    dot = np.dot(arr1.ravel(), arr2.ravel())

    return sine, matmul, dot


def aggregate_functions(arr):

    mean = np.mean(arr)

    unique = np.unique(arr)

    sorted = np.sort(arr)

    return mean, unique, sorted


def reorganize_arrays(arr1, arr2):

    vert_stack = np.vstack([arr1, arr2])

    hori_stack = np.hstack([arr1, arr2])

    flattened = arr2.ravel()

    return vert_stack, hori_stack, flattened

