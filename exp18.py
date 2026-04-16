# Aim = NumPy Array
# Coder = Mayuresh Mene
# Class = F.E.Computers 1
# UIN/Roll no = 251P016 / 15
# Date = 
import numpy as np

arr1=np.array([10, 20, 30, 40 ,50])
print("1D array:\n",arr1)

arr2=np.array([[1, 2, 3],
              [4, 5, 6]])
print("2D array:\n",arr2)

arr3=np.array([
    [[1, 2],[3, 4]],
    [[5, 6],[7, 8]]
])
print("3D array:\n",arr3)

reshaped=arr1.reshape(5,1)
print("Reshaped array :\n",reshaped)

print("\nSlicing")
print("First three elements: ",arr1[:3])
print("Last two elements: ",arr1[-2:])
print("2D column slice: ",arr2[:,1])

print("Indexing")
print("1D index ",arr1[2])
print("2D index ",arr2[1][2])
print("3D index ",arr3[1][0][1])