from flask import Flask, render_template, redirect, url_for
import pymongo
import scrape_mars
from pprint import pprint

print("hello")
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
conn="mongodb://localhost:27017"
mongo = pymongo.MongoClient(conn)

print("hatim",mongo.mars_app_db)
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update_one({}, {"$set": mars_data}, upsert=True)
    return redirect('/', code=302)


if __name__ == "__main__":
    app.run(debug=True)
