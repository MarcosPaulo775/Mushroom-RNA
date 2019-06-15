import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix
import converter as conv
import confusion_matrix as cm
import matplotlib.pyplot as plt


dataset = open("dataset/agaricus-lepiota.data").readlines()
# 8124 valores

x_train = []
x_test = []
y_train = []
y_test = []

for i in range(len(dataset)):
    dataset[i] = dataset[i].split(",")
    dataset[i][22] = dataset[i][22].strip("\n")

# Cria os vetores X e Y de treinamento adicionando 75% do dataset;
for i in range(2031, 8124):
    x_values = []
    for j in range(1, 23):
        if(j != 11):
            x_values.append(dataset[i][j])

    y_train.append(dataset[i][0])
    x_train.append(x_values)


# Cria os vetores X e Y de teste com o restante(25%) do dataset;
for i in range(2031):
    x_values = []
    for j in range(1, 23):
        if(j != 11):
            x_values.append(dataset[i][j])

    y_test.append(dataset[i][0])
    x_test.append(x_values)

# Tratando os vetores de treinamento
x_train = np.array(x_train)
x_train = conv.converterX4(x_train)
y_train = np.array(y_train)
y_train = conv.converterY(y_train)

# Tratando os vetores de test
x_test = np.array(x_test)
x_test = conv.converterX4(x_test)
y_test = np.array(y_test)
y_test = conv.converterY(y_test)
# Para entender melhor a função converter olhar a descrição no arquivo converter.py

model = Sequential()
model.add(Dense(6, activation='sigmoid', input_dim=21))
model.add(Dense(6, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='Nadam', loss='mean_squared_error', metrics=['acc'])

model.summary()

history = model.fit(x_train, y_train, epochs=80)

y_pred = model.predict(x_test)


# --- Parte da Matriz de Confusao ---
matrizConfusao = confusion_matrix(y_test, conv.converterUmZero(y_pred))

df = pd.DataFrame({"Comestivel(Predito)": [matrizConfusao[0][0], matrizConfusao[1][0]], "Venenoso(Predito)": [
                  matrizConfusao[0][1], matrizConfusao[1][1]]}, index=["Comestivel", "Venenoso"])
print("\n ", df)

cm.calcAcuracia(matrizConfusao)
cm.calcRecall(matrizConfusao)
cm.calcPrecisao(matrizConfusao)
cm.calcFScore(matrizConfusao)

plt.plot(history.history['loss'])
plt.title('Loss X Epoch')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Loss'], loc='upper left')
plt.show()

plt.plot(history.history['acc'])
plt.title('Accuracy X Epoch')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Accuracy'], loc='upper left')
plt.show()
