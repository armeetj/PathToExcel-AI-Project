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
print('input | actual | engine | rounded');
i = 0;


while i < enginePredictions.size:
    print(testInputNumpy[i], end = '     ');
    print(testTargetNumpy[i], end = '     ');
    print(enginePredictions[i][0], end = '     ');
    roundedEnginePredictions[i] = round(enginePredictions[i][0], 0);
    print(round(enginePredictions[i][0], 0));
    i = i + 1;
