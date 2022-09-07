#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Dependencies

from bs4 import BeautifulSoup
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import pandas as pd
import warnings
import re
warnings.filterwarnings('ignore')


# In[2]:


# Setup Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless= False)


# In[3]:


# News url to be scraped

news_url = 'https://redplanetscience.com/'

# Test response
response = requests.get(news_url)
# response

# Visit url and convert browser to html
browser.visit(news_url)
news_html = browser.html

# Create BS object to pasre the html, use html.parser
news_soup = BeautifulSoup(news_html, 'html.parser')
# print(news_soup)

# Find latest News Title and Paragraph text, assign to variables for later use

# Look for: div with 'content_title' class for News Title
title = news_soup.find('div', class_= 'content_title')
news_title = ''

for t in title: 
#     print(t)
    news_title += str(t)
    
# Look for: div with 'article_teaser_body' class for paragraph text
p_text = news_soup.find('div', class_= 'article_teaser_body')
news_p = ''

for np in p_text: 
#     print(np)
    news_p += str(np)


# In[4]:


# Space images url to be scraped

space_imageURL = 'https://spaceimages-mars.com/'

# Visit url and convert browser to html
browser.visit(space_imageURL)
space_imageHTML = browser.html

# Create BS object to pasre the html, use html.parser
space_image_soup = BeautifulSoup(space_imageHTML, 'html.parser')
# print(space_image_soup)


# Find image URL for Featured Mars Image

image_href = space_image_soup.find('div', class_='floating_text_area' )
# print(image_href.a['href'])
featured_image_url = f"{space_imageURL + image_href.a['href']}"
featured_image_url



# <div class="floating_text_area">
# <h2 class="brand_title">FEATURED IMAGE</h2>
# <h1 class="media_feature_title">Dusty Space Cloud</h1>
# <br/>
# <a class="showimg fancybox-thumbs" href="image/featured/mars2.jpg" target="_blank"> <button class="btn btn-outline-light"> FULL IMAGE</button></a>
# </div>


# In[5]:


# Galaxyfacts- mars url to be scraped

facts_url = 'https://galaxyfacts-mars.com/'

# Read html 
facts_table = pd.read_html(facts_url)
# facts_table


# Check facts_table type
type(facts_table)


# Convert both tables into a Pandas DF
facts_comparisonDF = facts_table[0]
# facts_comparisonDF.head(10)

facts_marsDF = facts_table[1]
# facts_marsDF.head(10)


# -----------------------------------------------------------
# <div class="sidebar">
# <h5>MARS PLANET PROFILE</h5>
# <table class="table table-striped">
# # Visit url and convert browser to html
# browser.visit(facts_url)
# facts_html = browser.html

# # Create BS object to pasre the html, use html.parser
# facts_soup = BeautifulSoup(facts_html, 'html.parser')
# # print(facts_soup)


# In[6]:


# Clean facts_comparisonDF, fix header

# Grab first row for the header
header1 = facts_comparisonDF.iloc[0]

# Take the data less the header row
facts_comparisonDF = facts_comparisonDF[1:]

# Set the header row as the df header
facts_comparisonDF.columns = header1

# Reset index and drop columns
facts_comparisonDF.reset_index(inplace= True)
facts_comparisonDF.drop(columns= 'index', inplace= True)
facts_comparisonDF


# In[7]:


# Clean facts_marsDF, fix header

# Grab first row for the header
header2 = facts_marsDF.iloc[0]

# Take the data less the header row
facts_marsDF = facts_marsDF[1:]

# Set the header row as the df header
facts_marsDF.columns = header2

# Reset index and drop columns
facts_marsDF.reset_index(inplace= True)
facts_marsDF.drop(columns= 'index', inplace= True)
facts_marsDF


# In[17]:


# Mars hempispheres url to be scraped
marsURL = 'https://marshemispheres.com/'

# Visit url and convert browser to html
browser.visit(marsURL)
marsHTML = browser.html

# Create BS object to parse the html, use html.parser
mars_soup = BeautifulSoup(marsHTML, 'html.parser')
# print(mars_soup.prettify)

