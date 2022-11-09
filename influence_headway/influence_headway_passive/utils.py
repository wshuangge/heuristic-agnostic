import config
import numpy as np
import matplotlib.pyplot as plt


class Struct:
    def __init__(self, control, state, belief, reward, prev):
        self.control = control
        self.state = state
        self.belief = belief
        self.reward = reward
        self.prev = prev

def state_to_plot(state):
    relative = []
    for i in range(len(state.x)):
        relative.append((state.x[i] - state.x[0])*-config.plot_to_real_ratio)
    relative = [each + 600 for each in relative]
    return relative

def generate_phi(i, j):
    temp = [[(1/config.cols/config.rows)for i in range(config.cols)]
            for j in range(config.rows)]
    for x in range(config.rows):
        for y in range(config.cols):
            temp[x][y] = -((x-i)**2 + (y-j)**2)
    flat = np.array(temp).flatten()
    mini = min(flat)
    for x in range(config.rows):
        for y in range(config.cols):
            temp[x][y] -= mini
    flat = np.array(temp).flatten()
    summation = sum(flat)
    for x in range(config.rows):
        for y in range(config.cols):
            temp[x][y] /= summation
            temp[x][y] *= config.feature_norm
    return temp

def generate_particles():
    temp = [(i, 6) for i in range(config.cols)]
    particles = []
    for index in temp:
        phi = generate_phi(index[0], index[1])
        particles.append(phi)
    return particles


def images_to_video(length):
    import cv2
    import numpy as np
    import os
    from os.path import isfile, join
    pathIn= './frames/'
    pathOut = './videos/video1.avi'
    fps = 40
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    #for sorting the file names properly
    files = list(filter(lambda k: '_' in k, files))
    print(files)
    files.sort(key = lambda x: int(x.split("_")[2][:x.split("_")[2].index(".")]))
    files = files[0:length]
    for i in range(len(files)):
        filename = pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        height, width, layers = img.shape
        size = (width,height)
        
        #inserting the frames into an image array
        frame_array.append(img)
    
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()


plt.ion()
figure = plt.figure()

def plot_deviation(x, y, state, timer):
    ax = figure.add_subplot(111)
    labels = ['Autonomous Vehicle (Orange)', 'Human Vehicle (Orange)', 'Background Vehicle 1 (White)', 'Background Vehicle 2 (White)']
    for i in range(len(y)):
        ax.step(x, y[i], where='mid', label=labels[i])
        
    ax.grid(axis='x', color='0.95')
    ax.legend(title='')
    ax.set_xlabel('$Time \hspace{1} (s)$')
    ax.set_ylabel('$Velocity \hspace{1} Deviation \hspace{1} (m/s)$')
    figure.canvas.draw()
    
    if (min(state.v)>=19 and timer >= 400):
        figure.savefig("./figures/deviation1.jpg", dpi=300)
    
    figure.canvas.flush_events()
    figure.clf()
    

plt.ion()
figure = plt.figure()

def plot_velocity(x, y, state, timer):
    ax = figure.add_subplot(111)
    labels = ['Autonomous Vehicle (Yellow)', 'Human Vehicle (Orange)', 'Background Vehicles (White)']
    for i in range(len(y)):
        ax.step(x, y[i], where='mid', label=labels[i])
        
    ax.grid(axis='x', color='0.95')
    ax.legend(title='')
    ax.set_xlabel('$Time \hspace{1} (s)$')
    ax.set_ylabel('$Velocity \hspace{1} Deviation \hspace{1} (m/s)$')
    figure.canvas.draw()
    if (timer >= 400):
        figure.savefig("./figures/velocity2.jpg", dpi=300)

    figure.canvas.flush_events()
    figure.clf()


fig = plt.figure()
def plot_deviation(x, y, state, timer):
    ax = fig.add_subplot(111)
    labels = ['Autonomous Vehicle (Yellow)', 'Human Vehicle (Orange)', 'Background Vehicles (White)']
    for i in range(0, len(y)):
        ax.step(x, y[i], where='mid', label=labels[i])
        
    ax.grid(axis='x', color='0.95')
    ax.legend(title='')
    ax.set_xlabel('$Time \hspace{1} (s)$')
    ax.set_ylabel('$Cumulative \hspace{1} Control \hspace{1} Deviation \hspace{1} (m/s)$')
    fig.canvas.draw()
    
    if (timer >= 400):
        fig.savefig("./figures/deviation2.jpg", dpi=300)
    
    fig.canvas.flush_events()
    fig.clf()

if __name__ == '__main__':
    images_to_video(500)