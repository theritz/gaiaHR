# %%
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np
import glob

# set input file path
data_folder = '/Users/maurits/Documents/VCS_projects/GaiaHR/files/'
#data_folder = '../GaiaHR/files/'

# read csv into dataframe using a lambda function
dfraw = pd.concat([pd.read_csv(f)
    for f in glob.glob(data_folder+'*.csv')], ignore_index=True)
gaiaHR = dfraw

# clean up NaN values not necessary as they won't be plotted anyway
#gaiaHR = dfraw[np.isfinite(dfraw['lum_val'])]
#gaiaHR = dfraw[np.isfinite(dfraw['teff_val'])]

# what we're here for: colour & brightness
x = gaiaHR['teff_val'] #Temperature in K
y = gaiaHR['lum_val'] #absolute magnitude derived by FLAME instrument

# set some labels, scale, colours etc.
plt.style.use('dark_background')
plt.yscale('log')
plt.title('Hertzsprung-Russell Diagram', fontsize=20)
plt.xlabel('Temperature[K]')
plt.ylabel('Apsis-FLAME Luminosity (ℒ)')
plt.scatter(x, y, s=3, c=x, cmap=plt.get_cmap('RdYlBu_r'))
plt.gca().invert_xaxis()
plt.show()
# clipped on y-axis min, not checked why
