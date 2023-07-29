# test_exercises.py

import numpy as np
import numpy_ex.exercises as ex

# Fixtures
arr = np.random.rand(10, 10)
arr1 = np.random.rand(3, 3)
arr2 = np.random.rand(3, 3)
arr3 = np.random.randn(10)
arr4 = np.random.rand(4, 3)
arr5 = np.random.rand(4, 3)


def test_create_arrays():

    arr1, arr2, arr3 = ex.create_arrays()

    assert arr1.shape == (5, 5)  
    assert np.isclose(arr1.mean(), 0, atol=0.5)
    assert np.isclose(arr1.std(), 1, atol=0.5)
    assert arr2.shape == (3, 3, 3)
    assert np.all(arr2 == 1)
    assert np.all(arr3 == [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    
def test_array_operations():
    
    det, inv, pow = ex.array_operations(arr)
    
    assert np.isclose(det, np.linalg.det(arr))
    assert np.allclose(inv, np.linalg.inv(arr)) 
    assert np.allclose(pow, arr**3)

    
def test_indexing_slicing():

    subarr, cols, diag = ex.indexing_slicing(arr)
    
    assert subarr.shape == (5, 5)
    assert np.allclose(cols, arr[:, ::2]) 
    assert np.isclose(diag, np.trace(arr))

    
def test_arithmetic_operations():

    sine, matmul, dot = ex.arithmetic_operations(arr1, arr2)
    
    assert np.allclose(sine, np.sin(arr1))
    assert np.allclose(matmul, arr1 @ arr2)
    assert np.isclose(dot, np.dot(arr1.ravel(), arr2.ravel()))

    
def test_aggregate_functions():

    mean, unique, sorted = ex.aggregate_functions(arr3)
    
    assert np.isclose(mean, np.mean(arr3))
    assert np.allclose(unique, np.unique(arr3))
    assert np.allclose(sorted, np.sort(arr3))

    
def test_reorganize_arrays():

    vert_stack, hori_stack, flattened = ex.reorganize_arrays(arr4, arr5)
    
    expected_vert = np.vstack([arr4, arr5])
    expected_hori = np.hstack([arr4, arr5])
    
    assert np.allclose(vert_stack, expected_vert)
    assert np.allclose(hori_stack, expected_hori)
    assert np.allclose(flattened, arr5.ravel())