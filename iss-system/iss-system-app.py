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

app = Flask(__name__)

@app.route('/download_data', methods= ['POST'])
def download_data(): 
    global sighting_data
    global position_data

    with open('XMLsightingData_citiesUSA10.xml', 'r') as f:
        sighting_data = xmltodict.parse(f.read())

    with open('ISS.OEM_J2K_EPH.xml', 'r') as g:
        positon_data = xmltodict.parse(g.read())

    return 'Data has been downloaded \n'
    























if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
