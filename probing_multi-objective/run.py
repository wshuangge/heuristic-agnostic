
import sys
from stable_baselines3 import DQN
import matplotlib.pyplot as plt
import numpy as np

import env
import utils

x = [r'$\varphi_{'+str(i)+'}$' for i in range(utils.rows)]
plt.ion()
figure_1 = plt.figure()
belief_plot = figure_1.add_subplot(111)
figure_2 = plt.figure()
kld_plot = figure_2.add_subplot(111)

if __name__ == "__main__":

    env = env.Env()
    
    if sys.argv[1] == "train":
        
        model = DQN("MlpPolicy", env, verbose=1, learning_rate=0.0005, exploration_fraction=0.1, exploration_final_eps=0.1, exploration_initial_eps=1.0)
        model.learn(total_timesteps=2000000, log_interval= 4)
        model.save("./model/probing_velocity")
        del model

    elif sys.argv[1] == "inference":
        
        model = DQN.load("./model/probing_velocity")
        obs = env.reset()
        
        
        
        rewards = []
        time = []
        counter = 0
        
        while True:
            
            action, _states = model.predict(obs, deterministic=True)
            obs, reward, done, info = env.step(action)
            env.render()
            if done:
                input()       
                obs = env.reset()
            
            rewards.append(reward)
            time.append(counter)
            counter += 1
            
            #print(obs[4:])
            print(obs[:4])
            
            # Dynamically Plot Belief
            figure_1.canvas.flush_events()
            belief_plot.cla()
            x = belief_plot.pcolor(env.phi[0], env.phi[1], obs[4:].reshape((utils.rows, utils.rows)))
            #figure_1.colorbar(x)
            #belief_plot.set_xticks([i*utils.graph_gap for i in range(int(utils.rows/utils.graph_gap))])
            #belief_plot.set_xticklabels([r'$\varphi_{'+str(i*utils.graph_gap)+'}$' for i in range(int(utils.rows/utils.graph_gap))])
            #belief_plot.bar(x, obs[4:])
            belief_plot.set_ylabel('$Probability$')
            figure_1.canvas.draw()
            
            # Dynamically Plot KLD
            figure_2.canvas.flush_events()
            kld_plot.cla()
            kld_plot.step(np.array(time)/10, rewards, where='mid')
            kld_plot.set_xlabel('$Time \hspace{1} (s)$')
            kld_plot.set_ylabel('$ Kullback–Leibler \hspace{1} Divergence \hspace{1} (nats)$')
            figure_1.canvas.draw()
            
            
            
            
            


    else:
        print("Invalid Command")
  
    env.close()

