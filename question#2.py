from statsmodels.stats.proportion import proportions_ztest,proportion_confint
from scipy.stats import t
import numpy as np

data = [6, -4, 1,2,-3,0,-7,1,-2,5]
# I assume this is the differences from mobile to laptop
# thus the positive number will represent that mobile gets a higher rate
count = 5 # 5 people rate mobile is better
total = len(data)
# null hypothesis ( laptop is better )
null_hypothesis = 0.5

stat, pval = proportions_ztest(count, total, null_hypothesis)
print(pval)