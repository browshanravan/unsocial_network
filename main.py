import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt




class DigiSapiens:
    def __init__(self, belief, openness, stubbornness, group_id, influence_strength):
        self.belief= belief #[1 if x > 1 else -1 if x < -1 else x for x in [np.random.normal(loc=0, scale=0.2)]][0] #ranges from -1 strongly oppose to 1 stringly support
        self.openness= openness # [1 if x>1 else x for x in [np.abs(np.random.normal(loc=0.5, scale=0.1))]][0] ranges from 0 (close minded) to 1 (open minded)
        self.stubbornness= stubbornness #[1 if x>1 else x for x in [1 - stats.expon.rvs(loc= 0, scale=0.2)]][0] most people are resist to change (openness modifier). 1 is high resistance. negative skewness
        self.group_id= group_id
        self.influence_strength= influence_strength #[1 if x>1 else x for x in [stats.expon.rvs(loc= 0, scale=0.2)]][0] most people not influential. 0 is no influence strength. Positive skewness
    
