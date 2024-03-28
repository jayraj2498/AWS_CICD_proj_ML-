# utils is the place which is common for entire project we make heer function and 
# use in entire project where it required 


import os
import sys
import pickle
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.exception import CustomException
from src.logger import logging


# to save preprocessor.pickle file  
# to save model.pickle file 


def save_object(file_path, obj):                   # save_object(it will take path of pickle file , preprocessor)
    try:
        dir_path = os.path.dirname(file_path)       # directory path 

        os.makedirs(dir_path, exist_ok=True)        # make directory 

        with open(file_path, "wb") as file_obj:     # we open file in wb mode 
            pickle.dump(obj, file_obj)              # dump the file               

    except Exception as e:
        raise CustomException(e, sys)  
    
    
    
    
# evalute models from model_trainer.py 



def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report={} 
        for i in range(len(models)):
            model=list(models.values())[i] 
            #train model 
            model.fit(X_train,y_train)
            # predicting test data 
            y_test_pred =model.predict(X_test) 
            # Get R2 scores
            test_model_score =r2_score(y_test,y_test_pred)
            
            report[list(models.keys())[i]] = test_model_score
            
        return report
            
    
    except Exception as e:
        logging.info('Exception occured during model training ')
        raise CustomException(e, sys)
    
    

    
    
# to load preprocessor.pickle file  
# to load model.pickle file 

def load_object(file_path):              # from these file path load the  model in prediction_pipeline.py 
    try:
        with  open(file_path ,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e, sys)
    
    
    

    
    
 
    
    
    
    
    
    
    
# def save_object(file_path, obj):
# these whatever  directory path we giving it will save over , and crete directory save , and dump over 
# whatever object we givw 
  
#