import numpy as np
import pickle

LAMBDA = 1
EPSILON_KL = 0.1

d_t = 0.1

l0_corner = [25, 0]
l1_corner = [75, 0]
lane_width = 50 

real_to_plot_ratio = 5


sigma = 5000

cols, rows = 30, 30


max_velocity = 36
max_headway = 350


human_action_space, ego_action_space = np.linspace(start=-1, stop=1, num=21),  np.linspace(start=-1, stop=1, num=21)

graph_gap = 5


def generate_particles():
    temp = [(i, 9) for i in range(cols)]
    particles = []
    for index in temp:
        phi = [36/29*index[0], 350/29*index[1]]
        particles.append(phi)
    return particles

def read_target_belief():
    with open('./data/belief.txt', 'rb') as f:
        baseline = pickle.load(f)
    return baseline[-1]

def generate_target_belief(desired_velocity):
    digit = round(desired_velocity/max_velocity*(cols-1))
    belief = [0 for i in range(cols)]
    belief[digit] = 1
    return belief, digit
    
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