# Find title and image href
mars_results = mars_soup.find_all('div', class_= 'item')
# mars_results


# Loop thru mars_results to find title and full resolution imageURL
mars_title = []
mars_imageURL = []
# mars_href = []

for r in mars_results:
    
#   Find title, 'h3'
    h3 = r.find_all('h3')
    mars_title += h3
#     time.sleep(2)


    # Find the a tag in each class
    a = r.find_all('a')
    
    # Get the html in href
    href = a[0]['href']
    
    # Join sepearte indices together to make one html
    href = list(href[0:])
    href = [''.join(href[0:])]
    time.sleep(2)
#     print(href)


    # Loop each link to find image url
    for ref in href:
        
        # Scrape each link
        outlink_url = f"{marsURL+ref}"
        
        # Visit each url and convert browser to html
        browser.visit(outlink_url)
        outlinkHTML = browser.html
        
        # Create BS to parse each html
        outlink_soup = BeautifulSoup(outlinkHTML, 'html.parser')
        
        # Get image url
        outlink_results = outlink_soup.find_all('div', class_= 'downloads')
#         print(outlink_results)

        # Set timer
        time.sleep(2)
        
      
        for o in outlink_results:
            a_tag = o.find_all('a')
            image_href = a_tag[0]['href']
            
            # Join seperated indices together to make 1 index
            image_href = list(image_href[0:])
            image_href = [''.join(image_href[0:])]
            
            # Append image to empty list
            mars_imageURL += image_href
            
            # Set timer
            time.sleep(2)

# browser.quit()


# In[9]:


mars_imageURL


# In[10]:


mars_title


# In[11]:


# Remove tags from mars_title
title_cleaned = []

for i in range(0,4):
    
    # Remove tags
    clean = (mars_title[i]).get_text()
    
    # Join individual indices into a value
    clean = list(clean[0:])
    clean = [''.join(clean[0:])]
    
    # Append to new list, title_cleaned
    title_cleaned += clean
    
title_cleaned

marstitles_new = [word.replace('Enhanced','') for word in title_cleaned]
marstitles_new


# In[15]:


# Append marsURL to mars_imageURL
mars_imageURL_cleaned = []

for m in range(0, 4):
    
    # Combine original url and image url
    clean2 = f"{marsURL + mars_imageURL[m]}"
    
    # Join individual indices into a value
    clean2 = list(clean2[0:])
    clean2 = [''.join(clean2[0:])]
    
    mars_imageURL_cleaned += clean2
    
mars_imageURL_cleaned


# In[16]:


# Create a Dictionary from marstitles_new and mars_imageURL_cleaned

hempisphere_image_urls = [
    {"title": marstitles_new[0], "img_url": mars_imageURL_cleaned[0]},
    {"title": marstitles_new[1], "img_url": mars_imageURL_cleaned[1]},
    {"title": marstitles_new[2], "img_url": mars_imageURL_cleaned[2]},
    {"title": marstitles_new[3], "img_url": mars_imageURL_cleaned[3]}
]
hempisphere_image_urls


# In[14]:


# -----------------------------------------------
# <div class="collapsible results">
# <div class="item">
# <a class="itemLink product-item" href="cerberus.html"><img alt="Cerberus Hemisphere Enhanced thumbnail" 
# class="thumb" src="images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png"/></a>
# <div class="description">
# <a class="itemLink product-item" href="cerberus.html">
# <h3>Cerberus Hemisphere Enhanced</h3>
# </a>

# <div id="wide-image" class="wide-image-wrapper " style="max-height: 1296px;">

#<div class="downloads">
#<img class="thumb" src="images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png">
#</div>

#<img class="wide-image" src="images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg">
#<a id="wide-image-toggle" class="open-toggle" href="#open">Close</a>
#</div>

# -----------------------------------------------
    # [<div class="downloads">
    # <img class="thumb" src="images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png"/>
    # <h3>Download</h3><ul>
    # <li><a href="images/schiaparelli_enhanced-full.jpg" target="_blank">Sample</a> (jpg) 1024px wide</li>
    
#     <li><a href="images/full.jpg" target="_blank">Sample</a> (jpg) 1024px wide</li>

