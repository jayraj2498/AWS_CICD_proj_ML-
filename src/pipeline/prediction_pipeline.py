# whenever we give the input to predict or get our output   so , that kind of itraction should be written in modular coding itself 

import sys 
import os  
from src.exception import CustomException
from src.logger import logging  
import pandas as pd 

from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass 
    
    
    def predict(self,features):                                # it will do all load our model 
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl') 
            
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path) 
            
            data_scaled=preprocessor.transform(features)
            pred=model.predict(data_scaled) 
            
            return pred
            
        except Exception as e:
            raise CustomException(e,sys)    
        
        
class CustomData:                                                   # to call abouve features we created customData wrt how many features we have 
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)














# preprocessor_path=os.path.join('artifacts','preprocessor.pkl') 
# model_path=os.path.join('artifacts','model.pkl')
# always wrrite os.path.join bcz when we do deployemnet it will understand  


#def predict(self,features):   <-- to call these function we should have our featues  data aslo 
# so we will create our custom dataclas ---> class CustomData: (wrt to how many features we have in our dataset ) 

# def get_data_as_dataframe(self):   get the data in the form of dataframe whenever we train our data 
# we train in the form of dataframe so we take and return that as dataframe 

# where our input data is comming from , we have some form on web appl url  wher people putting some data 
# so that data call these function --> get_data_as_dataframe(self):--> to crete dataframe 
# so after getting the dataframe we will call the def predict function --> you will got the output  

# after that we create our app.py to crete our form by using flask 








# we also done that thing in model_training.ipynb <-- then why we doing it here again ? 
#-- > bcoz when you deployed it in cloud and run it should be run as as application 
# so , we make these appliction as in pipeline way 