import numpy as np
from scipy import stats
import pandas as pd
import statistics



class DigiSapien:
    def __init__(self, id, belief, openness, stubbornness, influence_strength, group_id, ingroup_trust_weight, outgroup_trust_weight):
        self.id= id
        self.belief= belief
        self.openness= openness
        self.stubbornness= stubbornness
        self.influence_strength= influence_strength
        self.group_id= group_id
        self.ingroup_trust_weight= ingroup_trust_weight
        self.outgroup_trust_weight= outgroup_trust_weight


    def upadte_belief(self, neighbor_snapshot):

        print("stop here")
        # local_belief_score= statistics.median(neighbor_beliefs)
        # self.belief= local_belief_score * self.openness * self.stubbornness
        # return self.belief


    def snapshot(self):
        return {
            "belief": self.belief,
            "influence_strength": self.influence_strength,
            "group_id": self.group_id,
            }



class DigiScape:
    def __init__(self, digizen_count, time=None):
        self.digizen_count= digizen_count
        self.time= time
        self.digizen_pool= []
        self.digizen_snapshot= []


    def run_simulation(self):
        #Create digizen pool
        for i in range(self.digizen_count):
            id= f"digizen_{i+1}"
            belief= [1 if x > 1 else -1 if x < -1 else x for x in [np.random.normal(loc=0, scale=0.2)]][0] # -1 (strongly oppose) to 1 (strongly support)
            openness=  [1 if x > 1 else x for x in [np.abs(np.random.normal(loc=0.5, scale=0.1))]][0]  #0 (close minded), 1 (open minded)
            stubbornness= [1 if x > 1 else x for x in [1 - stats.expon.rvs(loc= 0, scale=0.2)]][0] #most people resist change (openness modifier). 1 is high resistance. Negative skewness.
            influence_strength= [1 if x>1 else x for x in [stats.expon.rvs(loc= 0, scale=0.2)]][0] #most people not influential. 0 is no influence strength. Positive skewness.
            group_id= np.random.choice(["L", "R"])
            ingroup_trust_weight= [1 if x > 1 else x for x in [1 - stats.expon.rvs(loc= 0, scale=0.2)]][0] #most people wwight their ingroup highly
            outgroup_trust_weight= [1 if x>1 else x for x in [stats.expon.rvs(loc= 0, scale=0.2)]][0] #most people weight their ingroup poorly
            
            digizen= DigiSapien(
                id= id,
                belief= belief,
                openness= openness,
                stubbornness= stubbornness,
                influence_strength= influence_strength,
                group_id= group_id,
                ingroup_trust_weight= ingroup_trust_weight,
                outgroup_trust_weight= outgroup_trust_weight,
                )
            
            self.digizen_pool.append(digizen)
        
        #Create digizen pool snapshot
        for i in self.digizen_pool:
            self.digizen_snapshot.append(i.snapshot())
        
        #Update digizen pool
        if self.time == None:
            for i in range(len(self.digizen_pool)):
                self.digizen_pool[i].upadte_belief(neighbor_snapshot= self.digizen_snapshot)
