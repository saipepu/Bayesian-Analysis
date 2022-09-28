import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

hypos = '2003','2004','2005','2006','2007','2008','2009','2010','2016','2017','2018'
probs = 1/11,1/11,1/11,1/11,1/11,1/11,1/11,1/11,1/11,1/11,1/11

prior = pd.Series(probs, hypos)
print(prior)

likelihood = 0.5,0.5,0.7,0.82,0.84,0.83,0.85,0.86,0.7,0.68,0.65

unnorm = prior * likelihood
print(unnorm)

norm = unnorm / unnorm.sum()
print(norm)

norm.plot()
plt.show()