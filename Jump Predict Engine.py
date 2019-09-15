#================================================#
# author: xarmeetx (Armeet Singh Jatyani 2019)   #
#================================================#

'''
description: 
-------------------------------------------------------------------------------------------------------
This is a AI regression model. 

Input:
-------------------------------------------------------------------------------------------------------
Momentum, Proficiency, Difficulty, Percent

Output
-------------------------------------------------------------------------------------------------------
--> output of -x means the students jumps back x levels
--> output of 1 means the student progresses to the next level and has "mastered" 
    this concept
--> output of 0 means the student has to retry the excercise
'''

from __future__ import absolute_import, division, print_function, unicode_literals

import pathlib
#pandas is used for data analysis 
import pandas as pd;
import numpy as np;
#importing seaborn, which helps us draw plots/graphs
import seaborn as sns;
#tensor flow ml library
import tensorflow as tf;
from tensorflow import keras;
from tensorflow.keras import layers;
from tensorflow.keras.callbacks import EarlyStopping;

#constants
EPOCHS = 1000;

#just prints out the current version of tf
print("tf version: "+ tf.__version__);
print("Armeet Jatyani 2019\n");

#we are given the percent scored by the student and the number of levels we need to jump
input_column_names = ['Momentum','Proficiency','Difficulty', 'Percent','Jump'] ;
#define the path for the dataset

#reading using pandas
#pass the path and the names of the columns(the classification of the data)
trainData = pd.read_csv("trainData.csv", names=input_column_names, na_values = "?", comment='\t', sep=",", skipinitialspace=True);
# trainData = trainData.drop([0], axis=0);
testData = pd.read_csv("testData.csv", names=input_column_names, na_values = "?", comment='\t', sep=",", skipinitialspace=True);
# testData = testData.drop([0], axis=0);

#read the backmapping and conversiontable data
IDBackMapping = pd.read_csv("IDBackMapping.csv", names=['ID', 'Backmap ID'], na_values = "?", comment='\t', sep=",", skipinitialspace=True);
ConversionTable = pd.read_csv("ConversionTable.csv", names=['ID', 'Name'], na_values = "?", comment='\t', sep=",", skipinitialspace=True);

#read the training and testing inputs and targets from the csv files
trainInput = trainData.drop(columns = ['Jump']);
trainTarget = trainData.drop(columns = ['Momentum','Proficiency', 'Difficulty', 'Percent']);
testInput = testData.drop(columns = ['Jump']);
testTarget = testData.drop(columns = ['Momentum','Proficiency', 'Difficulty', 'Percent']);


IDNumpy = IDBackMapping.drop(columns = ['Backmap ID']).to_numpy();
BackmapIDNumpy = IDBackMapping.drop(columns = ['ID']).to_numpy();
ConversionTableNumpy = ConversionTable.drop(columns = ['ID']).to_numpy();
IDNumpy = np.delete(IDNumpy, 0);
BackmapIDNumpy = np.delete(BackmapIDNumpy, 0);
ConversionTableNumpy = np.delete(ConversionTableNumpy, 0);

#convert DataFrame to numpy arrays
trainInputNumpy = trainInput.to_numpy();
trainInputNumpy = np.delete(trainInputNumpy, 0, 0);
trainTargetNumpy = trainTarget.to_numpy();
trainTargetNumpy = np.delete(trainTargetNumpy, 0);
testInputNumpy = testInput.to_numpy();
testInputNumpy = np.delete(testInputNumpy, 0, 0);
testTargetNumpy = testTarget.to_numpy();
testTargetNumpy = np.delete(testTargetNumpy, 0);

#count the number of cols in the trainingInputData
n_cols = trainInput.shape[1];

print('training shape: ');
print(trainInput.shape);


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
    optimizer = keras.optimizers.Adam(lr=0.01, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False);
    #use the adam optimizer and mean squared error as the measure of model performance
    model.compile(optimizer = optimizer, loss = 'mean_squared_error');
    return model;

#make the model (call the method)
jump_predict_engine = build_model();
#print out the summary
jump_predict_engine;

