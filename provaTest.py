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
import rl
from rl.agents.dqn import DQNAgent
from rl.agents.sarsa import SARSAAgent
from rl.policy import BoltzmannQPolicy,LinearAnnealedPolicy ,EpsGreedyQPolicy,  GreedyQPolicy
from rl.memory import SequentialMemory
from keras.metrics import Precision, Recall
from keras.utils.vis_utils import plot_model
from math import inf 
import dirbpy 

import random
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import copy

import gym

# Importing classes

from agent_brain import QLearningTable
from agent_brain_Sarsa import SarsaTable

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
    model.add(Dense(nb_actions, activation="linear"))

    print(model.summary())
    plot_model(model, to_file="Model_plot.png", show_shapes=True, show_layer_names=True)

    memory = SequentialMemory(limit=50000, window_length=1)
    
    dqn = DQNAgent( model = model, policy = EpsGreedyQPolicy(), memory=memory, nb_actions=nb_actions,  nb_steps_warmup=5,target_model_update=1e-12)
    
    dqn.compile(optimizer=Adam(learning_rate=0.0005), metrics=['mae'])

    dqn.load_weights("dqn_weights_nhosts.h5")
    
    test_results = dqn.test(env, nb_episodes=4,nb_max_episode_steps=20, visualize=False)
    
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

    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1, value_min=5e-9, value_test=0.005, nb_steps=1000)
    #policy = BoltzmannQPolicy()
    sarsa = rl.agents.sarsa.SARSAAgent(model=model, nb_actions=nb_actions, policy=policy, test_policy=GreedyQPolicy(), gamma=1, nb_steps_warmup=10, train_interval=1, delta_clip=np.inf)
    sarsa.compile(Adam(learning_rate=0.0009), metrics=['mae'])
    

    sarsa.load_weights("sarsa__weights_nhosts.h5")

    sarsa.test(env, nb_episodes=4,nb_max_episode_steps=20, visualize=False)

    sarsa_deep = env.render()
    print("Numero episodi", len(sarsa_deep))
    
    return sarsa_deep

if __name__ == "__main__":
    
    DQN_R = DQN()
    SARSA_Deep = SARSADeep()
    """ 
    
    #SARSA_Deep = SARSADeep()
    SARSA_R = SARSADeep()
    
    
    
    plt.plot(DQN_R, c='black')
    plt.plot(SARSA_R, c='red')
    plt.show()
    
    
    plt.plot(DQN_R[:500], c='black')
    plt.plot(SARSA_Deep[:500], c='red')
    plt.show()
    plt.plot(Q_Learning_R[:500], c='green')
    plt.plot(SARSA_R[:500], c='red')
    plt.plot(DQN_R[:500], c='black')
    plt.plot(SARSA_Deep[:500], c='blue')
    plt.show()"""
    