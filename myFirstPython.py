import pandas as pd
import numpy as np
### Step 1, create an empty array
np.random.rand(3,3)
#### below development steps

##### Create 2 random arrays
x = 4 * np.random.rand(100)
mu, sigma = 0, 1
y =  2 + 3 * x +  np.random.normal(mu, sigma, 100)

import matplotlib.pyplot as plt

plt.scatter(x, y, alpha=0.5)
plt.title(r"$ y = 2 + 3x + e $")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

from scipy import stats
### Compute the linear relationship
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("The slope is {0:.2f} and the intercept is {1:.2f}".format(slope,
 intercept))


print("hello")