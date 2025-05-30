import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import sys
import random
import networkx as nx



class DigiSapien:
    def __init__(self, id, belief, openness, stubbornness, influence_strength, group_id, ingroup_trust_weight, outgroup_trust_weight, number_of_rounds=0):
        self.id= id
        self.belief= belief
        self.openness= openness
        self.stubbornness= stubbornness
        self.influence_strength= influence_strength
        self.group_id= group_id
        self.ingroup_trust_weight= ingroup_trust_weight
        self.outgroup_trust_weight= outgroup_trust_weight
        self.number_of_rounds= number_of_rounds


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
            "number_of_rounds": self.number_of_rounds,
            }



class DigiScape:
    def __init__(self, digizen_count, group, neighbor_count=4, network_randomness=0.2, number_of_rounds=0, network_type="fully_connected"):
        self.digizen_count= digizen_count
        self.number_of_rounds= number_of_rounds
        self.group= group
        self.digizen_pool= []
        self.digizen_snapshot= []
        self.digizen_timeline= []
        if network_type == "fully_connected":
            self.network = nx.complete_graph(n= digizen_count)
        elif network_type == "small_world":
            self.network = nx.watts_strogatz_graph(n=digizen_count, k=neighbor_count, p=network_randomness)
        elif network_type == "scale_free":
            self.network = nx.barabasi_albert_graph(n=digizen_count, m=neighbor_count)
        else:
            sys.exit("Please select one of the provided network types")
    
    
    def run_simulation(self):
        #Start with digizen_count nodes, each being an empty dictionary
        for node_id in self.network.nodes:
            id= f"digizen_{node_id+1}"
            belief= [np.float64(1) if x > np.float64(1) else np.float64(-1) if x < np.float64(-1) else x for x in [np.float64(np.random.normal(loc=0, scale=0.2))]][0] # -1 (strongly oppose) to 1 (strongly support)
            openness=  [np.float64(1) if x > np.float64(1) else x for x in [np.abs(np.random.normal(loc=0.5, scale=0.1))]][0]  #0 (close minded), 1 (open minded)
            stubbornness= [np.float64(1) if x > np.float64(1) else x for x in [np.float64(1) - stats.expon.rvs(loc=0, scale=0.2)]][0] #most people resist change (openness modifier). 1 is high resistance. Negative skewness.
            influence_strength= [np.float64(1) if x > np.float64(1) else x for x in [stats.expon.rvs(loc=0, scale=0.2)]][0] #most people not influential. 0 is no influence strength. Positive skewness.
            group_id= np.random.choice(self.group)
            ingroup_trust_weight= [np.float64(1) if x > np.float64(1) else x for x in [np.float64(1) - stats.expon.rvs(loc= 0, scale=0.2)]][0] #most people weight their ingroup highly. mostly close to 1
            outgroup_trust_weight= [np.float64(1) if x > np.float64(1) else x for x in [stats.expon.rvs(loc= 0, scale=0.2)]][0] #most people weight their ingroup poorly. mostly close to 0
            
            #Create nodes and attach agents to them
            digizen = DigiSapien(
                id= id,
                belief= belief,
                openness= openness,
                stubbornness= stubbornness,
                influence_strength= influence_strength,
                group_id= group_id,
                ingroup_trust_weight= ingroup_trust_weight,
                outgroup_trust_weight= outgroup_trust_weight,
                )
            
            #empty dictionary is populated here {"digizen": digizen}
            self.network.nodes[node_id]["digizen"] = digizen


        assert isinstance(self.number_of_rounds, int), "Please enter a 0 or above intiger value"
        
        for x in range(self.number_of_rounds):
            if x == 0:
                #capture and append
                for node_id in self.network.nodes:
                    digizen = self.network.nodes[node_id]["digizen"]
                    digizen.number_of_rounds= x
                    self.digizen_snapshot.append(digizen.capture_snapshot())
                              
                #add
                self.digizen_timeline.extend(self.digizen_snapshot)

                #reset
                self.digizen_snapshot= []
            
            else:

                for node_id in self.network.nodes:
                    digizen = self.network.nodes[node_id]["digizen"]
                    digizen.number_of_rounds= x
                    neighbors = list(self.network.neighbors(node_id))
                    neighbor_snapshot = [self.network.nodes[i]["digizen"].capture_snapshot() for i in neighbors]
                    digizen.update_belief(neighbor_snapshot)
                    self.digizen_snapshot.append(digizen.capture_snapshot())

                #add
                self.digizen_timeline.extend(self.digizen_snapshot)

                #reset
                self.digizen_snapshot= []
        
        return self.digizen_timeline
    
    
    def plot_network(self):
        shape_map= {}
        group_nodes= {}
        shape_types= ["o", "v", "s", "p", "D", "h"]
        for i in self.group:
            shape= random.choice(shape_types)
            shape_map[i]= shape
            group_nodes[i]= []
            shape_types.remove(shape)
        
        for node_id in self.network.nodes:
            group = self.network.nodes[node_id]["digizen"].group_id
            group_nodes[group].append(node_id)
        
        pos = nx.spring_layout(self.network)
        
        for group, nodes in group_nodes.items():
            node_color= [float(self.network.nodes[i]["digizen"].belief) for i in nodes]
            nx.draw_networkx_nodes(
                G= self.network,
                pos= pos,
                nodelist=nodes,
                node_color= node_color,
                node_shape=shape_map[group],
                label=group,
                cmap="coolwarm",
                alpha=0.95
                )
        
        nx.draw_networkx_edges(
            G= self.network,
            pos= pos,
            alpha=0.3)
        
        plt.legend(loc="best")
        plt.tight_layout()
        plt.show()
    
        
    def process_data_for_plot(self):
        df= pd.DataFrame(self.digizen_timeline)
        df= df.pivot_table(values="belief", columns= "id", index="number_of_rounds", aggfunc="mean")
        df.columns.name= None
        
        return df
    

    def plot_belief_evolution(self):
        df= self.process_data_for_plot()
        for column in df.columns:
            plt.plot(df[column], label= column)

        plt.axhline(y=0, color='r', ls='dashed', label="Neutral")

        plt.title(f"Evolution of belief")
        plt.xlabel("Group exposure rounds")
        plt.ylabel("support vs oppose")

        plt.tight_layout()
        plt.show()