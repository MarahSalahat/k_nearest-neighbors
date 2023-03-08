# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 20:27:40 2022

@author: marah
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:,[3,4]].values

from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)
plt.title("The Elbo Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

#training the kmeans model on the dataset
kmeans=KMeans(n_clusters=5,init='k-means++',random_state=42)
y_kmeans=kmeans.fit_predict(X)

#visualising the clusters
plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1] ,s=100,c='red',label='cluster_1' )
plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1] ,s=100,c='blue',label='cluster_2' )
plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1] ,s=100,c='green',label='cluster_3' )
plt.scatter(X[y_kmeans==3,0],X[y_kmeans==3,1] ,s=100,c='cyan',label='cluster_4' )
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1] ,s=100,c='magenta',label='cluster_5')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='centroids')
plt.title('Clusters of Customers')
plt.xlabel('Annual Income(k$)')
plt.ylabel('Spending Score(1-100)')
plt.legend()
plt.show()