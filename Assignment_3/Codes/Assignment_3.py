from scipy.stats import norm
from scipy.stats import binom
import numpy as np

p = 0.9
n = 10
k = 3
sig = np.sqrt(n*p*(1-p))

print(1- norm.cdf((k-n*p/sig)))
print((binom.cdf(k,n,p)-norm.cdf((k-n*p)/sig))/binom.cdf(k,n,p))
