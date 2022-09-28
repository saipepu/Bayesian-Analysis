import numpy as np
import pandas as pd

hypos = 'fast', 'furious'
probs = 0.75,0.25
prior = pd.Series(probs, hypos)
likelihood = 0.26,0.74
unnorm = prior * likelihood
norm = unnorm / unnorm.sum()
fast, furious = norm
print('Probability of Furious involved in the tuk-tuk accident: ',round(furious,5))