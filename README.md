# WelcomeToTheHood

## Author
Roy Rasugu 
  
## Description  
A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements.

##  Live Link  
 Click [View Site](https://wleomehood.herokuapp.com/)  to visit the site

 
## User Story  
  
* A user must sign in with the application to start using.
* A user can set up a profile about them.
* A user can find a list of different businesses in their neighborhood.
* A user can create posts that will be visible to everyone.
* A user can change their neighborhood when they decide to move out in their edit Profile. 
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/RoyRasugu/WelcomeToTheHood.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd project-awwards pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations blog
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 2.2](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com) 
* PSQL
* JS
* HTML
* CSS 
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information

You can reach me on my email [royratchizi@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2021 **Roy Rasugu**