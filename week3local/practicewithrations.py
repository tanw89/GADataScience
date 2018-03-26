# -*- coding: utf-8 -*-
"""
Created on Fri Sep 01 23:08:32 2017

@author: tanw
"""

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")

from sklearn import datasets
data = datasets.load_iris()
data.keys()

values = [[1,2], [2,5]]
df2 = pd.DataFrame(values, columns=['Type A', 'Type B'], index=['Index 1','Index 2'])
df2.head()

#Reading in my own file!
url = 'C:/Users/tanw/Desktop/Rations_Revisited.csv'
#Defining the column names
col_names = ['Block', 'Unit_No', 'Allswell', 'Meiji_Plain', 'Meiji_Oat', 'Toothpaste', 'Fine_Sugar', 'Light_Sauce', 'Brown_Rice', 'Fragrant_Rice', 'Bran_Oil', 'Coffee', 'Soya_Cereal', 'Soya_Oatmeal', 'Soya_Milk', 'Razor', 'Shampoo', 'Ascience_Shampoo', 'Milo_Poweder', 'Sardine', 'Hup_Seng', 'Fresh_Produce', 'Lux', 'Toothbrush']
rations = pd.read_csv(url, names=col_names, header=None)
#testing what the data looks like
del rations['Block']
del rations['Unit_No']
rations.keys()

#Importing visualisation libraries
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (6, 4)
plt.rcParams['font.size'] = 14
from matplotlib.colors import ListedColormap
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

#Exploring visualisations
rations.plot(kind='scatter', x='Toothpaste', y='Sardine')

#Trying out k-means clustering
from sklearn import cluster
k_means = cluster.KMeans(n_clusters=2)
k_means.fit(rations)

#Setting parameters for the k-means plot
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(1, figsize=(8, 8))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=8, azim=200)
ax.scatter(rations[:, 3], rations[:, 0], rations[:, 2])
plt.cla()
#Plot the cluster figure
ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
ax.set_xlabel('Allswell')
ax.set_ylabel('Meiji_Plain')
ax.set_zlabel('Toothpaste')
plt.show