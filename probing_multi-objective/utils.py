import numpy as np
import pickle

LAMBDA = 1
EPSILON_KL = 0.1

d_t = 0.1

l0_corner = [25, 0]
l1_corner = [75, 0]
lane_width = 50 

real_to_plot_ratio = 5


sigma = 5000, 50

rows, cols  = 10, 10


min_velocity, max_velocity = 10, 36
min_headway, max_headway = 1, 2


human_action_space, ego_action_space = np.linspace(start=-1, stop=1, num=21),  np.linspace(start=-1, stop=1, num=21)

graph_gap = 5


def generate_particles():
    v = np.linspace(min_velocity, max_velocity, rows)
    h = np.linspace(min_headway, max_headway, cols)
    x, y = np.meshgrid(v, h)
    return x, y

def read_target_belief():
    with open('./data/belief.txt', 'rb') as f:
        baseline = pickle.load(f)
    return baseline[-1]

def generate_target_belief(desired_velocity, desired_headway):
    v = np.linspace(min_velocity, max_velocity, rows)
    h = np.linspace(min_headway, max_headway, cols)
    x, y = np.meshgrid(v, h)
    belief = (x + y)*0
    a, b = int((desired_velocity-min_velocity)/(max_velocity-min_velocity)*(rows-1)) , int((desired_headway-min_headway)/(max_headway-min_headway)*(cols-1))
    belief[a, b] = 1
    return belief
    
def state_to_plot(state):
    relative = []
    for i in range(2):
        relative.append((state[1]-state[i])*real_to_plot_ratio + 900)
    return relative

def generate_phi():
    index = (19, 4)
    return [[max_velocity/29*index[0], max_headway/29*index[1]]]


def nominal_action(state):
    reward = []
    for i in ego_action_space:
        new_velocity = i * d_t + state[1]
        reward.append(-(new_velocity - state[3])**2)
    return ego_action_space[np.argmax(reward)]