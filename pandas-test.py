import pandas as pd
import numpy as np
arr=np.array([10,20,30,40,50])
mask=arr>20
print(mask)

filtered=arr[mask]
print(filtered)

print(arr[arr>25])

arr=np.array([[1,5,9],[2,6,10],[3,7,11]])
mask=arr>5
print(mask)

print(arr[mask])

arr=np.array([10,20,30,40,50])
arr[arr>25]=0
print(arr)

import numpy.ma as ma
arr=np.array([1,2,-999,4,5])
masked=ma.masked_where(arr==-999,arr)
print(masked)
print(masked.mean())

arr=np.array([True,False,True,True])
print(arr)
print(arr.dtype)

arr=np.array([10,15,20,25,30])
mod=arr>20
print(arr[mod])

arr=np.array([5,10,15,20,25])
mod=(arr>10) & (arr<25)
print(mod)
print(arr[mod])

a=np.array([10,20,30,40,50])
selected=a[[0,2,4]]
print(selected)



# l=[10,20,30,40,50]
# for i in l :
#     if not(i>20):
#         l.remove(i)
# print(l)
# print(l[l>25])
