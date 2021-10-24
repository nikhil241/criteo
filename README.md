# Criteo Assignment

## Technology Used 
* Flask 
* Flask Rest
* Used http://ip-api.com/json API for converting the IP to Geolocation and City(Also can be done by using somegeolocation DB but duet to timeconstraint used availabele API)

## How to Test
#### Python is required to run this project
Following are the command if python is already installed

* ```pip install -r requirements.txt```
* ```python app.py```
* It is a rest API application so parameters need to passed in the URL
so for example if the application is running on the port 5000 the url will be ```http://127.0.0.1:5000```

#### Parameter list
    * ip is optional if not given it will take the userIP and pass it to the request
    * city is required - the IP is valid or not it is checked according to the city provided
Example request

 ```http://localhost:5000/?ip=49.36.186.46&city=Delhi```

## How to Test already Deployed
This application is already deployed on Heroku so you can test it on the heroku url

Example request

```https://criteo-assignment.herokuapp.com/?ip=49.36.186.46&city=Delhi```