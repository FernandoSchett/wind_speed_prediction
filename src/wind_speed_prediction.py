'''
File:           wind_speed_prediction.py
Last changed:   15/06/2023 21:21
Purpose:        tensorflow implementation for wind speed prediction         
Authors:        Fernando Antonio Marques Schettini  
Usage: 
  HowToExecute:   python3 wind_speed_prediction.py           

Problem Description:

Wind speed is an important factor that can affect the growth and yield of oranges. The farmer has collected historical data on wind speed and its corresponding suitability for orange cultivation. Each sample consists of a measurement of wind speed (in meters per second), which is available in _datasets_ folder, named as `wind_data_train.csv`.
In order to ensure ideal growth conditions, the same farmer wishes to develop a prediction system that determines the wind speed based on the historical data.
You are tasked with training the model using the provided data and then testing it using a separate test dataset, named `wind_data_test.cs` and located at _datasets_ directory.
'''

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Read the input file:
x_train = pd.read_csv("./datasets/wind_data_train.csv", sep=",", header=0)

values_title = list(x_train.columns.values)

y_train = x_train.iloc[:, [-1]]
x_train = x_train.iloc[:, [*range(len(values_title)-1)]]

x_test = pd.read_csv("./datasets/wind_data_test.csv", sep=",", header=0)

y_test = x_test.iloc[:, [-1]]
x_test = x_test.iloc[:, [*range(len(values_title)-1)]]


# Show data:
print("----------train data info------------")
print(x_train.info())
print(x_train.head())
print(y_train.head())

print("----------test  data info------------")
print(x_test.info())
print(x_test.head())
print(y_test.head())

x_test.plot()

#Convert the commented code to np, it automatically normalizes between 0 and 1:
x_train = np.array(x_train)
y_train = np.array(y_train)

x_test = np.array(x_test)
y_test = np.array(y_test)

# Check normalization:
x_train = x_train/2015
x_test = x_test/2015

print("----------NAN in xtrain------------")
print(np.argwhere(np.isnan(x_train)))
print("----------NAN in ytrain------------")
print(np.argwhere(np.isnan(y_train)))


def plot_data_comp(title,data_plot1,data_plot2):
    plt.figure(figsize=(14, 10), dpi=80, facecolor='w', edgecolor='k')

    # plt.subplot(2, 1, 0)
    plt.plot(data_plot1,label="Original")
    plt.plot(data_plot2,label="Predicted")

    plt.xlabel("Minutes")
    plt.ylabel("Wind Speed")
    plt.title(title)
    plt.legend(loc=0)
    plt.show()

def create_model(x_train, y_train, x_test, y_test, listall, name): 
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(len(x_train[0]), input_shape=(len(x_train[0]),), activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(90, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(90, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(90, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(1, activation="linear"))

    tf.keras.utils.plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
    
    learning_rate = 0.01
    model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=learning_rate),
                    loss=['mse'],
                    metrics=['mae'])

    print("training learning_rate=%f" % learning_rate)
    history = model.fit(x_train, y_train, batch_size=50, epochs=30)

    val_loss, val_acc = model.evaluate(x_test, y_test)
    print("MSE:", val_loss, "|MAE:", val_acc)

    # Plot training & validation loss values
    plt.figure(figsize=(14, 10), dpi=80, facecolor='w', edgecolor='k')
    plt.plot(history.history['loss'])
    plt.title('Model loss Final Loss %f (MSE):%.2f MAE:%.2f' % (learning_rate, val_loss, val_acc))
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    
    if name != False:
        model_json = model.to_json()
        with open("%s.json" % (name), "w") as json_file:
            json_file.write(model_json)
        # Serialize weights to HDF5
        model.save_weights("%s.h5" % (name))
        print("Saved model to disk")

    return model

def load_model(name):
    # Load JSON and create model
    json_file = open("%s.json" % name, "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # Load weights into the new model
    loaded_model.load_weights("%s.h5" % name)
    print("Loaded model from disk")
    return loaded_model

def get_model(x_train, y_train, x_test, y_test, listall, name):
    my_file = Path("%s.json" % (name))
    if my_file.is_file():
        return load_model(name)
    return create_model(x_train, y_train, x_test, y_test, listall, name);


#Input and Outpus number
listsee = [0]
listall = [9]

model = get_model(x_train, y_train, x_test, y_test, listall, "temp2015_2")

predictions = model.predict(x_test)

for i in listsee:
    plot_data_comp("Comparation %s: Anemometer vs. Predicted: Dataset = TRAIN" % (values_title[9]),y_test[:,i],
                   predictions[:,i])