
#created a function that checks  weather all the expected_data items are present in the sent data dictionary 
def check_endpoint_info(sent_data, expected_data):
     # loop through the expected_data items
    for data  in expected_data:
        # Check if the sent_data contains the expected
        #  item, if it is none, it means that the item is missing in the sent data dictionary so it returns an error  message
        if(sent_data.get(data) == None):
        # Return an error message if the expected item is not 
         # used formatted string literal to concatenate  the exact missing data  to clarify what is missing in the request
            return f"The {data} must be sent!" 