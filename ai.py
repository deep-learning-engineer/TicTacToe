import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F


class CustomLoss(nn.Module):
    def __init__(self):
        super(CustomLoss, self).__init__()

    def forward(self, errors):
        return torch.tensor([errors], requires_grad=True)


class Agent(nn.Module):
    def __init__(self):
        super(Agent, self).__init__()
        self.loss_fn = CustomLoss()
        self.fc1 = nn.Linear(in_features=9, out_features=16)
        self.fc2 = nn.Linear(in_features=16, out_features=16)
        self.fc3 = nn.Linear(in_features=16, out_features=9)
        self.errors = 0.0

    def forward(self, pos):
        x = F.relu(self.fc1(pos))
        x = F.relu(self.fc2(x))
        x = F.softmax(self.fc3(x))
        return x

    def custom_loss(self):
        return self.errors

    #  Обнулить errors!

    def train(self, optimizer):
        #loss = self.cusmot_loss()
        loss = self.loss_fn(self.errors)
        print(loss)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        self.errors = 0.0


# class Population:
#     def __init__(self, n_agents: int = 10):
#         self.population = [Agent() for _ in range(n_agents)]
