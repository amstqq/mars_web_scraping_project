# mars_web_scraping_project

This project has two parts. The first part uses BeautifulSoup and Splinter to build a function in Python that scrapes various websites for data related to Mars and stores the collected information into a Python dictionary. The second part uses MongoDB with Flask templating to build a web application that displays the information collected in a Bootstrap page.

## Required Python packages

- splinter
- bs4, BeautifulSoup
- pandas
- flask
- PyMongo

## Navigation
- app.py is the flask application.
- mission_to_mars.py contains the code to scrape data from mars websites.
- Inside templates folder contains the website used to display scraped data. The website is built using Bootstrap.

## Part 1: Scraping

- Scrape [NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) and collect the lastest news title and paragraph text.
- Scrape [Jet Propulsion Laboratory](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) and collect the url to its featured space image.
- The latest Mars weather data is scraped from [Mars Weather twitter account](https://twitter.com/marswxreport?lang=en).
- A table of Mars facts is scraped from [Space Facts](https://space-facts.com/mars/).
- Visit the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars). The full image url rests under the link titled by each individual hemisphere name.
- Build a function to collect all the information and return a Python dictionary of results.

## Part 2: MongoDB and Flask Application

- Create a route `/scrape` using Flask that calls the above mentioned scrape funtion and stores the results in Mongo database.
- The root route `/` queries the Mongo Database and pass the mars data into an HTML template to display the data.
- The template HTML file `index.html` displays the mars data in appropriate locations. The HTML template is built using Bootstrap.

## Instructions for Accessing the Website

Store the repository in your local computer. Double-click on `app.py` and, if run correctly, the last line should read: `Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`. Open your browser and type `http://127.0.0.1:5000/` to see the website.

Click on `Scrape` button on the top of the webpage and wait for approximately one minute for the data to be collected. Then, you should be able to see the latest information displayed on the site.

