# https://arxiv.org/abs/1909.10140

import pandas as pd
import numpy as np

n = 100
x = np.random.uniform(-1, 1, n)
y = np.power(x, 2)

# y = x^2
df = pd.DataFrame({"x":x,"y":y})
# ry
df["ry"] = df["y"].rank()
# rx
df = df.sort_values(by='x')

# sum = ∑|ry_{i+1}-ry_{i}|
sum = df["ry"].diff().abs().sum()

# ξ = 1 - 3 * ∑|ry_{i+1}-ry_{i}| / (n^2 - 1)
print(1 - 3 * sum / (pow(n, 2) - 1))