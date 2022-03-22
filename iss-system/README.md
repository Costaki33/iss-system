International Space Station (ISS) Positional and Sighting Data Application

The purpose of this application is to provide the user with a proper medium to analyize positional and sightings data for the International Space Station.
The user can access specific information related to the speed and various positions of the ISS at specific times throughout the country, region, or city.

## Table of Contents

#How To Download the Application
#How to Build Your Own DockerImage
#How to Use the Application
#Interpreting the Results
#Overall File Contents & Descriptions

## How to Download the Application

To use the application commands below, you need to download the specified Makefile from this repository. Alternatively, you can run the `docker` commands as shown below.

1. Pull the image from Docker Hub:
    - Type `make pull` in the CMD line of your powershell or, 
    - Type `docker pull costaki33/iss_system_get:1.0` in the CMD line2. Run the image
    - Type `make run` in the command line or  type `docker run --name "iss_system_get" -d -p 5031:5000 costaki33/iss_system_get:1.0`

2. You now have the image set up and running! Check out: `GUIDE: How to Use the Application` to see how to use this application with applicable routes

## How to Build Your Own DockerImage

To build your own docker image, you need to download the necessary files.

1. Download the Files:
    - Clone this repository using `git clone` to access all files required to build the image properly

2. Build the image from the provided Dockerfile:
    - `NAME="<username>" make build`
    - Alternatively, type `docker build -t <username>/iss_system_get:<tag> .` 
    - Make sure to replace the <> spaces with your own username and tag!

3. Download the data: 
    - Required data files: `ISS.OEM_J2K_EPH.xml` and `XMLsightingData_citiesUSA10.xml`
    - Download the data from this [link](https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq)
      - ISS.OEM_J2K_EPH.xml: which is under the link "Public Distribution"
      - XMLsightingData_citiesUSA10.xml

4. Running the image:
    - `NAME="<username>" make run`
    - Alternatively, type `docker run --name "iss_system_get" -d -p 5031:5000 <username>/iss_system_get:1.0`

5. The image is up and running, see the section below for a list of applicable routes:

## How to Interact with this Application

#### Applicable Routes:
  - `curl localhost:5031/help`
  - Run the command above, you should see the following output, which details the routes of the app:
    ```
    GUIDE: How to Interact with this application
    To use this application, you first need to download the data that this system supports. 
    Use the following command: 
        curl localhost:<your port number>/download -X POST\n
    
   After the dataset has been downloaded: you can access it through the application with the following routes:
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
    The <fill_in> is from you to look up something specific 
    ```
#### The Applicable Routes 

1. `/epochs`
    - Returns a list of dictionaries, where each dictionary is a complication of epoch
2. `/epochs/<get_epoch>`
    - This function takes in user input of an epoch, and returns the first dictionary whose key value matches the user's requested input
3. `/sightings`
    -     This function returns a list of dictionaries where each dictionary is a collection of sighting data
4. `/sightings/countries`
    -    This function returns a list of dictionaries, where each dictionary is a collection of country data as well as the number of times a metorite sighting occured in that specific country

5. `/sightings/<country>`
    -     This function takes in a country as the input from the input and returns a list of dictionaries, where each dictionary is a meteorite sighting in that specific country

6. `/sightings/countries/regions`
    - This function returns a dictionary, where the keys are all of the countries in the sightings data and the associative values are a 
    list of each region where a sighting occured in their respective country
7. `/sightings/<country>/region`
    -     This function, takes a specific country as user input and returns a dictionary, where the first key is the country given, and the value returned is a list of dictionaries. Each dictionary contains a region with the number of sightings within that region

8. `/sightings/region-<region>`
    -     This function takes in a region as the user input, and returns a list of dictionaries, where each dictionary is a sighting in that specific region

9. `/sightings/<country>-<region>-cities`
    -     This function takes a country & region as input, and returns a dictionary, where the [key] is the country provided, and the value is 
    another dictionary, where the:
                       
                        first key value pair = region 
                        second key-value pair = cities
10. `/sightings/city-<city>`
    -  This function takes in a city-name as the input, and returns a dictionary, where they [key] is 
    the city, and the value is a list of the data for sightings in that specific city

11. `/help`
    - Returns the user to the help guide 
  
## Interpretnghe Results

The following section holds an example command followed by their resulting output. Remember to first download the data before executing any commands: `curl localhost:5031/download -X POST`

### List of commands and their respective outputs
### /epochs
**EX OUT:** `curl localhost:5031/epochs` 
```
...
  {
    "EPOCH": "2022-057T12:00:00.000Z", 
    
      "#text": "", 
      "@units": "km"
    }, 
    "X_DOT": {
      "#text": "1.19203952554952", 
      "@units": "km/s"
    }, 
    "Y": {
      "#text": "-3625.9704508659102", 
      "@units": "km"
    }, 
    "Y_DOT": {
      "#text": "-5.67286420497775", 
      "@units": "km/s"
    }, 
    "Z": {
      "#text": "-2944.7433487186099", 
      "@units": "km"
    }, 
    "Z_DOT": {
      "#text": "4.99593211898374", 
      "@units": "km/s"
    }
  }
]
```
From the sample, we see that each epoch is defined by their key: "EPOCH". We can also see the position of the ISS in X, Y and Z coordinates, as well as its velocity in X, Y, and Z directions through the X_DOT, Y_DOT, and Z_DOT, respectively.


