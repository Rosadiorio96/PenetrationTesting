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

epsilon = 1.0
epsilonn_min = 0.005
epsilon_decay = 0.993
total_episodes = 50000
max_steps = 50
alpha = 0.05
gamma = 0.95
env = gym.make('gym_pt:pt-v0')
rewards_per_episode = list()

action_size = len(env.action_space)
state_size = env.obs.getShape()[0]
Q = np.zeros((3**state_size, action_size))



def choose_action(state):
    action = 0
    var = random.uniform(0,1)
    print(var)
    if var >epsilon:
        print("NOT Random")
        actionId = np.argmax(Q[state])
        action = generate_action(actionId, env.host) 
    else:
        print("Random")
        n = random.randint(0,10)
        action = env.action_space[n] 
    return action

def update(state, state2, reward, action, action2):
    predict = Q[state, action.id]
    target = reward + gamma * Q[state2, action2.id]
    Q[state, action.id]=Q[state, action.id]+alpha * (target - predict)


reward = 0

for e in range(total_episodes):
    print("EPISODIO ",e)
    t = 0
    state = env.reset()
    action = choose_action(state)
    score = 0
    state1 = copy.copy(state)
    action1 = copy.copy(action)


    """print(state)
    print(action)
    print(action.id)
    print(state1)
    print(action1.id)"""


    for x in range(max_steps):
        """print("step",x)
        print("stat1",state1)
        print(action1)"""
        state2, reward, done, info = env.step(action1)
        
        score += reward


        """print(state)
        print(action)
        print(action.id)

        print(state1)
        print(action1)
        print(action1.id)"""


        action2 = choose_action(state2)


        """print("stat2", state2)
        print(action2)
        print(action2.id)"""

        #update(state1, state2, reward, action1, action2)

        Q[state1, action1.id] = Q[state1, action1.id]+alpha * (reward + gamma * Q[state2, action2.id]-Q[state1, action1.id])
        state1 = copy.copy(state2)
        action1 = copy.copy(action2)
        """print("stat1",state1)
        print(action1)
        input()
        print(state)
        print(action)
        print(action.id)

        print(state1)
        print(action1)
        print(action1.id)

        print(state2)
        print(action2)
        print(action2.id)
        input("")"""

        t+=1
        reward +=1
        score += reward

        if done:
            break 
    if epsilon >=epsilonn_min:
        epsilon *= epsilon_decay

    print("Ricompensa totale", score)
    rewards_per_episode.append(score)      

plt.plot(rewards_per_episode, 'o', color=black)
plt.show()
for e in rewards_per_episode:
    print(e)



