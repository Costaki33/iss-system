SS Positional and Sighting Data Application

The purpose of this application is to provide the user with various positional and sightings data for the International Space Station (ISS).
Specifically, the user can access information related to the position and velocity of the ISS at specific times as well as the country, region, or city
the ISS was sighted in at specific times.

## Table of Contents

[How to Download the Pre-built Code](#how-to-download-the-pre-built-code) <br >
[How to Build Your Own Image](#how-to-build-your-own-image)<br >
[How to Interact with the Application](#how-to-interact-with-the-application)<br >
[Interpret the Results](#interpret-the-results)<br >
[File Descriptions](#file-descriptions)<br >

## How to Download the Pre-built Code

To use the `make` commands below, you need to download the Makefile from this repository. Alternatively, you can run the `docker` commands
as shown below.

1. Pull the image from Docker Hub
    - Type `make pull` in the command line
    - Alternatively, you can type `docker pull ianwood314/iss-data-query:1.1` in the command line (which is the same command executed by `make pull`)
2. Run the image
    - Type `make run` in the command line
    - Alternatively, type `docker run --name "iss-query-data" -d -p 5038:5000 ianwood314/iss-data-query:1.1` (again, the same command executed by `make run`)
3. Now that you have the image up and running, see the [How to Interact with the Application](#how-to-interact-with-the-application) section for a list of queryable routes

## How to Build Your Own Image
1. Download the Necessary Files
    - Clone this repository using `git clone` to access all files required to build the image (learn how to clone a repository [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))
2. Build the image from the Dockerfile
    - `NAME="<username>" make build`
    - Alternatively, type `docker build -t <username>/iss-data-query:<tag> .` (remember to replace with your own username and tag)
3. Download the data 
    - Required data files: `ISS.OEM_J2K_EPH.xml` and `XMLsightingData_citiesUSA01.xml` (a description of these files is available in the [Data Files](#data-files) section)
    - Download the data [here](https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq)
      - `ISS.OEM_J2K_EPH.xml`: under link "Public Distribution"
      - `XMLsightingData_citiesUSA01.xml`: under link "XMLsightingData_citiesUSA01"
5. Run the image
    - `NAME="<username>" make run`
    - Alternatively, type `docker run --name "iss-query-data" -d -p 5038:5000 <username>/iss-data-query:1.1`
6. Now that you have the image up and running, see the section below for a list of queryable routes

## How to Interact with the Application

NOTE: for the sections below, a port number of 5038 is used.

#### View a list of all the queryable routes
  - `curl localhost:5038`
  - Once you run the command above, you should see the following output:
    ```
    -- How to Interact with this Application --

    In order to access the data, you must first download it:
       curl localhost:<your port #>/download-data -X POST

    Once the data is downloaded, you can access it through the following routes:
      1.  /epochs
      2.  /epochs/<requested_epoch>
      3.  /sightings
      4.  /sightings/countries
      5.  /sightings/<country>
      6.  /sightings/countries/regions
      7.  /sightings/<country>/regions
      8.  /sightings/region-<region>
      9.  /sightings/<country>-<region>-cities
      10. /sightings/city-<city>
    ```
  - Output above details how to download the data and provides a list of the ten queryable routes

#### Brief description of each queryable route

NOTE: each output is in the class `~flask.Response` 

1. `/epochs`
    - Returns a list of dictionaries where each dictionary is an epoch
2. `/epochs/<requested_epoch>`
    - Takes in user input of an epoch and returns the first dictionary whose EPOCH key value matches the user's input
3. `/sightings`
    - Returns a list of dictionaries where each dictionary is a sighting of the ISS
4. `/sightings/countries`
    - Returns a list of dictionaries where each dictionary is a country along with the number of times a sighting occurred in that country
5. `/sightings/<country>`
    - Takes in a country as user input and returns a list of dictionaries where each dictionary is a sighting in that country
6. `/sightings/countries/regions`
    - Returns a dictionary where the keys are all of the countries in the sightings data and the values are a list of the regions where a sighting occurred in that country
7. `/sightings/<country>/regions`
    - Takes in a country as user input and returns a dictionary where the first and only key is the country given and the value is a list of dictionaries where each dictionary is a region with the number of sightings within that region
8. `/sightings/region-<region>`
    - Takes in a region as user input and returns a list of dictionaries where each dictionary is a sighting in the region provided by the user
9. `/sightings/<country>-<region>-cities`
    - Takes a country and region as user input and returns a dictionary where the key is the country provided and the value is another dictionary where the first key value-pair is the region provided and the second key-value pair are the cities located in that country and region
10. `/sightings/city-<city>`
    - Takes in a city name as user input and returns a dictionary where they key is the city provided and the value is a list of all the data for sightings in that city
  
## Interpret the Results

The following sections display an example command and the resulting output. Remember to first download the data before executing any of the commands below: `curl localhost:5038/download-data -X POST`

### List of routes for you to easily jump to:
[/epochs](#epochs) <br >
[/epochs/<requested_epoch>](#epochsrequested_epoch) <br >
[/sightings](#sightings) <br >
[/sightings/countries](#sightingscountries) <br >
[/sightings/\<country>](#sightingscountry) <br >
[/sightings/countries/regions](#sightingscountriesregions) <br >
[/sightings/\<country>/regions](#sightingscountryregions) <br >
[/sightings/region-\<region>](#sightingsregion-region) <br >
[/sightings/\<country>-\<region>-cities](#sightingscountry-region-cities) <br >
[/sightings/city-\<city>](#sightingscity-city)

### /epochs
**Example Command:** `curl localhost:5038/epochs` <br >

**Example Output:**
```
...
  {
    "EPOCH": "2022-057T12:00:00.000Z", 
    "X": {
      "#text": "6626.5027288478996", 
      "@units": "km"
    }, 
    "X_DOT": {
      "#text": "-0.48760287876274999", 
      "@units": "km/s"
    }, 
    "Y": {
      "#text": "-824.23928357807699", 
      "@units": "km"
    }, 
    "Y_DOT": {
      "#text": "4.9312583060242199", 
      "@units": "km/s"
    }, 
    "Z": {
      "#text": "-1255.3633426653601", 
      "@units": "km"
    }, 
    "Z_DOT": {
      "#text": "-5.8454326130222896", 
      "@units": "km/s"
    }
  }
]
```
From the example output above, we can see that each epoch is defined by the key "EPOCH". Additionally, we can see the  position of the ISS in cartesian coordinates from the X, Y and Z keys as well as its velocity in X, Y, and Z directions given by X_DOT, Y_DOT, and Z_DOT, respectively. <br >

Link for you to go back to the [list of routes](#list-of-routes-for-you-to-easily-jump-to) <br >

### /epochs/<requested_epoch>
**Example Command:** `curl localhost:5038/epochs/2022-057T11:28:56.869Z` <br >

**Example Output:**
```
{
  "EPOCH": "2022-057T11:28:56.869Z", 
  "X": {
    "#text": "-2986.4186115953698", 
    "@units": "km"
  }, 
  "X_DOT": {
    "#text": "6.6940352721911403", 
    "@units": "km/s"
  }, 
  "Y": {
    "#text": "-3351.8103353889501", 
    "@units": "km"
  }, 
  "Y_DOT": {
    "#text": "-3.2941899081049599", 
    "@units": "km/s"
  }, 
  "Z": {
    "#text": "5093.8109194735598", 
    "@units": "km"
  }, 
  "Z_DOT": {
    "#text": "1.74823024507643", 
    "@units": "km/s"
  }
}
```
From the example output above, we can see that the requested epoch is defined by the key "EPOCH". Additionally, we can see the  position of the ISS in cartesian coordinates from the X, Y and Z keys as well as its velocity in X, Y, and Z directions given by X_DOT, Y_DOT, and Z_DOT, respectively. For example, we can see that the ISS was traveling at 6.694 km/s in the x-direction. <br >

Link for you to go back to the [list of routes](#list-of-routes-for-you-to-easily-jump-to) <br >

### /sightings
**Example Command:** `curl localhost:5038/sightings` <br >

**Example Output:**
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
From the example output above, we can see that locational information such as city, country, etc. is provided for each sighting. Additionally, we can see the time and elevation of the sighting. <br >

Link for you to go back to the [list of routes](#list-of-routes-for-you-to-easily-jump-to) <br >

### /sightings/countries
**Example Command:** `curl localhost:5038/sightings/countries` <br >

**Example Output:**
```
[
  {
    "country": "United_States", 
    "numsightings": 3611
  }
]
```
From the example output above, we can see a list of all the countries in the dataset where the ISS was sighted as well as the number of times the ISS was sighted within that country. For example, we can see that the ISS was sighted in the United States 3611 times. <br >

Link for you to go back to the [list of routes](#list-of-routes-for-you-to-easily-jump-to) <br >

### /sightings/\<country>
**Example Command:** `curl localhost:5038/sightings/united_states` <br >

**Example Output:**
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
