# Mission to Mars!

The purpose of this challenge is to demonstrate web scraping skills from various websites for data related to Mars and displaying found data in an HTML page as well as loading data into a MongoDB collection. 

## Instructions: 
 
### Part 1 Scraping: 

* Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

* Visit the URL for the Featured Space Image site [here](https://spaceimages-mars.com).
    * Use Splinter to navigate the site and find the image URL for the current Featured Mars Image, then assign the URL string to a variable called `featured_image_url`.

* Visit the [Mars Facts webpage](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including diameter, mass, etc and convert into an HTML table string. 

* Visit the [astrogeology site](https://marshemispheres.com/) to obtain high-resolution images for each hemisphere of Mars.

    * You will need to click each of the links to the hemispheres in order to find the image URL to the full-resolution image.

    * Save the image URL string for the full resolution hemisphere image and the hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

    * Append the dictionary with the image URL string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


### Part 2 MongoDB and Flask Application: 

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` by using a function called `scrape`. This function should  execute all your scraping code from above and return one Python dictionary containing all the scraped data.

* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the Mars data into an HTML template for displaying the data.

* Create a template HTML file called `index.html` that will take the Mars data dictionary and display all the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.


### Results: Screenshots

![mars_index.html](screenshots/mars_html.jpg)