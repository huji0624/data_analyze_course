import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['axes.grid'] = True

def filter(tdf,evlist):
    laststep = None
    filters = []
    for ev in evlist:
        if laststep is not None:
            t = tdf[tdf['event_name']==ev].drop_duplicates("id")
            step = t[t['id'].isin(laststep['id'])]
        else:
            step = tdf[tdf['event_name']==ev].drop_duplicates("id") 
        laststep = step
        filters.append(len(step))
    s = pd.Series(filters)
    t = s/s.max()
    print(t)
    t.plot()
