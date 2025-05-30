from unsocial_network.src.utils import (
    DigiScape
)

NETWORK_TYPE= ["fully_connected", "small_world"][1]
DIGIZEN_COUNT= 30
NUMBER_OF_ROUNDS= 100
NEIGHBOR_COUNT= 4


digizens= DigiScape(
    network_type= NETWORK_TYPE,
    digizen_count= DIGIZEN_COUNT, 
    number_of_rounds= NUMBER_OF_ROUNDS, 
    neighbor_count= NEIGHBOR_COUNT,
    )

digizens.run_simulation()
digizens.plot_belief_evolution()
digizens.plot_network()
