
import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion 
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer 




if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()         # here we save data 
    data_transformation = DataTransformation()                         
    train_arr,test_arr,_=data_transformation.initaite_data_transformation(train_data_path,test_data_path)    # here we do FE and get clean data for doing model_training 
    model_trainer=ModelTrainer()
    model_trainer.initiate_model_training(train_arr,test_arr)                       # here our data will given to various model and we get best model r2score 
    
    
    
    
    
    
    

# python -m src.pipeline.training_pipeline     ,<-- run these 