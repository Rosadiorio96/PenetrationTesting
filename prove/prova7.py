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

rewards_per_episode = list()



alpha = 0.1
gamma = 0.6
epsilon = 0.1
max_steps = 50

for i in range(1, 100000):
    print("Episodio", i)
    state = env.reset()

    epochs = 0
    penalties, reward = 0,0
    score = 0
    done = False

    for x in range(max_steps):
        print("Step",x)
        old_state = copy.copy(state)

        if random.uniform(0,1)>epsilon:
            actionId = np.argmax(qtable[old_state])
            
            action = generate_action(actionId, env.host) 
        else:
            print("Random")
            n = random.randint(0,10)
            action = env.action_space[n] 

        next_state, reward, done, info = env.step(action)
        print(reward)
        score += reward
        old_value = qtable[old_state, action.id]

        next_max = np.max(qtable[next_state])

        new_value = (1-alpha)*old_value + alpha *(reward+gamma*next_max)
        qtable[old_state, action.id] = new_value

        epochs +=1

        if done:
            break

    print("Ricompensa totale", score)
    rewards_per_episode.append(score)

plt.plot(rewards_per_episode)
plt.show()
for e in rewards_per_episode:
    print(e)






