# here we train the model and evaluate the model and save model in artifacts folder 
import sys
import os

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge,Lasso,ElasticNet
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object
from src.utils import evaluate_model

from dataclasses import dataclass




@dataclass 
class ModelTrainerConfig :
    trained_model_file_path= os.path.join('artifacts','model.pkl') 
    
class ModelTrainer : 
    def __init__(self):
        self.model_trianer_config= ModelTrainerConfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            X_train, y_train, X_test, y_test=( 
                train_array[:,:-1],                     # iv train 
                train_array[:,-1],                      # DV train 
                test_array[:,:-1],                      # iv test 
                test_array[:,-1]                        # DV test 
                )  
            
            models={
            'LinearRegression':LinearRegression(),
            'Lasso':Lasso(),
            'Ridge':Ridge(),
            'Elasticnet':ElasticNet()  
            
            }
            
            
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)            # check utils.py 
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'model_report : {model_report}')
            
            # to get the best model score from dictionary 
            best_model_score = max(sorted(model_report.values())) 
            
            # to get the best model name from dictionary 
            best_model_name =list(models.keys())[ list(model_report.values()).index(best_model_score) ]
            
            best_model=models[best_model_name]
            
            print(f"best_model found ,model name : {best_model_name} , R2_score :{best_model_score}") 
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            
            save_object(
                file_path=self.model_trianer_config.trained_model_file_path,
                obj=best_model
            )
        
        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise CustomException(e,sys)



























# first we give model pickle path  trained_model_file_path = os.path.join('artifacts','model.pkl') 
