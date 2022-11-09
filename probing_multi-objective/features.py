import utils


class Features:
    def __init__(self):
        self.sigma = utils.sigma
        return

    def reward(self, state, phi):
        return (-(state[3] - phi[0])**2)/self.sigma[0]**2 + (-((state[0]-state[1])/state[3] - phi[1])**2)/self.sigma[1]**2
