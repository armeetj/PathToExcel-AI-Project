#================================================#
# author: xarmeetx (Armeet Singh Jatyani 2019)   #
#================================================#

'''
description: 
-------------------------------------------------------------------------------------------------------
    Loop infinitely until -1 is entered...
    
    Enter in input with format: 
     ID Difficulty Percent
    
    Example:
     32 0.6 0.87
    
    Calls the returnNextLessonByID() method 
     and stores the resulting tuple in result
'''
while 0 == 0: 
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
     G2 M3 L1 0.6 0.87
    
    Calls the returnNextLessonByName() method 
     and stores the resulting tuple in result
'''
while 0 == 0: 
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
