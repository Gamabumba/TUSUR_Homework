import pandas as pd
import numpy as np

r = np.random.RandomState(1)
s = pd.Series(r.uniform(0, 10, 100))

print(s[s > 5].index[0])