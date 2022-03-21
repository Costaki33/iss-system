from flask import Flask, jsonify
import json
import xmltodict
import logging
import socket


#Information on how to interact with the application
#All Epochs in the positional data
#All information about a specific Epoch in the positional data
#All Countries from the sighting data
#All information about a specific Country in the sighting data
#All Regions associated with a given Country in the sighting data
#All information about a specific Region in the sighting data
#All Cities associated with a given Country and Region in the sighting data
#All information about a specific City in the sighting data

format_str=f'[%(asctime)s {socket.gethostname()}] %(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)

# Help guide on how to interact with the application 

@app.route('/help', methods = ['GET'])
def help_info():
    return '''\n GUIDE: How to Interact with this application \n
    To use this application, you first need to download the data that this system supports. 
    Use the following command: 
        curl localhost:<your port number>/download -X POST\n
    Once the dataset has been downloaded: you can access it through the application with the following routes:
    1.  /epochs
    2.  /epochs/<get-epoch>
    3.  /sightings
    4.  /sightings/countries
    5.  /sightings/<country>
    6.  /sightings/countries/regions
    7.  /sightings/<country>/regions
    8.  /sightings/region-<region>
    9.  /sightings/<country>-<region>-cities
    10. /sightings/city-<city>\n\n 

 '''

# Downloading the data 

@app.route('/download', methods = ['POST'])
def download(): 
    '''

    This function loads the ISS Sighting and Positional date from their respective XML dataets into 
    the following global variables: 
        sighting_data
        position_data

    Error handling applied

    '''
    global sighting_data
    global position_data
    
    try: 

        with open('XMLsightingData_citiesUSA10.xml', 'r') as f:
            dataset = xmltodict.parse(f.read())
            sighting_data = dataset['visible_passes']['visible_pass']

    except FileNotFoundError as error:
        
            logging.error(error)
            return logging.error('ISS Positional Data was not found')
    
    try:
    
        with open('ISS.OEM_J2K_EPH.xml', 'r') as g:
            dataset = xmltodict.parse(g.read())
            position_data = dataset['ndm']['oem']['segment']['stateVector'] 

    except FileNotFoundError as error:
         
            logging.error(error)
            return logging.error('ISS Position Data not found')
    
    return 'Successful! Data has been downloaded \n'
    
#Keys
countries_key = 'country'
region_key = 'region'
city_key = 'city'
epoch_key = 'EPOCH' 
 
# Route: All Epochs in the positional data
@app.route('/epochs')
def get_epochs() -> List[dict]:

    '''

    This function returns a list of dictionaries, where each dictioary is a epoch dataset of the 
    XML positonal dataset 

    '''
    try: 
        logging.debug('Retrieving epochs requested')
        call = jsonify(position_data)
        return call

















    '''    
     
    This function 1) takes the user input of an epoch call from the /epochs commmands list and 2) returns the first     dictionary who's EPOCH key value matches the user input 

    Args: 
        request (str) : the requested epoch string by the user

    Returns: 
        epoch (dict) : a dictionary containing all the information of the epoch that was requested by the user

    '''
    


















if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