#training the model
#5 parameters: training input, training targets, validation splits, # epochs, and callbacks
#set early stopping monitor so the model stops training when it won't improve anymore
early_stopping_monitor = EarlyStopping(patience=100);
#train model with fit()
jump_predict_engine.fit(trainInputNumpy, trainTargetNumpy, validation_split=0.1, epochs=EPOCHS, callbacks=[early_stopping_monitor]);

print('\nFINISHED TRAINING\n');

print("RUNNING TEST DATA");

enginePredictions = jump_predict_engine.predict(testInputNumpy);
roundedEnginePredictions = enginePredictions;

print('\nFINISHED RUNNING TEST DATA\n');

print('         input         | actual | engine | rounded');

i = 1
while i < enginePredictions.size:
    print(testInputNumpy[i], end = '     ');
    print(testTargetNumpy[i], end = '     ');
    print(enginePredictions[i][0], end = '     ');
    roundedEnginePredictions[i] = round(enginePredictions[i][0], 0);
    print(roundedEnginePredictions[i][0]);
    i = i + 1;


#================================================#
# author: xarmeetx (Armeet Singh Jatyani 2019)   #
#================================================#

'''
description: 
-------------------------------------------------------------------------------------------------------
    Loop infinitely until -1 is entered...
    
    Enter in input with format: 
     ID Proficiency Difficulty Percent
    
    Example:
     32 .89 0.6 0.6 0.87
    
    Calls the returnNextLessonByID() method 
     and stores the resulting tuple in result
'''
while 0 == 0: 
    print("input: lesson ID, momentum, proficiency, difficulty, percent, jump")
    inputString = input();
    if inputString == '-1':
        break;
    parsedInput = inputString.split(" ");
    try:
        result = returnNextLessonByID(parsedInput);
        print('answer:', end = " ")
        print(result);
        print();
    except:
        print("ERROR");

'''
description: 
-------------------------------------------------------------------------------------------------------
    Loop infinitely until -1 is entered...
    
    Enter in input with format: 
     Name of Excercise Difficulty Percent
    
    Example:
     G2 M3 L1 0.89 0.6 0.6 0.87
    
    Calls the returnNextLessonByName() method 
     and stores the resulting tuple in result
'''
while 0 == 0: 
    print("input: lesson, momentum, proficiency, difficulty, percent, jump")
    inputString = input();
    if inputString == '-1':
        break;
    parsedInput = inputString.split(" ");
    try:
        result = returnNextLessonByName(parsedInput);
        print('answer:', end = " ")
        print(result);
        print();
    except:
        print("ERROR");


        #================================================#
# author: xarmeetx (Armeet Singh Jatyani 2019)   #
#================================================#

'''
description: 
    This program shows all the read data including...
        -> DataFrame objects read from csv
        -> converted Numpy Arrays
        -> Testing Data/Results
'''

print("training data: ");
print(type(trainData));
print(trainData.head());
print();
print("testing data: ");
print(type(testData));
print(testData.head());
print("\n");

print("training inputs")
print(type(trainInput));
print(trainInput.head());
print();
print("training targets");
print(type(trainTarget));
print(trainTarget.head());
print();

print("testing inputs");
print(type(testInput));
print(testInput.head());
print();
print("testing targets");
print(type(testTarget));
print(testTarget.head());
print("\n");

print("training inputs numpy: ");
print(type(trainInputNumpy));
print(trainInputNumpy);
print();
print("training targets numpy: ");
print(type(trainTargetNumpy));
print(trainTargetNumpy);
print();
print("test inputs numpy: ");
print(type(testInputNumpy));
print(testInputNumpy);
print();
print("test targets numpy: ");
print(type(testTargetNumpy));
print(testTargetNumpy);
print();

print(IDNumpy)
print(BackmapIDNumpy)
print('         input         | actual | engine | rounded');
i = 0;


while i < enginePredictions.size:
    print(testInputNumpy[i], end = '     ');
    print(testTargetNumpy[i], end = '     ');
    print(enginePredictions[i][0], end = '     ');
    roundedEnginePredictions[i] = round(enginePredictions[i][0], 0);
    print(round(enginePredictions[i][0], 0));
    i = i + 1;