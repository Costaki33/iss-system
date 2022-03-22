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
    10. /sightings/city-<city> 
    11. /help\n

    The <fill_in> is from you to look up something specific 
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

    except FileNotFoundError as e:
        
            logging.error(e)
            return logging.error('ISS Positional Data was not found')
    
    try:
    
        with open('ISS.OEM_J2K_EPH.xml', 'r') as g:
            dataset = xmltodict.parse(g.read())
            position_data = dataset['ndm']['oem']['segment']['stateVector'] 

    except FileNotFoundError as e:
         
            logging.error(e)
            return logging.error('ISS Position Data not found')
    
    return 'Successful! Data has been downloaded \n'
    
#Keys
countries_key = 'country'
region_key = 'region'
city_key = 'city'
epoch_key = 'EPOCH' 
 
# Route: All Epochs in the positional data

@app.route('/epochs', methods = ['GET'])
def get_epochs():

    '''

    This function returns a list of dictionaries, where each dictioary is a epoch dataset of the 
    XML positonal dataset 

    '''
    try: 
        logging.debug('Retrieving epochs requested')
        call = jsonify(position_data)
        return call

    except Exception as e:
        logging.error(e)
        return logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide\n')

# Route: All information about a specific Epoch in the positional data

@app.route('/epochs/<get_epoch>', methods = ['GET'])
def get_epoch(get_epoch: str) -> dict: 

    '''    
     
    This function 1) takes the user input of an epoch call from the /epochs commmands list and 2) returns the first     dictionary who's EPOCH key value matches the user input 

    Args: 
        request (str) : the requested epoch string by the user

    Returns: 
        epoch (dict) : a dictionary containing all the information of the specifc epoch that was requested by the user

    '''
    
    try: 
        for i in position_data:
            if i[epoch_key] == get_epoch:
                logging.debug('Retrieving a specific epoch requested')
                return jsonify(epoch)
		
            logging.info('User requested an unknown epoch value: {requested_epoch}')
            return f'  Requested epoch value: {requested_epoch} was not found. Try again.\n'
    
    except Exception as e:
            logging.error(e)
            return logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide\n')


# Route: All Countries from the sighting data

@app.route('/sightings', methods=['GET'])
def get_sightings():

    '''	
   
    This function returns a list of dictionaries where each dictionary is a collection of sighting data
   
    '''

    try:		
        logging.debug('Retrieving total sighting data requested')
        return jsonify(sighting_data)
    
    except Exception as e:
        logging.error(e)
        return logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide')

# Route: All Countries from the sighting data

@app.route('/sightings/countries', methods = ['GET'])
def get_countries():
    
   '''

   This function returns a list of dictionaries, where each dictionary is a collection of country data as well as the number of times a metorite sighting occured in that specific country
    
   '''

   try:

        total_countries = {}
        sighting_in_countries = []

        for sightings in sighting_data:
            
            if sightings[countries_key] in total_countries.keys():
                total_countries[sightings[countries_key]] += 1
            
            else:
                total_countries[sightings[countries_key]] = 1

        for country in total_countries.keys():
            sightings_in_countries.append({'country': country, 'numsightings': countries[country]})
        
        logging.debug('Retrieving total country data requested')       
        return jsonify(sightings_in_countries)
	
   except Exception as e:
        logging.error(e)
        return logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide')

# Route: All information about a specific Country in the sighting data

@app.route('/sightings/<country>')
def get_country(country: str):
    
    '''
    
    This function takes in a country as the input from the input and returns a list of dictionaries, where each dictionary is a meteorite sighting in that specific country
	
        Args: 
            country (str): the specific country the user would like to request

        Returns:
            country_data (list): a list of dictionaries that contains all the sightings data from that specific country

    '''
 
    try:
        country_data = []
        for sightings in sighting_data:
            if sightings[countries_key] == country.title():
                country_data.append(sightings)
        logging.debug('Get specific country queried')
        return jsonify(country_data)
	
    except Exception as e:
        logging.error(e)
        return logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide')

# Route: All Regions associated with a given Country in the sighting data

