# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 23:12:30 2017

@author: tanw
"""

import pandas as pd
import matplotlib.pyplot as plt
matplotlib inline
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 14

#Reading in the files
drink_cols = ['country', 'beer', 'spirit', 'wine', 'liters', 'continent']
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'
drinks = pd.read_csv(url, header=0, names=drink_cols, na_filter=False)

#Sort by the frequency of the number of beers
drinks.beer.sort_values

# Plot frequencies of beer
drinks.beer.plot(kind='hist', bins=3)
drinks.beer.plot(kind='bar')
drinks.beer.plot(kind='hist', bins=25)
drinks.beer.plot(kind='density', xlim=(0, 500))

#comparing beer and wine
drinks[['beer', 'wine']].sort_values('beer')
drinks.plot(kind='scatter', x='beer', y='wine') #comparing with scatterplot
drinks.plot(kind='scatter', x='beer', sharex=False, y='wine', c='spirit', colormap='flag_r')
pd.plotting.scatter_matrix(drinks[['beer', 'spirit', 'liters']])

#UFO dataset
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/ufo.csv'
ufo = pd.read_csv(url)
ufo = ufo.rename(index=str, columns={"Colors Reported": "Color", "Shape Reported": "Shape"})