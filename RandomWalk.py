import numpy as np
import seaborn as sea
import matplotlib.pyplot as plt

currPosition =0
steps = 1000
positionHistory = [currPosition]

for _ in range(steps):
    step = np.random.choice([-1,1])
    currPosition += step
    positionHistory.append(currPosition)
    
    
sea.lineplot(x=range(steps + 1), y=positionHistory )
plt.xlabel("steps")
plt.ylabel("position")
plt.axis()

plt.show()