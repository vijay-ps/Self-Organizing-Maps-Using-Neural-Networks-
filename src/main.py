import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor

data = pd.read_csv('data/Wholesale customers data.csv')
data = data.drop(['Channel', 'Region'], axis=1)

scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

som = MiniSom(x=10, y=10, input_len=data_scaled.shape[1], sigma=1.0, learning_rate=0.5)
som.random_weights_init(data_scaled)
som.train_random(data_scaled, 500)

plt.figure(figsize=(10, 10))
plt.pcolor(som.distance_map().T, cmap='coolwarm')
plt.colorbar()
plt.title('SOM U-Matrix')
plt.savefig('visuals/matrix.png')
plt.show()

lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
outliers = lof.fit_predict(data_scaled)

plt.figure(figsize=(10, 10))
plt.pcolor(som.distance_map().T, cmap='coolwarm')
plt.colorbar()

for i, x in enumerate(data_scaled):
    w = som.winner(x)
    if outliers[i] == -1:
        plt.plot(w[0] + 0.5, w[1] + 0.5, 'rx', markersize=12, markeredgewidth=2)
    else:
        plt.plot(w[0] + 0.5, w[1] + 0.5, 'bo', markersize=12, markeredgewidth=2)

plt.title('SOM with Anomaly Detection')
plt.savefig('visuals/anomalies.png')
plt.show()
