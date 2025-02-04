import pandas as pd
import numpy as np

data = pd.read_csv("DataSet2.csv")

features = np.array(data) [:,:-1]
target = np.array(data) [:,-1]

def finds(fea, tar):
    for i, val in enumerate(target):
        if val.upper() == "POSITIVE":
            spc_h = fea[i].copy()
            break
        
    for i, val in enumerate(features):
        if tar[i].upper() == "POSITIVE":
            for x in range(len(spc_h)):
                if spc_h[x] != val[x]:
                    spc_h[x] = "?"
                else:
                    pass
    return spc_h
print(finds(features, target))