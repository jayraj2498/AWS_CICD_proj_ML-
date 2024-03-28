# make the the flask app to predict ans  

from flask import Flask , request , render_template , jsonify 

from src.pipeline.prediction_pipeline import CustomData , PredictPipeline  

application = Flask(__name__) 
app=application 

@app.route('/') 
def home_page():
    return render_template('index.html') 


@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method == 'GET':                             # if /predict we see form.html(GET) ,# else it is (POST)
        return render_template('form.html')   
    
    else:
        data=CustomData(
            carat=float(request.form.get('carat')),
            depth =float(request.form.get('depth')),         
            table=float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
            
            
        )
        
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)
        results=round(pred[0],2)
        
        
        return render_template('results.html',final_result=results)
        
        




if __name__ == '__main__': 
    app.run(host='0.0.0.0',debug=True) 




































































































# ,jsonify you can jsonify it 

# here we require to call 2 things :from  prediction_pipeline 

#  from src.pipeline.prediction_pipeline import CustomData,PredictPipeline 
                                    
#


# host flask app 
# debug=True) <-- remove it when you do deployement 
#  render_template('index.html') --> alway make template folder for .html file 
# by defauult port it will take 5000 

# @app.route('/') --> home page bydefault GET if we dont use any request 
# render_template('form.html')--> go to that template folder and show on url 

# here /predict handle both GET and POST it show us form we fill the values 
# @app.route('/predict',methods=['GET','POST'])   why get , post ? 
# for get --> see form when you hit /predict
# for post --> submit form 

# in the form we write /predict then show the form  
#  if request.method=='GET':        <-- if GET we see the form 
#    return render_template('form.html') -- > show the form page  

# when we hit /predict then show the form in that --- > for @app.route('/predict',methods=['GET','POST'])<--  here it will both GET and POST 
# then form will be shown & we put all values and at end we submit the form button 

# thes is imp 
# flask has inbuilt function -> url_for() that internal function is called ans it will be post method when we submit it  
# in the form.html ----> <form action="{{url_for('predict_datapoint')}}" method="POST">  <<-- here the method is post 
# whatever function we given here --> predict_datapoint that function get called << now here request.method == 'POST' 
# it will be the post method when we submit --> method="POST"

# so , if submit happend in the form how do we retrive tghe data -> it like action
# if request.method == Get is not GET --> it should be POST 

# so now we have input data and we called Customdata funct from predict pipeline 
# data=CustomData(
#       carat=float(request.form.get('carat')), <-- we getting string val from form we convert it into float
#       whenever we do form submit it comes in term of string format so , we need to typecast it 
#       color= request.form.get('color'), <-- the all already categorical features # these will hanle by pickle file 
# and so on , means requesting from form val to come def CustomData 
# as soon we submit the val we able to get in --> request.form.get()
# here our data is the form of dictionaries 

## now we have our data , so have to convert it into the form of dataframe 
## we called --> get_data_as_dataframe() funvtion 


# final_new_data=data.get_data_as_dataframe()
#         predict_pipeline=PredictPipeline()
#         pred=predict_pipeline.predict(final_new_data) <-- predict take all feature that we take from form nd we make it as dataframe 

#         results=round(pred[0],2)                     <-- prediction it is in the form of array 
#  we take first val pred[0] , wrt to round val of .2 digit  


## and finally 
# we return these results in result.html as final results 
# return render_template('results.html',final_result=results) 













## no need to know html these all front end people will do , U can also use stremlit app ,fastapi 