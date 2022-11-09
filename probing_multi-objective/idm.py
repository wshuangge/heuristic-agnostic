import math


class IDM:
    def __init__(self, v_0=25, T=1.5, a=0.73, b=1.67, delta=4, s_0=2):
        self.v_0 = v_0
        self.T = T
        self.a = a
        self.b = b
        self.delta = delta
        self.s_0 = s_0

    def select_action(self, state):
        spacing = self.s_0 + state[3] * self.T + (state[3] - state[2]) / (2 * math.sqrt(self.a*self.b))
        action = self.a * (1-(state[3]/self.v_0)**self.delta - (spacing/(state[0]-state[1]))**2)
        return action
