import config
import utils
from state import State
from idm import Idm
from features import Features
from ego import Ego
from acc import Acc
from visual import *
from statistics import mean

import numpy as np
import matplotlib.pyplot as plt

import pickle

particles = utils.generate_particles()
features = Features()
ego = Ego()
idm = Idm()

cars = 7
acc_list = []

headway = [60, 60, 90, 60, 60]
for i in range(2, cars):
    acc_list.append(Acc(i, headway[i - 2]))

dynamics = [[0, 20], [-50, 20],
            [0, 25], [-sum(headway[:1]), 25], [-sum(headway[:2]), 25], [-sum(headway[:3]), 25], [-sum(headway[:4]), 25]]

lanes = [1, 1] + [0 for i in range(2, cars - 2)]

state = State(dynamics, lanes)

# lanes
l1, l2 = Lane([25, 0], 50, 1), Lane([75, 0], 50, 2)

lane_list = [l1, l2]

pos = utils.state_to_plot(state)

# agents
ego_P, ego_S = [config.right_lane_center, pos[0]], 20
human_P, human_S = [config.right_lane_center, pos[1]], 20


robot = Agent('./images/car-yellow.png', ego_P, ego_S)
human = Agent('./images/car-orange.png', human_P, human_S)

agent_list = [robot, human]

# obstacles
obj_list = []

for i in range(2, cars):
    obj_list.append(Obstacles('./images/car-white.png',
                    [config.left_lane_center, pos[5]], 25))


if __name__ == '__main__':

    # plot to real world: 10 : 1
    env = Environment(lane_list, obj_list, agent_list, state)
    gameExit = False
    timer = 0

    x, velocity, deviation = [], [], []

    while not gameExit:

        controls = []

        #print("target:" , ego.target, "phase:", ego.phase)
        #print(acc_list[5].head_id, "sdsd")
        if(state.lane[1] == 0):
            acc_list[idm.head_id -1].head_id = 1

        # ego control
        ego_control = ego.generate_control(state)
        controls.append(ego_control)

        # human control
        human_action = idm.generate_control(state)
        controls.append(human_action)

        # acc control
        for acc in acc_list:
            controls.append(acc.generate_control(state))

        state.print()

        print("controls", controls)

        new_state = state.update(controls, config.d_t)

        env.step(new_state, state)

        state = new_state
        
        
        # plotting
        x.append(timer/10)
        # velocity
        if timer == 0:
            velocity.append([state.v[0] - 20])
            velocity.append([state.v[1] - 20])
            velocity.append([mean(state.v[5:]) - 25])
        else:
            velocity[0].append(state.v[0] - 20)
            velocity[1].append(state.v[1] - 20)
            velocity[2].append(mean(state.v[5:]) - 25)
        

        utils.plot_velocity(x, velocity, state, timer)
        
        # deviation
        if timer == 0:
            deviation.append([abs(controls[0] * config.d_t)])
            deviation.append([abs(controls[1] * config.d_t)])
            deviation.append([abs(mean(controls[5:]) * config.d_t)])
        else:
            deviation[0].append(deviation[0][-1] + abs(controls[0] * config.d_t))
            deviation[1].append(deviation[1][-1] + abs(controls[1] * config.d_t))
            deviation[2].append(deviation[2][-1] + abs(mean(controls[5:]) * config.d_t))

        utils.plot_deviation(x, deviation, state, timer)

        print("current time:", timer/10)
        
        with open("./data/velocity.txt", "wb") as fp: #Pickling
            pickle.dump(velocity, fp)
        with open("./data/deviation.txt", "wb") as fp: #Pickling
            pickle.dump(deviation, fp)
        

        timer += 1
        

            
        mainClock.tick(FPS)
        # input()

    pygame.quit()
    quit()
