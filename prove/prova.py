import gym
import random


env = gym.make('gym_pt:pt-v0')

#print(env.observation_space.shape[0])
#print(env.action_space.n)
plot_model(model, to_file="Model_plot.png", show_shapes=True, show_layer_names=True)
from keras.utils.vis_utils import plot_model
for episode in range(20):
    #state = env.reset()
    done = False
    score = 0
    while not done:
        n = random.randint(0,10)
        action = env.action_space[n]
        print("Action", type(action))
        result, next_state, done, reward = env.step(action)
        score+=reward
    print('Episode:{} Score:{}'.format(episode,))


