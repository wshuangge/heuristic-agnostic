import utils


class Features:
    def __init__(self):
        return

    def weighted_sum(self, state, phi):
        return (-(state[3] - phi[0])**2 - ((state[0]-state[2]) - phi[1])**2)/utils.sigma