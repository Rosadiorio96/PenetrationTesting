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
import copy

env = gym.make('gym_pt:pt-v0')

action_size = len(env.action_space)
state_size = env.obs.getShape()[0]
print(3**state_size)
qtable = np.zeros((3**state_size, action_size))

epsilon = 1
epsilonn_min = 0.005
epsilon_decay = 0.9999
episodes = 100000
max_steps = 50
learning_rate = 0.45
gamma = 0.65

rewards_per_episode = list()

for e in range(episodes):
    print("Nuovo episodio", e)
    state = env.reset()
    print("stato iniziale", state)
    done = False
    score = 0.0
    for x in range(max_steps):
        print("Step ", x)
        prev_state = copy.copy(state)

        if random.uniform(0,1)>epsilon:
            print("Not random action")
            actionId = np.argmax(qtable[prev_state])
            action = generate_action(actionId)   
        else:
            print("Random Action")
            n = random.randint(0,10)
            action = env.action_space[n]
        

          
        
        next_state, reward, done, info = env.step(action)
        print("ricompensa", reward)
            
        
        score += reward
        
        
        qtable[prev_state, action.id]=(1-learning_rate)*qtable[prev_state, action.id]+learning_rate*(reward+gamma*np.max(qtable[next_state, :]))
        
        rows, cols = np.nonzero(qtable)
        print("R",rows)
        print("C",cols)
        print("QQQ",qtable[rows, cols])
        print("QQQ",qtable[rows, :])
        input()
        prev_state = next_state

        if done:
            break

    if epsilon >=epsilonn_min:
        epsilon *= epsilon_decay
        print(epsilon)

    print("Ricompensa totale episodio", score)

    print("Ricompensa totale", score)
    rewards_per_episode.append(score)

    #input("Premi un carattere per continuare")

plt.plot(rewards_per_episode)
plt.show()
for e in rewards_per_episode:
    print(e)

rows, cols = np.nonzero(qtable)
print(qtable[rows, cols])