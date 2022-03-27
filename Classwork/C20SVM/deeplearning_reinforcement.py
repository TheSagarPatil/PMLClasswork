import random

class SampleEnvironment :
    def __init__(self) -> None:
        self.steps_left = 20

    def get_observations(self) -> list[float]:
        return [ 0.0, 0.0, 0.0] #radar logic

    def get_actions(self)-> list[int]:
        return [0,1] #left or right

    def is_done(self) -> bool:
        return self.steps_left == 0

    def action(self, action:int ) -> float:
        if self.is_done():
            raise Exception('Game Over')
        self.steps_left -= 1
        return random.random()

class Agent :
    def __init__ (self):
        self.total_reward = 0.0

    def step(self, env : SampleEnvironment):
        """
        Step function accepts enviroment instance
        Observe the env
        make decission about action based on observations
        submit the action to env
        get +- reward for current step
        """
        current_obs = env.get_observations()
        print(f'Observations : {current_obs}')
        action = env.get_actions()
        reward = env.action(random.choice( action ))
        print(f'Action Reward: {reward}')
        self.total_reward += reward
        print(f'Total Reward : {self.total_reward}')

def main():
    print('Reinforcement demo')
    env = SampleEnvironment()
    agent = Agent()
    i = 0
    while not env.is_done():
        i += 1
        print(f'step no {i}')
        agent.step( env )

    print(f'Total Reward achieved : {agent.total_reward}')

if __name__ == '__main__':
    main()
