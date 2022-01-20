from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

print("Hello World")
#lit le tableau csv présent dans le dossier
data = pd.read_csv("base1.csv")
#imprime le tableau récupéré
print(data.head(10))
#détermine combien de graphiques afficher
figure, axis = plt.subplots(2,3)
#Récupère les données
x = data['Prix']
y = data['Taille']
z = data['Distance']
types = data['Prénom']
#Créé des données pour les tableaux sin cos Tan avec numpy
X = np.arange(0, math.pi*2, 0.05)
Y1 = np.sin(X)
Y2 = np.cos(X)
Y3 = np.tan(X)
Y4 = np.tanh(X)

axis[0, 0].plot(X, Y1)
axis[0, 0].set_title("Sine Function")
axis[0, 0].set(xlabel = "X", ylabel = "Sine")

axis[0, 1].plot(X, Y2)
axis[0, 1].set_title("Cosine Function")

axis[1, 0].plot(X, Y3)
axis[1, 0].set_title("Tangent")

axis[1, 1].plot(X, Y4)
axis[1, 1].set_title("Tan Function")

#image im car il faut ça pour mettre la barre
im = axis[0, 2].scatter(x, y, c=data['Distance'])
axis[0, 2].set_title("Prix x Taille x Distance")
#mettre la barre avec im
plt.colorbar(im, ax=axis[0,2], label="Distance (km)")
#mettre les petits labels
for i, txt in enumerate(types):
    axis[0, 2].annotate(txt, (x[i], y[i]), xytext=(5,5), textcoords='offset points', fontsize=8)
    axis[0, 2].scatter(x, y, marker="None")

axis[1, 2].plot(x)
axis[1, 2].set_title("Test avec Prix")

plt.show()
