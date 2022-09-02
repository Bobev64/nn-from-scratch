import numpy as np

a = np.random.randint(10, size=3)
b = np.random.randint(10, size=3)

dot = 0

for a_num, b_num in zip(a,b):
    dot += a_num * b_num

print(f"Vector A: {a}\nVector B: {b}\nDot Product: {dot}")
