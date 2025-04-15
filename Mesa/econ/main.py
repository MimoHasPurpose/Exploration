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
    
    def say_hi(self):
         print(f"Hi, I am an agent, you can call me cutie no: {self.unique_id!s}.")
    
    def say_wealth(self):
        print(f"Hi boss am{self.unique_id!s} my wealth is huhuhu only: {self.wealth}")
         



class MoneyModel(mesa.Model):
    def __init__(self,n,seed=42):
        super().__init__(seed=seed)
        self.num_agents=n 
        MoneyAgent.create_agents(model=self, n=n)

    def step(self):
        self.agents.do("say_wealth")
        self.agents.do("say_hi")


starter_model = MoneyModel(5)
starter_model.step()