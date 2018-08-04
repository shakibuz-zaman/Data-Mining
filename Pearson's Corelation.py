
import numpy as np
import h5py
import matplotlib.pyplot as plt
import pandas as pd
dlink=np.array([[66,8],[72,11],[77,15],[84,20],[83,21],[71,11],[65,8],[70,10]]);

np.random.shuffle(dlink)
dff=pd.DataFrame(dlink,columns=['Temperature','Ice Cream Sell'])
dff.corr() # Correlation Matrix