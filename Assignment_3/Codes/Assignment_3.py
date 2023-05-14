import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
simlen=10000000
#number of trials
n =  10

#Probability that person chosen is left-handed
p = 0.1

experiment=np.zeros(1)
acctual=np.zeros(1)
data_binom = binom.rvs(n,p,size=simlen)  #Simulating the event 
defects,stimulation = np.unique(data_binom , return_counts= True)
if (len(stimulation) == 8):
	stimulation = np.insert(stimulation,8,0)
	stimulation = np.insert(stimulation,9,0)
	stimulation = np.insert(stimulation,10,0)
if (len(stimulation) == 9):
	stimulation = np.insert(stimulation,9,0)
	stimulation = np.insert(stimulation,10,0)
if (len(stimulation) == 10):
	stimulation = np.insert(stimulation,10,0)
stimulation = np.cumsum(stimulation)/simlen
experiment[0]=stimulation[3]
acctual[0]=binom.cdf(3,n,p)
exp = str(1 - round(experiment[0],4))
act = str(1 - round(acctual[0],4))
print("For answer  stimulation value is "+ exp +" and acctual value is "+ act )
