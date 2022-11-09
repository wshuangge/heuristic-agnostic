import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
from scipy.interpolate import make_interp_spline
from scipy.stats import entropy
import config
from matplotlib.ticker import FormatStrFormatter

font = {'size': 13}
plt.rc('font', **font)

length = 800

with open('./data/deviation.txt', 'rb') as f:
    active_deviation = pickle.load(f)

with open('./data/velocity.txt', 'rb') as f:
    active_velocity = pickle.load(f)


color = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']


def plot_perturbation(active):
    x = [i/10 for i in range(length)]
    
    stacked = plt.figure()
    kwargs = dict(alpha=0.2)
    ax = stacked.add_subplot(111)
    
    legend_1=[]
    legend_2=[]
    labels = ['Autonomous Vehicle', 'Human Vehicle', 'Background Vehicle']

        
    for i in range(len(active)):
        if i == 0:
            temp = ax.plot(x, active[i][:length], ls = "-", label=labels[i], color = color[i])
            legend_2.append(temp)
            legend_1.append(temp)
        else:
            legend_1.append(ax.plot(x, active[i][:length], ls = "-", label=labels[i], color = color[i]))
            

    l_1= ax.legend(legend_1[0]+ legend_1[1] + legend_1[2], labels, loc='upper left')
    plt.gca().add_artist(l_1)
    
    #ax.legend(legend_2[0]+legend_2[1], ["Active", "Passive"], loc='center left')
    #ax.set_xticks([i*config.graph_gap for i in range(int(config.rows/config.graph_gap))])
    ax.set_xlabel('$Time \hspace{1} (s)$')
    ax.set_ylabel('$Cumulative \hspace{1} Absolute \hspace{1} Control \hspace{1} (m/s)$')
    plt.show()
    stacked.savefig("./figures/deviation_1.jpg".format(), dpi=300)
    
    
def plot_velocity(active):
    x = [i/10 for i in range(length)]

    stacked = plt.figure()
    kwargs = dict(alpha=0.2)
    ax = stacked.add_subplot(111)

    legend_1=[]
    legend_2=[]
    labels = ['Autonomous Vehicle', 'Human Vehicle', 'Background Vehicle']

        
    for i in range(len(active)):
        if i == 0:
            temp = ax.plot(x, active[i][:length], ls = "-", label=labels[i], color = color[i])
            legend_2.append(temp)
            legend_1.append(temp)
        else:
            legend_1.append(ax.plot(x, active[i][:length], ls = "-", label=labels[i], color = color[i]))


    l_1= ax.legend(legend_1[0]+ legend_1[1] + legend_1[2], labels, loc='upper left')
    plt.gca().add_artist(l_1)

    #ax.legend(legend_2[0]+legend_2[1], ["Active", "Passive"], loc='center right')
    #ax.set_xticks([i*config.graph_gap for i in range(int(config.rows/config.graph_gap))])
    #ax.set_xticklabels([r'$\varphi_{'+str(i*config.graph_gap)+'}$' for i in range(int(config.rows/config.graph_gap))])
    ax.set_xlabel('$Time \hspace{1} (s)$')
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    ax.set_ylabel('$Velocity \hspace{1} Deviation \hspace{1} (m/s)$')
    plt.show()
    stacked.savefig("./figures/velocity_1.jpg".format(), dpi=300)

if __name__ == "__main__":
    print("active_velocity", len(active_velocity))
    print("active_deviation",len(active_deviation))
    print("active_deviation",active_deviation[2][length])
    plot_perturbation(active_deviation)
    plot_velocity(active_velocity)