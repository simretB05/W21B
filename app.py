# Importing the Flask class and request variable from FLASK
from flask import Flask,request
# Importing the json module for JSON serialization
import json
# Importing the dbhelper module
import dbhelper
# Importing API helper/ apihelpers module the apihelpers module
import apihelpers

# Creating a Flask application instance
app=Flask(__name__)


# philospher table with (GET/POST) requests
# GET REQUEST
# Added Route decorator for handling GET requests to the  '/api/philosopher' endpoint getting all philosopher
@app.get('/api/philosopher') 
#  Created  GET request handler function that handles the GET request
def  get_all_philosophers():
    # Call the 'get_all_philosopher()' procedure from the 'dbhelper' module and store the result in a variable
    results = dbhelper.run_procedure('CAll get_all_philosopher()',[])
    # Checking if the results are of type list
    if(type(results)==list):
    # And if so convert the 'results' list to a JSON string using json.dumps function
        philosophers_json= json.dumps(results,default=str)
    # Return the animals JSON string
        return philosophers_json
    # Else return an error message
    else:
        return 'sorry please try again'

# POST REQUEST
# Added Route decorator for handling POSTrequests to the 'api/philosopher' endpoint posting new philosopher
@app.post('/api/philosopher') 
#  Created  POST request handler function that handles the POST data sent from client
def  post_new_philosopher():
       # Check if all required information is provided in the request and if not return an error message
    error=apihelpers.check_endpoint_info(request.json,["name","bio","date_of_birth","date_of_death","image_url"])
    # if error is type string/str then that means we have an error and the other code wont  continue to excute
    if(type(error)==str):
            return  error
    # but if there is no error, code will continue to excute and return results from the procedure call function and add a new philosopher to the database
    results = dbhelper.run_procedure('CAll  add_new_philosopher(?,?,?,?,?)',[request.json.get('name'),request.json.get('bio'),request.json.get('date_of_birth'),request.json.get('date_of_death'),request.json.get('image_url')])
      # Checking if the results are of type list
    if(type(results)==list):
    # And if so convert the 'results' list to a JSON string using json.dumps function
        philosophers_json= json.dumps(results,default=str)
    # Return the animals JSON string
        return philosophers_json
    # Else return an error message
    else:
        return 'sorry please try again'
    

# Quote table with (GET/POST) requests
# GET REQUEST
# Added Route decorator for handling GET requests to the  '/api/quote' endpoint getting quote with specific id
@app.get('/api/quote') 
def  get_all_quote():
    # Check if all required information is provided in the get request and if not return an error message
    error=apihelpers.check_endpoint_info(request.args,["id"])
    # if error is type string/str then that means we have an error and the other code wont  continue to excute
    if(type(error)==str):
            return  error
        # Call the 'get_all_quote_info(?)' procedure from the 'dbhelper' module and store the result in a variable
    results = dbhelper.run_procedure('CAll  get_all_quote_info(?)',[request.args.get('id')])
       # Checking if the results are of type list
    if(type(results)==list):
    # And if so convert the 'results' list to a JSON string using json.dumps function
        quote_json= json.dumps(results,default=str)
    # Return the animals JSON string
        return quote_json
    # Else return an error message
    else:
        return 'sorry please try again'
    

# POST REQUEST
# Added Route decorator for handling POST requests to the 'api/quote' endpoint posting new quote
@app.post('/api/quote') 
#  Created  POST request handler function that handles the POST data sent from client
def  post_new_quote():
    # Check if all required information is provided in the get request and if not return an error message
    error=apihelpers.check_endpoint_info(request.json,["id","content"])
    if(type(error)==str):
            return  error
    # if there is no error, code will continue to excute and return results from the procedure call function and add a new quote to the database
    results = dbhelper.run_procedure('CAll  get_new_quote(?,?)',[request.json.get('id'),request.json.get('content')])
      # Checking if the results are of type list
    if(type(results)==list):
    # And if so convert the 'results' list to a JSON string using json.dumps function
        quote_json= json.dumps(results,default=str)
    # Return the animals JSON string
        return quote_json
    # Else return an error message
    else:
        return 'sorry please try again'
    
# Run the Flask application
app.run(debug=True) 