### /epochs/<get_epoch>

**EX OUT:**
```
{
  "EPOCH": "2022-042T12:04:00.000Z", 
  "X": {
    "#text": "-4483.2181885642003", 
    "@units": "km"
  }, 
  "X_DOT": {
    "#text": "2.63479158884966", 
    "@units": "km/s"
  }, 
  "Y": {
    "#text": "-4839.4374260438099", 
    "@units": "km"
  }, 
  "Y_DOT": {
    "#text": "-4.3774148889971602", 
    "@units": "km/s"
  }, 
  "Z": {
    "#text": "-1653.1850590663901", 
    "@units": "km"
  }, 
  "Z_DOT": {
    "#text": "5.7014974180323597", 
    "@units": "km/s"
  }
}
```
From the sample, we see the specifically requested epoch is defined by the key "EPOCH". We can see the information from the /epoch call

### /sightings

**EX OUT:**
```
...
  {
    "city": "Farmville", 
    "country": "United_States", 
    "duration_minutes": "2", 
    "enters": "11 above NW", 
    "exits": "10 above N", 
    "max_elevation": "11", 
    "region": "Virginia", 
    "sighting_date": "Fri Feb 25/05:42 AM", 
    "spacecraft": "ISS", 
    "utc_date": "Feb 25, 2022", 
    "utc_offset": "-5.0", 
    "utc_time": "10:42"
  }, 
  {
    "city": "Farmville", 
    "country": "United_States", 
    "duration_minutes": "< 1", 
    "enters": "11 above N", 
    "exits": "10 above NNE", 
    "max_elevation": "11", 
    "region": "Virginia", 
    "sighting_date": "Sat Feb 25/04:46 AM", 
    "spacecraft": "ISS", 
    "utc_date": "Feb 26, 2022", 
    "utc_offset": "-5.0", 
    "utc_time": "09:56"
  }
]
```
From the sample, you can analyze the information such as the city, country, etc. for each sighting.

### /sightings/countries

**EX OUT:**
```
[
  {
    "country": "United_States", 
    "numsightings": 3611
  }
]
```
From the example output above, we can see a list of all the countries in the dataset where the ISS was sighted, which here is the US. You can also see the number of occurances in that specific country.
### /sightings/\<country>
**EX OUT:**
```
...
  {
    "city": "Le_Grand", 
    "country": "United_States", 
    "duration_minutes": "2", 
    "enters": "18 above N", 
    "exits": "10 above NNE", 
    "max_elevation": "18", 
    "region": "California", 
    "sighting_date": "Thu Feb 24/05:01 AM", 
    "spacecraft": "ISS", 
    "utc_date": "Feb 24, 2022", 
    "utc_offset": "-8.0", 
    "utc_time": "13:01"
  }, 
  {
    "city": "Le_Grand", 
    "country": "United_States", 
    "duration_minutes": "< 1", 
    "enters": "9 above NNE", 
    "exits": "10 above NNE", 
    "max_elevation": "9", 
    "region": "California", 
    "sighting_date": "Fri Feb 25/04:15 AM", 
    "spacecraft": "ISS", 
    "utc_date": "Feb 25, 2022", 
    "utc_offset": "-8.0", 
    "utc_time": "12:15"
  }
]
```
From the example output above, we can see all the sightings that occurred in the country provided by the user. <br >

