import numpy as np
a=np.array([1,2,3]) #1D array
b=np.array([4,5,6])
result=a+b
print(result)

b=np.array([4]) #singleton array means array with 1 element
result=a+b
print(result)

# a=np.array([1,2,3,4])
# b=np.array([4,5])
# result=a+b
# print(result)   #Error

a=5
b=2.0
print(a+b)

c=int(b)
print(c)
print(type(c))

a=np.array([1,2,3]) #1D array
b=np.array([4,5,6])
r=np.empty_like(a)  #r=np.empty(3)
np.add(a,b,out=r)
print(r)

print(np.add(a,b))
print(np.multiply(a,b))
print(np.sin(np.array([0,np.pi/2,np.pi])))
