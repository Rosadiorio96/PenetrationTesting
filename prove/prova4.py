from gym_pt.envs.State3 import StateVector
from gym_pt.envs.State2 import State
from gym_pt.envs.Action import *
from gym_pt.envs.Host import *
from scripts.scan.scan_scripts import *
from scripts.config import *
import dirbpy 

import gym
import random
import numpy as np

import matplotlib.pyplot as plt


env = gym.make('gym_pt:pt-v0')

n_episodes = 100
max_iter_episode = 50
exploration_proba = 1
exploration_decreasing_decay = 0.001
min_exploration_proba = 0.01
gamma = 0.99
lr = 0.1
total_rewards_episode = list()

print(env.obs.getShape()[0]) #numero di attributi dello spazio di stato
print(len(env.action_space)) #numero azioni possibili
n_actions = len(env.action_space)
n_observations = env.obs.getShape()[0]
Q_table = np.zeros([n_observations, n_actions]).astype(float)

#print(Q_table[[0, 0, 0, 0, 0, 0,0 ,0,0 ,0, 0, 0, 0, 0, 0], 2])
        
rewards_per_episode = list()

for e in range(n_episodes):
    current_state = env.reset()
    print("NEW EPISODIO")
    done = False
    total_episode_reward = 0

    for i in range(max_iter_episode):

        print("ITER N ",i)

        if np.random.uniform(0,0)<exploration_proba:
            n = random.randint(0,10)
            action = env.action_space[n] 
        else:
            action = np.argmax(Q_table[current_state,:])
        
        next_state, reward, done, _  = env.step(action)
        
        print("REWARD", reward)
        print("DONE",done)
        old_value = Q_table[current_state, action.id]
        #print("OLD", old_value)
        next_max=np.max(Q_table[next_state])
        #print("NEXT MAX",next_max)
        new_value = (1.0-lr)*old_value+lr*(reward+gamma+next_max)
        #print("New value",new_value)
        Q_table[current_state, action.id]=new_value
        #print(Q_table[current_state, action.id])
        
            
        total_episode_reward = total_episode_reward + reward

        if done:
            break
        current_state = next_state

    print("Episodio",e,"ricompensa", total_episode_reward)
    exploration_proba = max(min_exploration_proba, np.exp(-exploration_decreasing_decay*e))
    rewards_per_episode.append(total_episode_reward)


plt.plot(rewards_per_episode)
plt.show()

for e in rewards_per_episode:
    print(e)