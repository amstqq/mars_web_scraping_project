# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars as mtm

app = Flask(__name__)

# Create connection variable
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

# Index page
@app.route("/")
def index():
    # Store the mars data dictionary scraped into result
    result = mongo.db.collection.find_one()

    # return template and data
    return render_template("index.html", result=result)

# Scrape page
@app.route("/scrape")
def scraper():
    # Drop the information scraped last time
    mongo.db.drop_collection("collection")

    # Run scrape function and store the dictionary into a new dict
    mars_dict = mtm.scrape()
    mars_info = {
        "news_title":mars_dict['news_title'],
        "news_p":mars_dict['news_p'],
        "featured_image_url":mars_dict['featured_image_url'],
        "mars_weather":mars_dict['mars_weather'],
        "mars_facts":mars_dict['mars_facts'],
        "hemis_list":mars_dict['hemis_list']
        }

    # Insert the data into mongo database
    mongo.db.collection.insert_one(mars_info)
    # Redirect to index page after scraping
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=False)
