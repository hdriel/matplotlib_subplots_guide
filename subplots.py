import matplotlib.pyplot as plt
from matplotlib import style
import random

fig = plt.figure()
style.use('seaborn-dark-palette')

def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)

    return xs, ys

def showPlots(axs):
    for ax in axs:
        x,y = create_plots()
        ax.plot(x,y)
    plt.subplots_adjust(left=0.11, bottom= 0.24, right=0.90, top=0.90, wspace=0.4, hspace=0.4)
    plt.show()
    plt.close('all')
    
##-------------------------------------------------------------------

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)
showPlots([ax1,ax2,ax3])


#######################################################################

ax = []
ax.append(plt.subplot2grid((3,3), (0,0), rowspan = 1, colspan = 1))
ax.append(plt.subplot2grid((3,3), (0,1), rowspan = 1, colspan = 1))
ax.append(plt.subplot2grid((3,3), (0,2), rowspan = 1, colspan = 1))
ax.append(plt.subplot2grid((3,3), (1,0), rowspan = 1, colspan = 1))
ax.append(plt.subplot2grid((3,3), (1,1), rowspan = 1, colspan = 1))
ax.append(plt.subplot2grid((3,3), (1,2), rowspan = 1, colspan = 1))
ax.append(plt.subplot2grid((3,3), (2,0), rowspan = 1, colspan = 1))
ax.append(plt.subplot2grid((3,3), (2,1), rowspan = 1, colspan = 1))
ax.append(plt.subplot2grid((3,3), (2,2), rowspan = 1, colspan = 1))
showPlots(ax)

#####################################################################

ax = []
ax.append(plt.subplot2grid((3,3), (0,0), rowspan = 1, colspan = 1))
ax.append(plt.subplot2grid((3,3), (0,1), rowspan = 1, colspan = 1))
ax.append(plt.subplot2grid((3,3), (0,2), rowspan = 3, colspan = 1))
ax.append(plt.subplot2grid((3,3), (1,0), rowspan = 2, colspan = 2))
showPlots(ax)

#####################################################################

 
