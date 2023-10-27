import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea

def run3DRandomWalk(steps: int, initialxPos: int, initialyPos: int, initialzPos: int,visualize: bool = False, simulationReps: int = 1):
    for simRepNumber in range(simulationReps):
        x,y,z = initialxPos, initialyPos, initialzPos
        steps = steps
        xHistory, yHistory, zHistory = [x], [y], [z]
        xTarget, yTarget, zTarget = 5,5,5
        timesTargetFound = 0
        
        for _ in range(steps):
            x_step, y_step, z_step = np.random.choice([-1, 1], 3)
            x += x_step
            y += y_step
            z += z_step
            xHistory.append(x)
            yHistory.append(y)
            zHistory.append(z)
            
            if x == xTarget and y == yTarget and z == zTarget:
                timesTargetFound += 1
                               
        print(f"found target {timesTargetFound} times")
        
        if visualize:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            
            #plot 3d movement
            ax.plot(xHistory, yHistory, zHistory, label='3D Random Walk')
            ax.plot(xTarget, yTarget, zTarget,"ro" ,label= "Target", )
            
            ax.set_xlabel('X Position')
            ax.set_ylabel('Y Position')
            ax.set_zlabel('Z Position')
            ax.set_title('3D Random Walk')

            plt.legend()
            plt.show()
            
            
if __name__=="__main__":
    run3DRandomWalk(100000,0,0,0,True,1)