import numpy as np
from scipy import stats
import sys



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


    def weighted_average(self, group):
        total_weight = sum(i["influence_strength"] for i in group)
        if total_weight == 0:
            return 0
        return sum(i["belief"] * i["influence_strength"] for i in group) / total_weight
    

    def update_belief(self, neighbor_snapshot):
        ingroup = [i for i in neighbor_snapshot if i["group_id"] == self.group_id]
        outgroup = [i for i in neighbor_snapshot if i["group_id"] != self.group_id]

        ingroup_belief = self.weighted_average(group= ingroup)
        outgroup_belief = self.weighted_average(group= outgroup)

        influence = (self.ingroup_trust_weight * ingroup_belief) + (self.outgroup_trust_weight * outgroup_belief)
        
        # Apply stubbornness (resistance to change)
        updated_belief = ((1 - self.stubbornness) * influence) + (self.stubbornness * self.belief)
        
        # Apply openness (willingness to shift)
        self.belief += (self.openness * (updated_belief - self.belief))

        return self.belief


    def capture_snapshot(self):
        return {
            "id": self.id,
            "belief": self.belief,
            "influence_strength": self.influence_strength,
            "group_id": self.group_id,
            }



class DigiScape:
    def __init__(self, digizen_count, time=0):
        self.digizen_count= digizen_count
        self.time= time
        self.digizen_pool= []
        self.digizen_snapshot= []
        self.digizen_timeline= []

    def run_simulation(self):
        #Create digizen pool
        for i in range(self.digizen_count):
            id= f"digizen_{i+1}"
            belief= [np.float64(1) if x > np.float64(1) else np.float64(-1) if x < np.float64(-1) else x for x in [np.float64(np.random.normal(loc=0, scale=0.2))]][0] # -1 (strongly oppose) to 1 (strongly support)
            openness=  [np.float64(1) if x > np.float64(1) else x for x in [np.abs(np.random.normal(loc=0.5, scale=0.1))]][0]  #0 (close minded), 1 (open minded)
            stubbornness= [np.float64(1) if x > np.float64(1) else x for x in [np.float64(1) - stats.expon.rvs(loc=0, scale=0.2)]][0] #most people resist change (openness modifier). 1 is high resistance. Negative skewness.
            influence_strength= [np.float64(1) if x > np.float64(1) else x for x in [stats.expon.rvs(loc=0, scale=0.2)]][0] #most people not influential. 0 is no influence strength. Positive skewness.
            group_id= np.random.choice(["L", "R"])
            ingroup_trust_weight= [np.float64(1) if x > np.float64(1) else x for x in [np.float64(1) - stats.expon.rvs(loc= 0, scale=0.2)]][0] #most people weight their ingroup highly. mostly close to 1
            outgroup_trust_weight= [np.float64(1) if x > np.float64(1) else x for x in [stats.expon.rvs(loc= 0, scale=0.2)]][0] #most people weight their ingroup poorly. mostly close to 0
            
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
        
        

        if isinstance(self.time, int):
            for x in range(self.time):
                if x == 0:
                    #capture
                    self.digizen_snapshot= [i.capture_snapshot() for i in self.digizen_pool]
                    
                    #add
                    self.digizen_timeline.append(
                        {
                            "time_point": x,
                            "cohort_output": self.digizen_snapshot
                        }
                    )

                    #reset
                    self.digizen_snapshot= []
                else:
                    #update
                    for i in range(len(self.digizen_pool)):
                        self.digizen_pool[i].update_belief(neighbor_snapshot= self.digizen_snapshot)
                    
                    #capture
                    self.digizen_snapshot= [i.capture_snapshot() for i in self.digizen_pool]
                    
                    #add
                    self.digizen_timeline.append(
                        {
                            "time_point": x,
                            "cohort_output": self.digizen_snapshot
                        }
                    )

                    #reset
                    self.digizen_snapshot= []
            
            return self.digizen_timeline

        else:
            sys.exit("Please enter a 0 or above intiger value")