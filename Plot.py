import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd

style.use("fivethirtyeight")
fig = plt.figure()

file_r = pd.read_csv("F.csv")

subPlots = []
for i in range(0,len(file_r)):
    subPlots.append(fig.add_subplot(2,2,i+1))

# obj = main()

def animate(p):
    cnt = 2
    for figs in subPlots:
        y = file_r.iloc[0:, cnt].values
        x = list(range(1, len(y) + 1))
        figs.clear()
        figs.plot(x, y)
        # figs.set_title(str(file_r.iloc[0:, cnt].values[0]), fontsize=10)
        # figs.set_title(obj.code[cnt-2], fontsize=10)
        cnt = cnt + 1


anm = animation.FuncAnimation(fig,animate,interval=1000)
plt.tight_layout()
plt.show()