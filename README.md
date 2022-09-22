# New Data Variables for Canadian Commercial Line Insurance


### Goal:
***
The overall aim of the project is to create new variables for Canadian businesses by leveraging different external data sources.

### Data Source Chosen
***
The data source chosen for this project is [Opentable.com](https://www.opentable.com)

### Techframework Used
***
The code is written in Python language

### Installation Required
***
- Chromedriver
- Selenium
- Pandas
- Numpy
- BeautifulSoup
- Time 
- os
- webdriver_manager.chrome
- multiprocessing

### List of variables extracted from restaurants on Opentable
***
- Name of Restaurant
- URL of [Opentable.com](https://www.opentable.com)
- Booked: number of times booked today via Opentable
- Rating
- Review Count: total number of reviews
- Price Range 
- Cuisine 
- Address, Google Address, location 
- cross street 
- neighborhood 
- public transit
- hours of operation 
- phone number 
- website 
- cuisines 
- dining style 
- dress code 
- parking details 
- payment options 
- additional 
- food,service, ambience, value rating 
- Noise Level 
- Top Tags, Loved for 
- No. of Photos 
- cleaning & sanitizing, protective equipment, screening, physical distancing 
- executive chef 
- entertainment 
- menu 
- catering 
- private party facilities, private party contact

### Data Processing
***
- Alcohol available: look for 'bar','beer','cocktails','wine' and 'corkage' in additional column of restauratant
- Wheelchair access: look for 'wheelchair'
- Outdoor seating: look for 'outdoor'
- Fireplace: look for 'fireplace'

### Functions Included
***
- main
- listings
- getinfo
- combine

### Input Required
***
- location id of [Opentable.com](https://www.opentable.com)
- cuisine id of [Opentable.com](https://www.opentable.com)

### listings() function
***
- scrape all restaurant names of urls of given cuisine and location
- will loop up to 10 times as Opentable has max 10 pages of results for each query

### getinfo() function
***
- scrape info of the restaurant giving the url from main

### combine() function
***
- combine all csv of the same region to a single csv
