from unsocial_network.src.utils import (
    DigiScape
)

NETWORK_TYPE= [
    "fully_connected", 
    "small_world", 
    "scale_free",
    ][2]
DIGIZEN_COUNT= 30
NUMBER_OF_ROUNDS= 100
NEIGHBOR_COUNT= 4
NETWORK_RANDOMNESS= 0.2
GROUPS= ["Left", "Center", "Right"]

digizens= DigiScape(
    network_type= NETWORK_TYPE,
    group= GROUPS,
    digizen_count= DIGIZEN_COUNT, 
    number_of_rounds= NUMBER_OF_ROUNDS, 
    neighbor_count= NEIGHBOR_COUNT,
    network_randomness=NETWORK_RANDOMNESS,
    )

digizens.run_simulation()
digizens.plot_belief_evolution()
digizens.plot_network()
