import numpy as np
import time


"""
Takes number of neurons you want as input, outputs based on randomly generated inputs (unless otherwise specified) and weights.
"""

def neuron(num_of_neurons, inputs=None): 

    output = []

    if inputs == None:
        inputs = np.random.randint(10, size=3)
        print(f"Inputs: {inputs}")

    np.random.seed(seed=int(time.time()))
    for i in range(num_of_neurons): 
        bias = np.random.randint(9)
        weights = np.random.random_sample(3)
        mat_mul = inputs @ weights
        
        output.append(mat_mul + bias)

        print(f"Info for neuron {i}:\nweights: {weights}\nbias: {bias}\n")
    return output



if __name__ == "__main__":
    total_neurons = 3
    output = neuron(total_neurons)
    print(f"Total Outputs: {output}\n")