Link for you to go back to the [list of routes](#list-of-routes-for-you-to-easily-jump-to) <br >

### /sightings/countries/regions
**Example Command:** `curl localhost:5038/sightings/countries/regions` <br >

**Example Output:**
```
{
  "United_States": [
    "Alabama", 
    "Alaska", 
    "American_Samoa", 
    "Arizona", 
    "Arkansas", 
    "California"
  ]
}
```
From the example output above, we can see a key for every country where a sighting occurred. The value of that key is a list of all the regions within that country where a sighting occurred. In the case above, the only country were a sighting occurred was in the United States and the regions (states) where Alabama, Alaska, etc. <br >

Link for you to go back to the [list of routes](#list-of-routes-for-you-to-easily-jump-to) <br >

### /sightings/\<country>/regions
**Example Command:** `curl localhost:5038/sightings/united_states/regions` <br >

**Example Output:**
```
{
  "United_States": [
    {
      "numsightings": 698, 
      "region": "Alabama"
    }, 
    {
      "numsightings": 157, 
      "region": "Alaska"
    }, 
    {
      "numsightings": 6, 
      "region": "American_Samoa"
    }, 
    {
      "numsightings": 443, 
      "region": "Arizona"
    }, 
    {
      "numsightings": 1049, 
      "region": "Arkansas"
    }, 
    {
      "numsightings": 1258, 
      "region": "California"
    }
  ]
}
```
From the example output above, we can see the country the user requested as the first key in the dictionary, in this case United_States. Additionally, we can see a list of all the regions where a sighting occurred as well as the number of times a sightings occurred within that region. For example, we can see that the ISS was sighting in Arkansas 1049 times. <br >

Link for you to go back to the [list of routes](#list-of-routes-for-you-to-easily-jump-to) <br >

### /sightings/region-\<region>
**Example Command:** `curl localhost:5038/sightings/region-american_samoa` <br >

**Example Output:**
```
...
  {
    "city": "National_Park_of_American_Samoa", 
    "country": "United_States", 
    "duration_minutes": "6", 
    "enters": "10 above WSW", 
    "exits": "10 above N", 
    "max_elevation": "27", 
    "region": "American_Samoa", 
    "sighting_date": "Sun Feb 13/05:39 AM", 
    "spacecraft": "ISS", 
    "utc_date": "Feb 13, 2022", 
    "utc_offset": "-11.0", 
    "utc_time": "16:39"
  }, 
  {
    "city": "National_Park_of_American_Samoa", 
    "country": "United_States", 
    "duration_minutes": "3", 
    "enters": "48 above N", 
    "exits": "10 above NNE", 
    "max_elevation": "48", 
    "region": "American_Samoa", 
    "sighting_date": "Mon Feb 14/04:55 AM", 
    "spacecraft": "ISS", 
    "utc_date": "Feb 14, 2022", 
    "utc_offset": "-11.0", 
    "utc_time": "15:55"
  }
]
```
From the example output above, we can see a list of all the sightings that occurred within the American Samoa region. <br >

Link for you to go back to the [list of routes](#list-of-routes-for-you-to-easily-jump-to) <br >

### /sightings/\<country>-\<region>-cities
**Example Command:** `curl localhost:5038/sightings/united_states-alaska-cities` <br >

**Example Output:**
```
{
  "United_States": {
    "citiesinregion": [
      "Alagnak_National_Wild_and_Scenic_River", 
      "Anchorage", 
      "Aniakchak_National_Monument", 
      "Aniakchak_National_Preserve", 
      ...
      "Wrangell_St_Elias_National_Preserve", 
      "Wrangell_St_Elias_Park_and_Wilderness", 
      "Wrangell_St_Elias_Preserve_and_Wilderness", 
      "Yakutat"
    ], 
    "region": "Alaska"
  }
}
```
From the example output above, we can see a list of all the cities within the requested region and country where the ISS was sighted. For example, we can see that the ISS was sighted in Anchorage, Alaska. <br >

Link for you to go back to the [list of routes](#list-of-routes-for-you-to-easily-jump-to) <br >

### /sightings/city-\<city>
**Example Command:** `curl localhost:5038/sightings/city-arkansas_city` <br >

**Example Output:**
```
...
    {
      "city": "Arkansas_City", 
      "country": "United_States", 
      "duration_minutes": "2", 
      "enters": "19 above NNW", 
      "exits": "10 above NNE", 
      "max_elevation": "19", 
      "region": "Arkansas", 
      "sighting_date": "Tue Feb 22/05:28 AM", 
      "spacecraft": "ISS", 
      "utc_date": "Feb 22, 2022", 
      "utc_offset": "-6.0", 
      "utc_time": "11:28"
    }, 
    {
      "city": "Arkansas_City", 
      "country": "United_States", 
      "duration_minutes": "< 1", 
      "enters": "12 above NNE", 
      "exits": "10 above NNE", 
      "max_elevation": "12", 
      "region": "Arkansas", 
      "sighting_date": "Wed Feb 23/04:42 AM", 
      "spacecraft": "ISS", 
      "utc_date": "Feb 23, 2022", 
      "utc_offset": "-6.0", 
      "utc_time": "10:42"
    }
  ]
}
```
From the example output above, we can see all the sightings of the ISS that occurred in Arkansas City. <br >

Link for you to go back to the [list of routes](#list-of-routes-for-you-to-easily-jump-to) <br >

## File Descriptions

### Scripts
1. `app.py`
    - Main application script 
    - Contains POST endpoint to load the data into memory in order to query the data
    - Contains all the GET routes the user can use to query data
3. `test_app.py`
    - Tests all routes in the previous script for error handling

### Data Files
1. `ISS.OEM_J2K_EPH.xml`
    - Contains the specific, time, position, and velocity data for the ISS
2. `XMLsightingData_citiesUSA01.xml`
    - Contains the sightings of the ISS within the United States
    - Contains the specific time, country (United States), region (state), and city the sighting took place

The ISS data above was taken from NASA's official website found [here](https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq).
