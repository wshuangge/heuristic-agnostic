import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
from scipy.interpolate import make_interp_spline
from scipy.stats import entropy
from influence_headway import config
from matplotlib.ticker import FormatStrFormatter
font = {'size': 13}
plt.rc('font', **font)

length = 350

with open('./influence_headway/data/deviation.txt', 'rb') as f:
    active_deviation = pickle.load(f)

with open('./influence_headway_passive/data/deviation.txt', 'rb') as f:
    passive_deviation = pickle.load(f)
    
with open('./influence_headway/data/velocity.txt', 'rb') as f:
    active_velocity = pickle.load(f)

with open('./influence_headway_passive/data/velocity.txt', 'rb') as f:
    passive_velocity = pickle.load(f)


color = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']


def plot_perturbation(active, passive):
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
            
    for i in range(len(passive)):
        if i ==0:
            legend_2.append(ax.plot(x, passive[i][:length], ls = "--", label=labels[i], color = color[i]))
        else:
            ax.plot(x, passive[i][:length], ls = "--",  label=labels[i], color = color[i])
                

    l_1= ax.legend(legend_1[0]+ legend_1[1] + legend_1[2], labels, loc='lower right')
    plt.gca().add_artist(l_1)
    
    ax.legend(legend_2[0]+legend_2[1], ["Active", "Passive"], loc='upper left')
    #ax.set_xticks([i*config.graph_gap for i in range(int(config.rows/config.graph_gap))])
    ax.set_xlabel('$Time \hspace{1} (s)$')
    ax.set_ylabel('$Cumulative \hspace{1} Absolute \hspace{1} Control \hspace{1} (m/s)$')
    plt.show()
    stacked.savefig("./deviation_2.jpg".format(), dpi=300)
    
    
def plot_velocity(active, passive):
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
            
    for i in range(len(passive)):
        if i ==0:
            legend_2.append(ax.plot(x, passive[i][:length], ls = "--", label=labels[i], color = color[i]))
        else:
            ax.plot(x, passive[i][:length], ls = "--",  label=labels[i], color = color[i])
                

    l_1= ax.legend(legend_1[0]+ legend_1[1] + legend_1[2], labels, loc='upper right')
    plt.gca().add_artist(l_1)

    ax.legend(legend_2[0]+legend_2[1], ["Active", "Passive"], loc='lower left')
    #ax.set_xticks([i*config.graph_gap for i in range(int(config.rows/config.graph_gap))])
    #ax.set_xticklabels([r'$\varphi_{'+str(i*config.graph_gap)+'}$' for i in range(int(config.rows/config.graph_gap))])
    ax.set_xlabel('$Time \hspace{1} (s)$')
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    ax.set_ylabel('$Velocity \hspace{1} Deviation \hspace{1} (m/s)$')
    plt.show()
    stacked.savefig("./velocity_2.jpg".format(), dpi=300)


if __name__ == "__main__":
    print("passive_deviation", len(passive_deviation[1]))
    print("active_deviation",len(active_deviation))
    print(passive_deviation[2][-1],active_deviation[2][-1], passive_deviation[2][-1] )
    for i in range(3):
        print("values", passive_deviation[i][length], active_deviation[i][length], passive_deviation[i][length])
        print("i:", (passive_deviation[i][length]-active_deviation[i][length])/passive_deviation[i][length])
    plot_perturbation(active_deviation, passive_deviation)
    plot_velocity(active_velocity, passive_velocity)