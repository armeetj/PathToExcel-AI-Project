#author: xarmeetx (Armeet Singh Jatyani 2019)

'''
description: 
This is a test AI regression model. We are using a regression model with 
the input being the percent the student scored on an excercise, and the output
being the number of levels the student needs to jump back or forward.

--> output of -x means the students jumps back x levels
--> output of 1 means the student progresses to the next level and has "mastered" 
    this concept
'''

from __future__ import absolute_import, division, print_function

import pathlib
#pandas is used for data analysis 
import pandas as pd
import numpy as np
#importing seaborn, which helps us draw plots/graphs
import seaborn as sns
#tensor flow ml libr
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping

#constants
EPOCHS = 100

#just prints out the current version of tf
print("tf version: "+ tf.__version__)
print("Armeet Jatyani 2019\n")

#we are given the percent scored by the student and the number of levels we need to jump
column_names = ['Percent','Jump'] 
#define the path for the dataset

#reading using pandas
#pass the path and the names of the columns(the classification of the data)
trainData = pd.read_csv("trainData.csv", names=column_names, na_values = "?", comment='\t', sep=",", skipinitialspace=True)
testData = pd.read_csv("testData.csv", names=column_names, na_values = "?", comment='\t', sep=",", skipinitialspace=True)


#read the training and testing inputs and targets from the csv files
trainInput = trainData.drop(columns = ['Jump'])
trainTarget = trainData.drop(columns = ['Percent'])
testInput = testData.drop(columns = ['Jump'])
testTarget = testData.drop(columns = ['Percent'])

#convert DataFrame to numpy arrays
trainInputNumpy = trainInput.to_numpy();
trainInputNumpy = np.delete(trainInputNumpy, 0);
trainTargetNumpy = trainTarget.to_numpy();
trainTargetNumpy = np.delete(trainTargetNumpy, 0);
testInputNumpy = testInput.to_numpy();
testInputNumpy = np.delete(testInputNumpy, 0);
testTargetNumpy = testTarget.to_numpy();
testTargetNumpy = np.delete(testTargetNumpy, 0);

#count the number of cols in the trainingInputData
n_cols = trainInput.shape[1]

#this function will build the model 
def build_model():
    #the keras model 
    model = keras.Sequential([
    #input layer (first layer)
    layers.Dense(100, activation=tf.nn.relu, input_shape=(n_cols, )),
    #middle/ "hidden" layers
    layers.Dense(100, activation=tf.nn.relu),
    #final layer (output layer)
    layers.Dense(1)
    ])
    
    #make the optimizer we will use
    optimizer = tf.keras.optimizers.RMSprop(0.001)
    #use the adam optimizer and mean squared error as the measure of model performance
    model.compile(optimizer = optimizer, loss = 'mean_squared_error')
    return model

#make the model (call the method)
jump_predict_engine = build_model();
#print out the summary
jump_predict_engine

#training the model
#5 parameters: training input, training targets, validation splits, # epochs, and callbacks
#set early stopping monitor so the model stops training when it won't improve anymore
early_stopping_monitor = EarlyStopping(patience=50)
#train model with fit()
jump_predict_engine.fit(trainInputNumpy, trainTargetNumpy, validation_split=0.2, epochs=EPOCHS, callbacks=[early_stopping_monitor])
print('\FINISHED TRAINING\n')

print("RUNNING TEST DATA")
enginePredictions = jump_predict_engine.predict(testInputNumpy)
print('\FINISHED RUNNING TEST DATA\n')
enginePredictions
