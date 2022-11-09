
import gym
import math
import numpy as np
from scipy.special import kl_div
import copy

import idm
import utils
import features
from visual import Agent, Lane, Environment



class Env(gym.Env):
    def __init__(self):
        
        self.action_space = gym.spaces.Discrete(21)
        self.observation_space = gym.spaces.Box(low=np.array([50, 0, 0, 0] + [0 for i in range(utils.rows*utils.cols)]), 
                                                high=np.array([1000, 1000, 30, 30] + [1 for i in range(utils.rows*utils.cols)]), 
                                                dtype=np.float64)
        
        
        self.phi = utils.generate_particles()
        
        self.features = features.Features()
        
        return
        
    def reset(self):
        
        self.idm = idm.IDM(v_0 = 25, T=1.5)
        
        self.target_belief = utils.generate_target_belief(self.idm.v_0, self.idm.T).flatten()
        
        self.episode = 0
        self.state = np.array([50, 0, 20, 20], dtype=np.float64) # later modify for stochasticity
        self.belief = (self.phi[0] + self.phi[0])*0 + 1/(400)
        
        # visual
        self.lane_list  = [Lane(utils.l0_corner, utils.lane_width, 0),
                           Lane(utils.l1_corner, utils.lane_width, 1)]
        pos = utils.state_to_plot(self.state)
        self.agent_list = [Agent('./images/car-yellow.png', [self.lane_list[1].middle, pos[0]], 20),
                           Agent('./images/car-orange.png', [self.lane_list[1].middle, pos[1]], 20)]
        self.environment = Environment(self.lane_list, self.agent_list, copy.deepcopy(self.state))
        
        return np.concatenate([self.state, self.belief.flatten()])
        
        
    def step(self, action):
        
        #nominal_action = utils.nominal_action(self.state)
        
        
        # dynamics
        robot_action = action/10.0 - 1
        human_action = self.idm.select_action(self.state)
        self.state[0] += robot_action/2*utils.d_t**2 + self.state[2]* utils.d_t
        self.state[2] += robot_action * utils.d_t
        self.state[1] += human_action/2*utils.d_t**2 + self.state[3]* utils.d_t
        self.state[3] += human_action * utils.d_t
        
        # belief
        temp = np.exp(self.features.reward(self.state, self.phi))
        self.belief = np.multiply(self.belief, temp)
        flat = self.belief.flatten()
        summation = np.sum(flat)
        self.belief /= summation
        
        next_state = np.concatenate([self.state, flat])
        
        # next state
        kld_list = kl_div(self.target_belief, flat)
        
        reward = (utils.LAMBDA) * - sum(kld_list)
        
        
        # done
        safe = self.state[0] > self.state[1] + 10
        too_small = min(kld_list) <= np.nextafter(0, 1)
        done = not safe or too_small
        
        if not safe:
            reward -= 10
        
        if too_small:
            reward -= 10
            
 

        # info
        self.episode += 1
        
        if done == True:
            info = {'episode': {'r': self.episode, 'l': 25, 't': 5.360702}, 'terminal_observation': np.array(next_state, dtype=np.float64)}
        else:
            info = {}

        return np.array(next_state, dtype=np.float64), reward, done, info
    
    def render(self):
        self.environment.step(self.state)
        return

    def close(self):
        return


