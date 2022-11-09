import math
from msilib.schema import Condition
import config
import numpy as np


class Idm:
    def __init__(self):
        self.v_0 = 20
        self.T = 1.5
        self.a = 0.73
        self.b = 1.67
        self.delta = 4
        self.s_0 = 2 + config.car_length
        self.id = 1
        self.head_id = None
        self.phase = 0
        self.behind = 15
        
    """
    def find_headway(self, state):
        headway = []
        for i in range(2, len(state.x)):
            h = state.x[i] - state.x[1]
            if h <= 0:
                break
            else:
                headway.append(h)
        return np.argmin(headway) + 2
    """

 
    def find_head_id(self, state):
        headway = []
        for i in range(2, len(state.x)-1):
            h = state.x[i] - state.x[i+1]
            headway.append(h)
        return np.argmax(headway) + 2
    
    def find_head(self, state):
        headway = []
        for i in range(2, len(state.x)-1):
            h = state.x[i] - state.x[self.id]
            if h < 0:
                break
            else:
                headway.append(h)
        return np.argmin(headway) + 2
    
    
    def merge_condition(self, state):
        min_headway = self.s_0 + state.v[1] * self.T + (state.v[1] - state.v[self.head_id]) / (2 * math.sqrt(self.a * self.b))
        real_headway = state.x[self.head_id] - state.x[self.id]
        
        condition_1 = real_headway >= min_headway
        condition_2 = state.x[self.id] - state.x[0] - self.behind > -2
        condition_3 = state.x[self.head_id] > state.x[self.id]
        print(condition_1, condition_2, condition_3)
        return condition_1 and condition_2 and condition_3
    
    def generate_control(self, state):
        print("idm head:", self.head_id, self.phase)
        match self.phase:
            case 0:
                if self.head_id == None:
                    self.head_id = 0
                if state.lane[0]==0:
                    self.phase = 1

                desired_headway = self.s_0 + state.v[1] * self.T + (state.v[1] - state.v[self.head_id]) / (2 * math.sqrt(self.a * self.b))
                human_action = self.a * (1 - (state.v[1] / self.v_0)**self.delta - (desired_headway / (state.x[self.head_id] - state.x[self.id]))**2)
                return human_action
            case 1:
                self.head_id = self.find_head(state)

                min_headway = self.s_0 + state.v[1] * self.T + (state.v[1] - state.v[self.head_id]) / (2 * math.sqrt(self.a * self.b))
                real_headway = state.x[self.head_id] - state.x[self.id]
                print("comp", real_headway, min_headway)
                if self.merge_condition(state):
                    self.phase = 2

                reward = []
                for i in config.human_action_space:
                    controls = [0 for i in range(len(state.x))]
                    controls[self.id] = i
                    new_state = state.update(controls, config.d_t)
                    reward.append(-4*(new_state.x[self.id] - new_state.x[0] - self.behind)**2 -(new_state.v[self.id] - new_state.v[0])**2)
                pos = np.argmax(reward)
                return config.human_action_space[pos]
            case 2:
                self.head_id = self.find_head(state)
                state.lane[self.id] = 0
                desired_headway = self.s_0 + state.v[1] * self.T + (state.v[1] - state.v[self.head_id]) / (2 * math.sqrt(self.a * self.b))
                human_action = self.a * (1 - (state.v[1] / self.v_0)**self.delta - (desired_headway / (state.x[self.head_id] - state.x[self.id]))**2)
                return human_action
