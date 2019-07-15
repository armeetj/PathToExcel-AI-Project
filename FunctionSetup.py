#================================================#
# author: xarmeetx (Armeet Singh Jatyani 2019)   #
#================================================#

'''
description: 
-------------------------------------------------------------------------------------------------------
method returnNextLessonByID: 
    -> Here we pass the ID of the excercise, the difficulty, and the score of the student.
    -> We return a tuple with format (id, name) which is the id and name of the next predicted lesson.

method returnNextLessonByName:
    -> Here we passe dhte Name of the excercise, the diffuculty, and the score of the student.
    -> We return a tuple with format (id, name) which is the id and name of the next predicted lesson.
'''

#return next lesson by the id of the excercise 
def returnNextLessonByID(parsedInput):
    #ID is the first argument
    ID = int(parsedInput[0]);
    
    #make the data to pass into the testing
    data = np.array([[parsedInput[1], parsedInput[2], parsedInput[3]]]);
    #make the prediction
    prediction = jump_predict_engine.predict(data); 
    
    #couunt is the prediction
    count = int(prediction[0][0]);
    print("Prediction: ", end = '');
    print(count);
    
    #we keep i so that we can keep track of how much we have jumped back
    i = 0;
    currentId = ID;
    currentName = '';
    print('Jumping: ')
    if count > 0: 
        currentName = (ConversionTableNumpy.item(currentId));
        return (ID + 1, currentName);
    elif count == 0: 
        currentName = (ConversionTableNumpy.item(currentId - 1));
        return (ID, currentName);
    elif count < 0:
        count = -count;
        while i < count:
            currentId = int(BackmapIDNumpy.item(currentId - 1));
            print(currentId);
            i = i + 1;
    currentName = (ConversionTableNumpy.item(currentId - 1));
    return (currentId, currentName);



#return the next lesson by the name of the excercise 
def returnNextLessonByName(parsedInput):
    #take the name of the lesson from the parsedInput and concatenate it all into one variable
    name = (parsedInput[0] + ' ' + parsedInput[1] + ' ' + parsedInput[2]);
    #find the id of this lesson
    ID = np.where(ConversionTableNumpy == name)[0][0] + 1;
    print(ID);
    #constructing input data for the keras net
    data = np.array([[parsedInput[3], parsedInput[4], parsedInput[5]]]);    
    
    #make the prediction
    prediction = jump_predict_engine.predict(data); 
    
    count = int(prediction[0][0]);
    print("Prediction: ", end = '');
    print(count);
    
    i = 0;
    currentId = ID;
    currentName = '';
    print('Jumping: ')
    if count > 0: 
        currentName = (ConversionTableNumpy.item(currentId));
        return (ID + 1, currentName);
    elif count == 0: 
        currentName = (ConversionTableNumpy.item(currentId - 1));
        return (ID, currentName);
    elif count < 0:
        count = -count;
        while i < count:
            currentId = int(BackmapIDNumpy.item(currentId - 1));
            print(currentId);
            i = i + 1;
    currentName = (ConversionTableNumpy.item(currentId - 1));
    return (currentId, currentName);
