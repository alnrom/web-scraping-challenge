from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars"
mongo = PyMongo(app)

@app.route("/")
def index():

    redplanet_col = mongo.db.news
    redplanet = redplanet_col.find_one()

    feat_image_col = mongo.db.ft_image
    feat_image = feat_image_col.find_one()
    
    hemi_first = mongo.db.first
    hemi_zero = hemi_first.find_one()

    hemi_second = mongo.db.second
    hemi_one = hemi_second.find_one()

    hemi_third = mongo.db.third
    hemi_two = hemi_third.find_one()

    hemi_fourth = mongo.db.fourth
    hemi_three = hemi_fourth.find_one()

    mars_data = scrape_mars.scrape_mars()
    featured_image = scrape_mars.feature_img()
    facts = scrape_mars.table_facts()
    hemi_photos = scrape_mars.hemispheres_images() 

    redplanet_col.update({}, mars_data, upsert=True)
    feat_image_col.update({}, featured_image, upsert=True)
    hemi_first.update({}, hemi_photos[0], upsert=True)
    hemi_second.update({}, hemi_photos[1], upsert=True)
    hemi_third.update({}, hemi_photos[2], upsert=True)
    hemi_fourth.update({}, hemi_photos[3], upsert=True)

    return render_template("index.html", redplanet=redplanet, feat_image=feat_image, \
                            facts=facts, hemi_zero=hemi_zero, hemi_one=hemi_one, \
                            hemi_two=hemi_two, hemi_three=hemi_three)
    


if __name__ == "__main__":
    app.run(debug=True)