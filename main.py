from unsocial_network.src.utils import (
    DigiScape
)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



digizens= DigiScape(digizen_count=10, time=3).run_simulation()


dataset=[]
for i in digizens:
    dataset.extend(i['cohort_output'])

df= pd.DataFrame(dataset)
print(df)


