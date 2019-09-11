import pandas as pd
import numpy as np
### Step 1, create an empty array
np.random.rand(3,3)
#### below development steps

##### Create 2 random arrays
x = 4 * np.random.rand(100)
mu, sigma = 3, 3
y =  2 + 3 * x +  np.random.normal(mu, sigma, 100)

import matplotlib.pyplot as plt

plt.scatter(x, y, alpha=0.5)
plt.title(r"$ y = 2 + 3x + e $")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
