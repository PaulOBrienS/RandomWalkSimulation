import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea


def run2dRandomWalk(steps: int, initialxPos: int, initialyPos: int, visualize: bool = False, simulationReps: int = 1):
    for simRepNumber in range(simulationReps):
        x, y = initialxPos, initialyPos
        steps = steps
        x_history, y_history = [x], [y]
        x_target, y_target = 3,3
        timesTargetFound = 0

        for _ in range(steps):
            # Generate random steps in both x and y directions
            x_step, y_step = np.random.choice([-1, 1], 2)
            x += x_step
            y += y_step
            x_history.append(x)
            y_history.append(y)
            
            if x == x_target and y == y_target:
                timesTargetFound += 1
            
        print(f"found target {timesTargetFound} times")
        
        if visualize:
            arrow_x = np.array(x_history[:-1])  # Exclude the final position
            arrow_y = np.array(y_history[:-1])
            arrow_dx = np.diff(x_history)  # Differences between consecutive x positions
            arrow_dy = np.diff(y_history)  # Differences between consecutive y positions
            plt.clf()
            plt.quiver(arrow_x, arrow_y, arrow_dx, arrow_dy, angles='xy', scale_units='xy', scale=1, color='b', width=0.005, headwidth=5)
            sea.scatterplot(x=x_history, y=y_history)
            plt.plot(x_target, y_target, 'ro', label="Target Location")
            plt.xlabel("xpath")
            plt.ylabel("ypath")
            plt.title("2D Random Walk")
            plt.axis("equal")
            plt.legend()
            plt.savefig(fname = f"2DRandomWalkVisSimulation{simRepNumber + 1}.png")

if __name__ == "__main__":
    run2dRandomWalk(100,0,0, True, 100)