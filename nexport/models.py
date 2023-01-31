# Module imports
import torch
from torch import nn

# External function visibility
__all__ = ['FFNetwork', 'BFNetwork', 'ICARNetwork', 'XORNetwork']


# Model classes

class FFNetwork(nn.Module):
    def __init__(self):
        super(FFNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential( # 25 parameters
            nn.Linear(2, 3), # 6 weights, 3 biases
            nn.ReLU(),
            nn.Linear(3, 3), # 9 weights, 3 biases
            nn.ReLU(),
            nn.Linear(3, 1) # 3 weights, 1 bias
        )


class BFNetwork(nn.Module):
    def __init__(self):
        super(BFNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 8)
        )


class ICARNetwork(nn.Module):
    def __init__(self):
        super(ICARNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(10, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 10)
        )


class XORNetwork(nn.Module):
    def __init__(self):
        super(XORNetwork, self).__init__()
        self.flatten = nn.Flatten()
        
        firstlayer = nn.Linear(2, 3)
        firstlayer.weight.data = XORNetwork.first_weights
        firstlayer.bias.data = XORNetwork.first_biases
        
        secondlayer = nn.Linear(3, 3)
        secondlayer.weight.data = XORNetwork.second_weights
        secondlayer.bias.data = XORNetwork.second_biases
        
        thirdlayer = nn.Linear(3, 1)
        thirdlayer.weight.data = XORNetwork.third_weights
        thirdlayer.bias.data = XORNetwork.third_biases
        
        self.linear_step_stack = nn.Sequential(
            firstlayer,
            XORNetwork.StepHS(),
            secondlayer,
            XORNetwork.StepHS(),
            thirdlayer,
            XORNetwork.StepHS()
        )

    # Network parameters
    ## Hidden layer 1
    first_weights = torch.tensor([[1.0, 0.0],
                                [1.0, 1.0],
                                [0.0, 1.0]])
    first_biases = torch.tensor([0.0, -1.99, 0.0])

    ## Hidden layer 2
    second_weights = torch.tensor([[1.0, 0.0, 0.0],
                                [0.0, 1.0, 0.0],
                                [0.0, 0.0, 1.0]])
    second_biases = torch.tensor([0.0, 0.0, 0.0])

    ## Output layer
    third_weights = torch.tensor([[1.0, -2.0, 1.0]])
    third_biases = torch.tensor([0.0])

    # Binary step activation function
    class StepHS(nn.Module):
        def __init__(self):
            super().__init__()
            
        def forward(self, input):
            output = torch.heaviside(input, torch.zeros(input.shape[0]))
            return torch.Tensor(output)
        
    # Forward function (matmul with activation function)
    def forward(self, input):
        return self.linear_step_stack(input)

    
        

