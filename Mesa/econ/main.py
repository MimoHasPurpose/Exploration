# Boltzman wealth model 

import numpy as np
import pandas as pd
import seaborn as sns
import mesa

#defining agent
class MoneyAgent(mesa.Agent):
    def __init__(self,model):
        super().__init__(model)
        self.wealth=1
    
    def exchange(self):
        if self.wealth>0:
            other_agent=self.random.choice(self.model.agents)
            if other_agent is not None:
                other_agent.wealth+=1
                self.wealth-=1

    def say_wealth(self):
        print(f"Hi boss am {self.unique_id!s} my wealth is huhuhu only: {self.wealth} ")
         



class MoneyModel(mesa.Model):
    def __init__(self,n):
        super().__init__()
        self.num_agents=n 
        MoneyAgent.create_agents(model=self, n=n)

    def step(self):
        self.agents.do("say_wealth")
        self.agents.shuffle_do("exchange")


all_wealth = []
# This runs the model 100 times, each model executing 10 steps.
for _ in range(10):
    # Run the model
    model = MoneyModel(10)
    for _ in range(30):
        model.step()

    # Store the results
    for agent in model.agents:
        all_wealth.append(agent.wealth)

import matplotlib.pyplot as plt

# Use seaborn
g = sns.histplot(all_wealth, discrete=True)
g.set(title="Wealth distribution", xlabel="Wealth", ylabel="number of agents")
plt.show()