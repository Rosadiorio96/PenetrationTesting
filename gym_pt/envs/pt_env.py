import gym
from gym import error, spaces, utils
from gym.utils import seeding
from .State2 import *
from .Host import *
import matplotlib.pyplot as plt

import numpy as np
import copy 
from random import randint

class PTEnv(gym.Env):
    
    stato_corrente = None
    prev_state = None
    host = None
    action_space = None
    num_action = None
    obs = None
    obs_shape = None
    reward = 10
    rewards_per_episode = []
    score = 0
    n = 0
    number = 0
    
    def __init__(self):
        #self.host = Host()
        self.stato_corrente = State()
        self.n = 0
        self.obs = self.stato_corrente.vectorState
        self.action_space = load_action_list()
        self.num_action = len(self.action_space)
        self.obs_shape = self.obs.getShape()
        self.steps = 0
        self.rewards_per_episode = []
        self.number = 0
        self.number2 = 0



    def goal_reached(self, state):
        print("Lo stato dell host",state.get_compromised())
        return state.get_compromised()

    def check_number_scan(self):
        count = 0
        
        for i in range (10,17):
            print(self.stato_corrente.vectorState.vector[i])
            if self.stato_corrente.vectorState.vector[i] != -1:
                count = count +1
        return count

    def calcolaRicompensa1(self, action, result, done):
        if isinstance(action,np.int64) or isinstance(action,int):
            action = generate_action(action)
           
        if action.id != 11 and self.stato_corrente.vectorState.vector[2] == -1:
            reward = -1
        elif action.id == 11 and self.prev_state[2] != -1:
            reward = -1
        elif action.id == 11 and self.prev_state[2] == -1:
            reward = 1
        else:
            if action.is_scanVuln():
                if self.stato_corrente.vectorState.vector[3] == 1:
                    if action.id == 7 and \
                    (self.stato_corrente.vectorState.vector[11] == 1 or \
                    self.stato_corrente.vectorState.vector[12] == 1 or \
                    self.stato_corrente.vectorState.vector[13] == 1 or \
                    self.stato_corrente.vectorState.vector[10] == self.prev_state[10]):
                        reward = -1
                        print("ok1")
                    elif action.id == 8 and \
                    (self.stato_corrente.vectorState.vector[10] == 1 or \
                    self.stato_corrente.vectorState.vector[12] == 1 or \
                    self.stato_corrente.vectorState.vector[13] == 1 or \
                    self.stato_corrente.vectorState.vector[11] == self.prev_state[11]):
                        reward = -1
                        print("ok2")
                        
                    elif action.id == 9 and \
                    (self.stato_corrente.vectorState.vector[11] == 1 or \
                    self.stato_corrente.vectorState.vector[10] == 1 or \
                    self.stato_corrente.vectorState.vector[13] == 1 or \
                    self.stato_corrente.vectorState.vector[12] == self.prev_state[12]):
                        reward = -1
                        print("ok3")
                    elif action.id == 10 and \
                    (self.stato_corrente.vectorState.vector[11] == 1 or \
                    self.stato_corrente.vectorState.vector[12] == 1 or \
                    self.stato_corrente.vectorState.vector[10] == 1 or \
                    self.stato_corrente.vectorState.vector[13] == self.prev_state[13]):
                        reward = -1
                        print("ok4")
                    else:
                        reward=1
                else:
                    reward = -1

            elif action.is_exploit():          
                if action.id == 0:
                    if self.stato_corrente.vectorState.vector[2] == 1 and \
                    self.stato_corrente.vectorState.vector[14] == 1:
                        n = self.check_number_scan()
                        reward = 5 - n
                        print("Numero scan",n)
                        
                    else:
                        reward = -1
                        
                        
                elif action.id == 1:
                    if self.stato_corrente.vectorState.vector[3] == 1 and self.stato_corrente.vectorState.vector[10] == 1:
                        n = self.check_number_scan()
                        reward = 5 - n
                        print("Numero scan",n)                     
                    else:
                        reward = -1

                elif action.id == 2:
                    if self.stato_corrente.vectorState.vector[5] == 1 and \
                    self.stato_corrente.vectorState.vector[14] == 1 :
                        n = self.check_number_scan()
                        reward = 5 - n
                        print("Numero scan",n)
                        
                    else:
                        reward = -1
                elif action.id == 3:
                    if self.stato_corrente.vectorState.vector[3] == 1 and self.stato_corrente.vectorState.vector[13] == 1:
                        n = self.check_number_scan()
                        reward = 5 - n
                        print("Numero scan",n)
                        
                        
                    else:
                        reward = -1
                elif action.id == 4:
                    if self.stato_corrente.vectorState.vector[3] == 1 and self.stato_corrente.vectorState.vector[12] == 1:
                        n = self.check_number_scan()
                        reward = 5 - n
                        print("Numero scan",n)
                        
                        
                    else:
                        reward = -1
                elif action.id == 5:
                    if self.stato_corrente.vectorState.vector[3] == 1 and self.stato_corrente.vectorState.vector[11] == 1:
                        n = self.check_number_scan()
                        reward = 5 - n
                        print("Numero scan",n)
                        
                        
                    else:
                        reward = -1
                elif action.id == 6:
                    if self.stato_corrente.vectorState.vector[4] == 1 and \
                    self.stato_corrente.vectorState.vector[14] == 1:
                        n = self.check_number_scan()
                        reward = 5 - n
                        print("Numero scan",n)
                    
                    else:
                        reward = -1
        print("reward calcolata",reward)
        print(self.prev_state)
        print(self.stato_corrente.vectorState.vector)
        #input("Check")
        return reward

 
    def calcolaRicompensa2(self, action, result, done):
        if isinstance(action,np.int64) or isinstance(action,int):
            action = generate_action(action)
           
        if action.id != 11 and self.stato_corrente.vectorState.vector[2] == -1:
            reward = -1
        elif action.id == 11 and self.prev_state[2] != -1:
            reward = -1
        elif action.id == 11 and self.prev_state[2] == -1:
            reward = 1
        else:
            if action.is_scanVuln():
                if action.id == 7 and (self.stato_corrente.vectorState.vector[3] != 1 or \
                self.stato_corrente.vectorState.vector[11] == 1 or \
                self.stato_corrente.vectorState.vector[12] == 1 or \
                self.stato_corrente.vectorState.vector[13] == 1 or \
                self.stato_corrente.vectorState.vector[10] == self.prev_state[10]):
                    reward = -1
                    print("ok1")
                elif action.id == 8 and (self.stato_corrente.vectorState.vector[3] != 1 or \
                self.stato_corrente.vectorState.vector[10] == 1 or \
                self.stato_corrente.vectorState.vector[12] == 1 or \
                self.stato_corrente.vectorState.vector[13] == 1 or \
                self.stato_corrente.vectorState.vector[11] == self.prev_state[11]):
                    reward = -1
                    print("ok2")
                    
                elif action.id == 9 and (self.stato_corrente.vectorState.vector[3] != 1 or \
                self.stato_corrente.vectorState.vector[11] == 1 or \
                self.stato_corrente.vectorState.vector[10] == 1 or \
                self.stato_corrente.vectorState.vector[13] == 1 or \
                self.stato_corrente.vectorState.vector[12] == self.prev_state[12]):
                    reward = -1
                    print("ok3")
                elif action.id == 10 and (self.stato_corrente.vectorState.vector[3] != 1 or \
                self.stato_corrente.vectorState.vector[11] == 1 or \
                self.stato_corrente.vectorState.vector[12] == 1 or \
                self.stato_corrente.vectorState.vector[10] == 1 or \
                self.stato_corrente.vectorState.vector[13] == self.prev_state[13]):
                    reward = -1
                    print("ok4")
                elif action.id == 12 and (self.stato_corrente.vectorState.vector[5] != 1 or \
                self.stato_corrente.vectorState.vector[11] == 1 or \
                self.stato_corrente.vectorState.vector[12] == 1 or \
                self.stato_corrente.vectorState.vector[10] == 1 or \
                self.stato_corrente.vectorState.vector[13] == 1 or \
                self.stato_corrente.vectorState.vector[14] == 1 or \
                self.stato_corrente.vectorState.vector[15] == 1 or \
                self.stato_corrente.vectorState.vector[16] == self.prev_state[16]):
                    print("OK66")
                    reward = -1
                elif action.id == 13 and (self.stato_corrente.vectorState.vector[4] != 1 or \
                self.stato_corrente.vectorState.vector[11] == 1 or \
                self.stato_corrente.vectorState.vector[12] == 1 or \
                self.stato_corrente.vectorState.vector[10] == 1 or \
                self.stato_corrente.vectorState.vector[13] == 1 or \
                self.stato_corrente.vectorState.vector[14] == 1 or \
                self.stato_corrente.vectorState.vector[16] == 1 or \
                self.stato_corrente.vectorState.vector[15] == self.prev_state[15]):
                    reward = -1
                    print("OKrr")
                elif action.id == 14 and (self.stato_corrente.vectorState.vector[2] != 1 or \
                self.stato_corrente.vectorState.vector[11] == 1 or \
                self.stato_corrente.vectorState.vector[12] == 1 or \
                self.stato_corrente.vectorState.vector[10] == 1 or \
                self.stato_corrente.vectorState.vector[13] == 1 or \
                self.stato_corrente.vectorState.vector[16] == 1 or \
                self.stato_corrente.vectorState.vector[15] == 1 or \
                self.stato_corrente.vectorState.vector[14] == self.prev_state[14]):
                    reward = -1
                    print("OK66l")
                else:
                    reward=1
            
            elif action.is_exploit():          
                if action.id == 0:
                    if self.stato_corrente.vectorState.vector[2] == 1 and \
                    self.stato_corrente.vectorState.vector[14] == 1:
                        n = self.check_number_scan()
                        reward = 8 - n
                        print("Numero scan",n)
                        
                    else:
                        reward = -1                 
                elif action.id == 1:
                    if self.stato_corrente.vectorState.vector[3] == 1 and self.stato_corrente.vectorState.vector[10] == 1:
                        n = self.check_number_scan()
                        reward = 8 - n
                        print("Numero scan",n)                     
                    else:
                        reward = -1

                elif action.id == 2:
                    if self.stato_corrente.vectorState.vector[5] == 1 and \
                    self.stato_corrente.vectorState.vector[16] == 1:
                        n = self.check_number_scan()
                        reward = 8 - n
                        print("Numero scan",n)
                        
                    else:
                        reward = -1
                elif action.id == 3:
                    if self.stato_corrente.vectorState.vector[3] == 1 and self.stato_corrente.vectorState.vector[13] == 1:
                        n = self.check_number_scan()
                        reward = 8 - n
                        print("Numero scan",n)
                        
                        
                    else:
                        reward = -1
                elif action.id == 4:
                    if self.stato_corrente.vectorState.vector[3] == 1 and self.stato_corrente.vectorState.vector[12] == 1:
                        n = self.check_number_scan()
                        reward = 8 - n
                        print("Numero scan",n)
                        
                        
                    else:
                        reward = -1
                elif action.id == 5:
                    if self.stato_corrente.vectorState.vector[3] == 1 and self.stato_corrente.vectorState.vector[11] == 1:
                        n = self.check_number_scan()
                        reward = 8 - n
                        print("Numero scan",n)
                                 
                    else:
                        reward = -1
                elif action.id == 6:
                    if self.stato_corrente.vectorState.vector[4] == 1 and \
                    self.stato_corrente.vectorState.vector[15] == 1:
                        n = self.check_number_scan()
                        reward = 8 - n
                        print("Numero scan",n)
                    
                    else:
                        reward = -1
        print("reward calcolata",reward)
        print(self.prev_state)
        print(self.stato_corrente.vectorState.vector)
        #input("Check")
        return reward

 
    
    def step(self, action):
        
        self.steps +=1
        self.prev_state = copy.copy(self.stato_corrente.vectorState.vector)
        result, next_state = self.host.perform_action(self.stato_corrente, action)
        done = self.goal_reached(next_state)

       
        self.reward = self.calcolaRicompensa2(action, result, done)
        print("Reward", self.reward)
        self.score += self.reward
        if done == True:
            
            self.rewards_per_episode.append(self.score)
        
        return next_state.vectorState.vector, float(self.reward), done, {}
        
    def find_target(self):
        #CASO 0
        #L'agente si allena su una sola macchina
        """RHOST = "RHOST0"""
        
        #CASO 1
        #L'AGENTE SI ALLENA SU 6 MACCHINE, CIASCUNA CON
        #UNA PORTA E UNA VULNERABILITA

        return "RHOST15"

        var = "RHOST"+str(self.number2)
        self.number2 += 1
        if self.number2 == 14:
            self.number2=0
        return var

        return "RHOST16"
        

        """print("Rosa",self.steps)
        if self.steps < 42668:
            print("ok")
            if self.number2 == 6:
                self.number2 +=1
            var = "RHOST"+str(self.number2)
            self.number2 += 1
            if self.number2 == 18:
                self.number2 = 0
            return var
        else:
            print("ok2")
            input()
            return "RHOST19"""

        
        
        """return "RHOST5"

        print("ok")
        var = "RHOST"+str(self.number2)
        self.number2 += 1
        if self.number2 == 18:
            self.number2 = 0
        return var"""
        

        
        """"
        print("NSTEP",self.steps)
        if episode == None:
            if self.steps >1999:
                return "RHOST16" 
  
            n_random = randint(0,12)
                #n_random = 1
            return "RHOST"+str(n_random)
        else:
            if episode >300:
                return "RHOST16" 
            else:
                n_random =  randint(0,5)
                return "RHOST"+str(n_random)


        if self.n <6:
            RHOST = "RHOST"+str(self.n)
            self.n +=1
        else:
            self.n = 0
            RHOST = "RHOST"+str(self.n)
            self.n +=1"""

        #CASO 2
        #L'AGENTE SI ALLENA SU MACCHINE AVENTI PIU'
        #PORTE APERTE MA UNA SOLA VULNERABILITA'





    def reset(self):
        #self.steps = 0
        self.reward = 0
        self.score = 0

        HOST_TARGET=self.find_target()
        print("NEW TARGET: ", HOST_TARGET)
        self.host = Host(HOST_TARGET, conf_host[HOST_TARGET]['IP'])
        self.stato_corrente.generete_initial_state()
        self.stato_corrente.vectorState.generate_initial_vector()
        #self.stato_corrente.set_initial_state(HOST_TARGET)
        
        return self.stato_corrente.vectorState.vector
    
    def render(self, mode = "human"):
        
        plt.plot(self.rewards_per_episode)
        plt.xlabel("Episodi")
        plt.ylabel("Ricompensa cumulativa")
        plt.show()
        return copy.copy(self.rewards_per_episode)
    

    def close(self):
        pass