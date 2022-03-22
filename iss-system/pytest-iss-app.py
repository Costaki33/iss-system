from iss_system_app import *
from flask import jsonify
import pytest


def test_help():
    assert help() == '''\n GUIDE: How to Interact with this application \n
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
    7.  /sightings/<country>/region
    8.  /sightings/region-<region>
    9.  /sightings/<country>-<region>-cities
    10. /sightings/city-<city> 
    11. /help
    
    The <fill_in> is from you to look up something specific. No need for the '<>' specifically 
 '''

def test_download():
    assert download() == 'Successful! Data has been downloaded \n'
	
def test_get_epochs():
    assert get_epochs() == logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide\n')

def test_get_epoch():
	assert get_epoch('test_value') == '   Requested epoch value: test_value was not found. Try again'

def test_get_sightings():
	assert get_sightings() == logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide\n')

def test_get_countries():
	assert get_countries() == logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide\n')

def test_get_country():
	assert get_country('Wano Kuny') == logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide\n')

def test_get_regions():
	assert get_regions() == logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide\n')

def test_get_regions_of_spec_country():
	assert get_regions_of_spec_country('spiderman') == logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide\n')

def test_get_region():
	assert get_region('marineford') == logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide\n')

def test_get_cities():
	assert get_cities('alabasta','arc') == logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide\n')

def test_get_city():
	assert get_city('gotham') == logging.error('Make sure to download the data. Use the curl localhost:5031/help -X POST and follow the intructions in the guide\n')
