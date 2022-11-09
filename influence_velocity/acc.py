import math
import config
import numpy as np


class Acc:
    def __init__(self, id, headway):
        self.id = id
        self.headway = headway
        self.head_id = id - 1
        
        # IDM parameters
        self.v_0 = 25
        self.T = 1.5
        self.a = 0.73
        self.b = 1.67
        self.delta = 4
        self.s_0 = 2

    """
    def generate_control(self, state):
        if self.id == 2:
            return 0
        else:
            print(self.head_id, self.id)
            headway = state.x[self.head_id] - state.x[self.id]
        if (headway <= self.headway):
            reward = []
            for i in config.acc_action_space:
                controls = [0 for i in range(len(state.x))]
                controls[self.id] = i
                new_state = state.update(controls, config.d_t)
                reward.append(-(new_state.x[self.head_id] - new_state.x[self.id] - self.headway)**2)
            pos = np.argmax(reward)
            return config.acc_action_space[pos]
        else:
            reward = []
            for i in config.acc_action_space:
                controls = [0 for i in range(len(state.x))]
                controls[self.id] = i
                new_state = state.update(controls, config.d_t)
                reward.append(-(new_state.v[self.head_id] - new_state.v[self.id])**2 - 1 * (state.u[0]-i)**2)
            pos = np.argmax(reward) 
            return config.acc_action_space[pos]
    """

    def generate_control(self, state):
        if self.id == 2:
            return 0
        else:
            desired_headway = self.s_0 + state.v[self.id] * self.T + (state.v[self.id] - state.v[self.head_id]) / (2 * math.sqrt(self.a * self.b))
            print(desired_headway)
            human_action = self.a * (1 - (state.v[self.id] / self.v_0)**self.delta - (desired_headway / (state.x[self.head_id] - state.x[self.id]))**2)
            return human_action