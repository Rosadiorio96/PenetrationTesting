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
import numpy as np


env = gym.make('gym_pt:pt-v0')

action_size = len(env.action_space)
state_size = env.obs.getShape()[0]

qtable = np.zeros((3**state_size, action_size))

epsilon = 1.0
epsilonn_min = 0.005
epsilon_decay = 0.99993
episodes = 50000
max_steps = 50
learning_rate = 0.65
gamma = 0.65

rewards_per_episode = list()

for e in range(episodes):
    print("Nuovo episodio", e)
    state = env.reset()
    print(state)
    done = False
    score = 0.0
    for x in range(max_steps):
        print("Step ", x)
        if random.uniform(0,1)>epsilon:
            """print("OOOOO")
            print(qtable[state,:])
            action_id = np.argmax(qtable[state,:])
            print(action_id)"""
            ind = np.unravel_index(np.argmax(qtable[state,:], axis=None), qtable.shape)
            print("Not random")
            action = generate_action(ind[1], env.host)   
        else:
            print("Random")
            n = random.randint(0,10)
            action = env.action_space[n]  

        next_state, reward, done, info = env.step(action)
        print("Reward", reward)
            
        
        score += reward
        
        
        qtable[state, action.id]=(1-learning_rate)*qtable[state, action.id]+learning_rate*(reward+gamma*np.max(qtable[next_state, :]))

        state = next_state

        if done:
            break

    if epsilon >=epsilonn_min:
        epsilon *= epsilon_decay
    

    print("Ricompensa totale", score)
    rewards_per_episode.append(score)

    #input("Premi un carattere per continuare")

plt.plot(rewards_per_episode)
plt.show()
for e in rewards_per_episode:
    print(e)