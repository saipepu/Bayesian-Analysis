import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

hypos = 'bucket a', 'bucket b', 'bucket c'
probs = 1/3,1/3,1/3

prior = pd.Series(probs, hypos)
print(prior)

likelihood = 3/4, 1/2, 4/5

#posterior
unnorm = prior * likelihood
print(unnorm)

norm = unnorm / unnorm.sum()
print(norm)

norm.plot()
# plt.show()