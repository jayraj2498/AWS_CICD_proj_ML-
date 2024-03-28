# here we take train data and test data and do data_transormation 
# we do --> FE , FS , handle missing val , handle cat  & various task 
# by doing all these we get 2 op --> 1) transformed data 2) pickle file(preprocessor.pkl) 

import os 
import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer                 # join pipeline as obj 
from sklearn.impute import SimpleImputer                      # HAndling Missing Values
from sklearn.pipeline import Pipeline           
from sklearn.preprocessing import OrdinalEncoder,StandardScaler    # Ordinal Encoding ,# HAndling Feature Scaling

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object



# here we dont need to write train and test wrt data path bcz op of data_ingestion , or training_pipeline is written train_data , test_data 



@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')
    
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        
        
    def get_data_transformation_object(self):
        
        try:
            logging.info('Data Transformation initiated')
            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            
            logging.info('Pipeline Initiated')

            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())

                ]

            )

            # Categorigal Pipeline
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ]

            )

            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])
            
            logging.info('Pipeline Completed')
            
            return preprocessor

            

        except Exception as e:
            logging.info("Error in Data Trnasformation")
            raise CustomException(e,sys)  
        
    
       
    def initaite_data_transformation(self,train_path,test_path):
        try:
            # Reading train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train Dataframe Head : \n{train_df.head(3).to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_df.head(3).to_string()}')

            logging.info('Obtaining preprocessing object in data transformation')

            preprocessing_obj = self.get_data_transformation_object()

            target_column_name = 'price'
            drop_columns = [target_column_name,'id']

            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)    # iv wrt train 
            target_feature_train_df=train_df[target_column_name]                   # DV wrt train 

            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)         # iv wrt test 
            target_feature_test_df=test_df[target_column_name]                      # DV wrt test 
            
            ## Trnasformating using preprocessor obj
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            logging.info("Applying preprocessing_object on training and testing datasets.")
            

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,  # artifact folder path see code in utils.py.py 
                obj=preprocessing_obj

            )
            logging.info('Preprocessor pickle file saved')

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e,sys)
        
    
    
        
         
   


































# def initaite_data_transformation(self,train_path,test_path):
# now we read our train_data , test_data  and apply all FE step wrt preprocessor and at end we save that pickle file  


## train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)] 
## test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)] 
## after doing preprocessing there may be senario that you will generate many col created if we have to get alll 
## all preprocess data again we have to go through various step , to save that step we will saving data interm 
## inshort we all concatinate all the data in the numpy array and we are concatinate 2 thing ip_feature , target_feature 
## and by converting it into array we are able to load the array it very quickly  


## we will save these preprocessor.pkl file cause we may require these pickle file for any new data 
## we will save these file by using utils.py    

#  save_object(

     # file_path=self.data_transformation_config.preprocessor_obj_file_path,  <-- first parameter 
    # obj=preprocessing_obj )                                                  <-- second parameter 
    
    # we convert preprocessing_obj into a pickle file 
# from src.utils import save_object  <-- inside our artifact folder we able to see pickle file  


