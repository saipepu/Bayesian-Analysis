import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

hypos = 'gender','race','working for wage','working without wage','salary period','residence type','marital status','education status'
probs = 1/8,1/8,1/8,1/8,1/8,1/8,1/8,1/8
likelihood = 0.3545,0.1170,0.0233,0.1052,0.0665,0.2478,0.1702,0.250
prior = pd.Series(probs,hypos)
def posterior_probability(hypos, probs,likelihood):
  prior = pd.Series(probs, hypos)
  unnorm = prior * likelihood
  norm = unnorm / unnorm.sum()
  return norm

posterior = posterior_probability(hypos, probs, likelihood)

print(type(posterior))
# print(pd.Series(posterior).array)
print(posterior.array)
# posterior.plot()
# plt(posterior,likelihood)
plt.plot(hypos, posterior.array)
plt.plot(hypos, likelihood)
plt.plot(hypos, prior)
plt.title('Bayesian Analysis on Rate of Diabetes in South Africa,Eastern Cape(EC) province')
plt.xlabel('Hypothesis')
plt.ylabel('posterior outcomes')
plt.show()