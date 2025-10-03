import numpy as np
data=np.random.randint(50,100,size=(5,4))
print("Original data (5x4):\n",data)
adjustment=np.array([5,-2,0,3])
adjusted_data=data+adjustment
print("\nData after broadcasting:\n",adjusted_data)
high_values_mask=data>80
print("\nBoolean mask (values>80):\n",high_values_mask)
high_values=data[high_values_mask]
print("\nValues from the original data that are >80:",high_values)
