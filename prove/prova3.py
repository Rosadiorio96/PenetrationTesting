from gym_pt.envs.State3 import StateVector
from gym_pt.envs.State2 import State
from gym_pt.envs.Action import *
from gym_pt.envs.Host import *
from scripts.scan.scan_scripts import *
from scripts.config import *
import dirbpy 

import gym
import random


env = gym.make('gym_pt:pt-v0')

print(env.obs.getShape()[0]) #numero di attributi dello spazio di stato
print(len(env.action_space)) #numero azioni possibili
n_actions = len(env.action_space)
n_observations = env.obs.getShape()[0]
Q_table = np.zeros((n_observations, n_actions))

for t in range(100):
    v = random.randint(0,n-1)
    action = env.action_space[v]
    print("Action", type(action))

host = Host(RHOST)
s = State()
port = s.get_ports()
print(port)
services = s.get_services()
print(services)
s.set_initial_state(RHOST)
port = s.get_ports()
print(port)
services = s.get_services()
print(services)
print(s.vectorState.vector)

scanAction = scanVuln(7, RHOST, "wordpress", "oracle", 1, 1)
host.perform_action(s, scanAction)
vuln = s.get_vulnerabilities()

print("******************************************")

scanAction = scanVuln(8, RHOST, "wordpress", "oracle", 1, 1)
host.perform_action(s, scanAction)
vuln = s.get_vulnerabilities()

print("******************************************")

scanAction = scanVuln(9, RHOST, "wordpress", "oracle", 1, 1)
host.perform_action(s, scanAction)
vuln = s.get_vulnerabilities()

print("******************************************")

scanAction = scanVuln(10, RHOST, "wordpress", "oracle", 1, 1)
host.perform_action(s, scanAction)
vuln = s.get_vulnerabilities()
print(s.vectorState.vector)
print(s.vectorState.getShape())



