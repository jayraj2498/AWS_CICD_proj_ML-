# reading the dataset   

import os                       # it is superimp to join the path , to create the file path   
import sys                      # it s use for sys error 
from src.exception import CustomException 
from src.logger import logging   
import pandas as pd 
from sklearn.model_selection import train_test_split  
from dataclasses import dataclass               # by usinf these u can directly create variable name ,no need to create __init__ 

from src.components.data_transformation import DataTransformation


    
# we are taking data as input path storing that  varible inside the dataclass 
# we are intitializing the data ingestion congfigration 
# these artifacts will be our folder name it will auto creted by our code 
# and that csv file will beused in as DataTransformation.py as input 

@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')


# now entire DataIngestionconfig: we need to send it --> dataingestion
# crete the class  for data_ingestion 
# see here we are not using dataclass , so we use __init__  

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion methods Starts')
        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train test split')
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of Data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
  
            
        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)
    




# these entire code will go to in our pipeline-> training pipeline.py  
'''
if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.initaite_data_transformation(train_data_path,test_data_path)'''
    
# os.path -> current directry path 
# self.ingestion_config=DataIngestionconfig() --> inside it we able to get all three path 
# def initiate_data_ingestion(self): --> here we read the data 
# exist_ok=True --> if its exist dont create the directtory 
# train_set.to_csv test_set.to_csv  --> we are saving it to the path 
# 
