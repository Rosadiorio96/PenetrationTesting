# File: run_agent.py
# Description: Running algorithm
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# Valentyn N Sichkar. Reinforcement Learning Algorithms for global path planning // GitHub platform. DOI: 10.5281/zenodo.1317899
from gym_pt.envs.State3 import StateVector
from gym_pt.envs.State2 import State
from gym_pt.envs.Action import *
from gym_pt.envs.Host import *
from scripts.scan.scan_scripts import *

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras import Input
from tensorflow.keras.optimizers import Adam
from tensorflow import keras

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy,LinearAnnealedPolicy ,EpsGreedyQPolicy, GreedyQPolicy
from rl.memory import SequentialMemory
from keras.metrics import Precision, Recall
from keras.utils.vis_utils import plot_model
import rl
import dirbpy 

import random
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import copy

import gym

# Importing classes

from agent_brain2 import QLearningTable
from agent_brain_Sarsa2 import SarsaTable





def Q_Learning():
    env = gym.make('gym_pt:pt-v0')

    RL = QLearningTable(actions=list(range(len(env.action_space))))

    print("Q_Learning")
    steps = []
    rewards_per_episode = list()
    all_costs = []

    for episode in range(400):
        print("Episodio",episode)
        observation = env.reset()
        i = 0
        cost = 0
        score = 0.0
        while True:
            print("STEP", i)
            prev_state = copy.copy(observation)
            actionId = RL.choose_action(str(observation), episode)
            action = generate_action(actionId)
            observation_, reward, done, _ = env.step(action)
            score += reward
            cost += RL.learn(str(prev_state), action.id, reward, str(observation_))
            observation = observation_
            i += 1
            if done:
                steps += [i]
                all_costs += [cost]
                break
        
        print("Ricompensa Totale", score)
        
        """ if episode < 195:
            print("Ricompensa inserita")
            """
        rewards_per_episode.append(score)
        
        
    Q_Learning_R = env.render()

    
    
    
    
    #RL.plot_results(steps, all_costs)

    return Q_Learning_R 

def SARSA():
    
    print("SARSA")
    env = gym.make('gym_pt:pt-v0') 
    steps = []
    RL = SarsaTable(actions=list(range(len(env.action_space))))
   
    all_costs = []
    rewards_per_episode = list()

    for episode in range(400):
        print("New Episodio", episode)
        observation = env.reset()

        i = 0

        cost = 0

        actionId = RL.choose_action(str(observation), episode)
        action = generate_action(actionId)
        score = 0
        while True:
            
            print("Step", i)
            
            prev_state = copy.copy(observation)
            prev_action = copy.copy(action)

            observation_, reward, done, _ = env.step(prev_action)
            print("Reward", reward)
            action_Id = RL.choose_action(str(observation_), episode)
            action_ = generate_action(action_Id)
       
            cost += RL.learn(str(prev_state), prev_action.id, reward, str(observation_), action_.id)

            observation = observation_
            action = action_
            score += reward
            
            i += 1
            if done:
                steps += [i]
                all_costs += [cost]
                break

        """if episode < 195:
            print("Ricompensa inserita")
            """
        rewards_per_episode.append(score)
        print("Reward totale", score)
    
    SARSA_R = env.render()
    
   

    #RL.plot_results(steps, all_costs)
    return SARSA_R

def DQN():
    env = gym.make('gym_pt:pt-v0')

    action_size = len(env.action_space)
    np.random.seed(123)
    env.seed(123)
    nb_actions = len(env.action_space)
    var = env.obs.getShape()

    model = Sequential()
    model.add(Flatten(input_shape=(1,env.obs.getShape(),)))
    model.add(Dense(200, activation="relu"))
    model.add(Dense(200, activation="relu"))
    model.add(Dense(200, activation="relu"))
    """  model.add(Dense(var, activation="relu"))
    model.add(Dense(var, activation="relu"))
    model.add(Dropout(0.1))"""
    model.add(Dense(nb_actions, activation="softmax"))

    print(model.summary())
    plot_model(model, to_file="Model_plot.png", show_shapes=True, show_layer_names=True)

    memory = SequentialMemory(limit=50000, window_length=1)
    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=0.05, value_min=1e-9, value_test=0.005, nb_steps=1000)
    
    dqn = DQNAgent( model=model, policy = policy, memory=memory, nb_actions=nb_actions,  nb_steps_warmup=5,target_model_update=1e-12)
    dqn.compile(optimizer=Adam(learning_rate=0.0005), metrics=['mae'])
    """
    optimizer = tf.keras.optimizers.Adam(learning_rate=1e-3)
    agent = dqn_agent.DqnAgent(env.)
    agent.initialize()
   
    """

    dqn.fit(env, visualize=False, verbose=1, nb_max_episode_steps=50, nb_steps = 2000)
    
    dqn.save_weights('dqn_weights_nhosts-testNO.h5', overwrite=True)

    dqn.test(env, nb_episodes=10,nb_max_episode_steps=20, visualize=False)

    DQN_R = env.render()
    print("Numero episodi", len(DQN_R))
    
    return DQN_R

def SARSADeep():
    env = gym.make('gym_pt:pt-v0')

    action_size = len(env.action_space)
    np.random.seed(123)
    env.seed(123)
    nb_actions = len(env.action_space)
    var = env.obs.getShape()

    model = Sequential()
    model.add(Flatten(input_shape=(1,env.obs.getShape(),)))
    model.add(Dense(200, activation="relu"))
    model.add(Dense(200, activation="relu"))
    model.add(Dense(200, activation="relu"))
    """  model.add(Dense(var, activation="relu"))
    model.add(Dense(var, activation="relu"))
    model.add(Dropout(0.1))"""
    model.add(Dense(nb_actions, activation="linear"))

    print(model.summary())
    plot_model(model, to_file="Model_plot.png", show_shapes=True, show_layer_names=True)

    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=0.05, value_min=1e-9, value_test=0.005, nb_steps=5000)
    
    #policy = BoltzmannQPolicy()
    sarsa = rl.agents.sarsa.SARSAAgent(model=model, nb_actions=nb_actions, policy=policy, test_policy=GreedyQPolicy(), gamma=0.0005, nb_steps_warmup=10, train_interval=1, delta_clip=np.inf)
    sarsa.compile(Adam(learning_rate=0.0005), metrics=['mae'])
    

    sarsa.fit(env, visualize=False, verbose=1, nb_max_episode_steps=30, nb_steps = 6000)
    sarsa.save_weights('sarsa__weights_nhosts-testNO.h5', overwrite=True)
    sarsa.test(env, nb_episodes=20, nb_max_episode_steps=20, visualize=False)

    sarsa_deep = env.render()
    print("Numero episodi", len(sarsa_deep))
    return sarsa_deep
if __name__ == "__main__":
    
    SARSA_R = SARSA()
    Q_Learning_R = Q_Learning()
    SARSADeep()
    DQN_R = DQN()
    
    
    

    
    
    
    
    
   
    

    