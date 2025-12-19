# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[2,3,4,5,6]
# plt.plot(x,y)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("Simple Line Plot")
# plt.show()


# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[5,3,6,2,7]
# plt.scatter(x,y)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("Simple Scatter Plot")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([1,2,3,4,5])
# y=np.array([2,4,6,8,10])
# y1=np.array([3,5,7,9,11])
# plt.plot(x,y1,label="y=2x+1",linewidth=4,color="red",marker="o")
# # plt.plot(x,y,label="y=2x",linewidth=2)
# plt.title("Line Plot")
# plt.xlabel("x value")
# plt.ylabel("y value")
# plt.legend(loc="upper left",title="Graph")
# plt.grid(True)
# plt.xticks(x)
# plt.yticks(y1)
# sc=plt.scatter(x,y,c=y,cmap="")
# plt.colorbar(sc,label="color")
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5]
y1=[2,4,6,8,10]
y2=[3,5,7,9,11]
fig,ax=plt.subplots(2,1,figsize=(6,6))
ax[0].plot(x,y1)
ax[0].set_title("First Line Plot")
ax[0].text(3,6,"Sample Text")
ax[0].annotate("Highest Value",
                xy=(5,10),
                xytext=(3,9),
                arrowprops=dict(arrowstyle="->"))
ax[1].plot(x,y2)
ax[1].set_title("Second Line Plot")
plt.tight_layout()
plt.show()
