import numpy as np 
import matplotlib.pyplot as plt 
import networkx as nx 
import random as rndm 

class Nueron:
    def  dot(self, v1, v2):
        output = 0
        if type(v1) is list:
            for v in v1:
                output += v  * v2[v1.index(v)]
        else:
            output += v1 * v2

    def __init__(self, inputs, weights, bias):
        self.inputs = inputs
        self.weights = weights
        self.activation_function = ""
        self.error = error

    def change_activation_function(self, activation_function: str) -> None:
        self.activation_function = activation_function

    def change_inputs(self, inputs: [float]) -> None:
        self.inputs = inputs

    def change_bias(self, bias: float) -> None:
        self.bias = bias 

    def change_error(self, error) -> None:
        self.error = error

    def get_output(self) -> float:
        transposed_weights = self.weights
        reference_inputs = self.inputs
        output = self.dot(reference_inputs, transposed_weights) + self.bias
        return ouput