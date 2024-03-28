## end to end ML project . 

### create env : - 
'''
conda create -p venv python==3.9 -y  
conda activate venv/
'''   

pip install -r .\requirements.txt  or 
 python .\setup.py install    

 setup.py it will install all library from requiremnet.txt  

 
# python -m src.components.data_ingestion  
# python -m src.exception 


 ### src 
 ''' create src folder  :  in the src folser entire lifecylce of ML project will run 

 in that folder 1st crete __init__.py file bcz : these thiswill alaways be a package and we should able to import it to somewhere == to use the functionality of programe everywhere   

 in that we have logger.py() , exception.py() , 
 utils.py(any common funt we want to craete for entire proj)
 
''' 

--------------------------------------------------------------------------
notebook : 

gemstoone.csv :   predcit the price of the diamond based on features   
these data is all about    

EDA : we do EDA Model_training : in .ipynb file  