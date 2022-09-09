from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    # find one document from our mongo db and return it.
    mars_data = mongo.db.mars.find_one()
    # pass that mars_data to render_template
    return render_template("index.html", mars=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    scrape_mars_data = scrape_mars.scrape_mars_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars.update_one({}, {"$set": scrape_mars_data}, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