@app.route('/sightings/countries/region', methods = ['GET'])
def get_regions() -> dict:

    '''
    
    This function returns a dictionary, where the keys are all of the countries in the sightings data and the associative values are a 
    list of each region where a sighting occured in their respective country
    
    '''
    try:
        countries_regions = {}
        for sightings in sighting_data:
            
            if sightings[countries_key] in countries_regions.keys():
                if not (sighting[region_key] in countries_regions[sightings[countries_key]]):
                    countries_regions[sighting[country_key]].append(sighting[region_key])
            else:
                countries_regions[sighting[country_key]] = [sighting[region_key]]
        
        logging.debug('Get the regions of all countries queried')
        return jsonify(countries_regions)
    
    except Exception as e:
        logging.error(e)
        return logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide')

# Route: All information about a specific Region in the sighting data

@app.route('/sightings/<country>/region', methods = ['GET'])
def get_regions_of_spec_country(country: str) -> dict:

    '''
    
    This function, takes a specific country as user input and returns a dictionary, where the first key is the country given, and the value returned is a list of dictionaries. Each dictionary contains a region with the number of sightings within that region

        Args:
            country (str): the specific country the user requests

        Returns:
            A dictionary (dict), where the country is the first key and its value is a list of dictionaries:
                - each dictionary is a region within that specific country where a sighting had happened
    '''

    try:
 
        regions = {}
        country_regions = []
        
        for sightings in sighting_data:

            if sightings[countries_key] == country.title():
                if sightings[region_key] in regions.keys():

                    regions[sightings[region_key]] += 1
                
                else:
                    regions[sightings[region_key]] = 1
		
        for region in regions.keys():
            country_regions.append({'region': region, 'numsightings': regions[region]})
        
        logging.debug('Retreiving the regions of the specific country requested')
        return jsonify({f'{country.title()}': country_regions})
      
    except Exception as e:
        logging.error(e)
        return logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide')

# Route: All infromation about a sighting in a region 

@app.route('/sightings/region-<region>', methods = ['GET'])
def get_region(region: str):
	
    '''
    This function takes in a region as the user input, and returns a list of dictionaries, where each dictionary is a sighting in that specific region

        Args:
            region (str): the region(s) the user requested 

        Returns:
		regional_sightings (list): a list of dictionaries that contain all the data from a sighting in that specific region	

    '''
	
    try:

        regional_sightings = []
        for sightings in sighting_data:
                if sightings[region_key] == region.title():
                    regional_sightings.append(sightings)

        logging.debug('Retreiving the data of the specific region requested')
        return jsonify(regional_sightings)

    except Exception as e:
        logging.error(e)
        return logging.error("Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide")

# Route: All Cities associated with a given Country and Region in the sighting data

@app.route('/sightings/<country>-<region>-cities')
def get_cities(country: str, region: str) -> dict:
    
    '''
    This function takes a country & region as input, and returns a dictionary, where the [key] is the country provided, and the value is 
    another dictionary, where the:
                       
                        first key value pair = region 
                        second key-value pair = cities

        Args:
            country (str): the country the user is requesting
            region (str): the region the user is requesting

        Returns:
		A dictionary where the key is the country provided and the value is another dictionary 
		where the first key value-pair is the region provided and the second key-value pair are the cities 
		located in that country and region
	
    '''
    
    try:
        
        cities = []
        for sightings in sighting_data:
            if (sightings[countries_key] == country.title()) and (sightings[region_key] == region.title()):
                if not (sightings[city_key] in cities):
                    cities.append(sighting[city_key])
		
        logging.debug('Retreiving the cities from the specific country and respective region requested')
        return jsonify({country.title(): {'region': region.title(), 'citiesinregion': cities} })
	
    except Exception as e:
        logging.error(e)
        return logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide')

# Route: All information about a specific City in the sighting data

@app.route('/sightings/city-<city>', methods = ['GET'])
def get_city(city: str) -> dict:

    '''
    This function takes in a city-name as the input, and returns a dictionary, where they [key] is 
    the city, and the value is a list of the data for sightings in that specific city

        Args:
            city (str): the city the user is requesting

        Returns:
            A dictionary, where they key in the city-name, and the value is a list of dict of all the data for a sighting in that specific city
	
    '''
    
    try:
    
        city_sightings = []
        for sightings in sighting_data:
            if sightings[city_key] == city.title():
                city_sightings.append(sighting)
        
        logging.debug('Retrieving the sighting data for a specific city requested')
        return jsonify({city.title(): city_sightings})
   
    except Exception as e:
        logging.error(e)
        return logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
