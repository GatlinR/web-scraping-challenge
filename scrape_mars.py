{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape():\n",
    "    \n",
    "    mars_dict = {}\n",
    "    \n",
    "    executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "    \n",
    "    url1 = 'https://mars.nasa.gov/news/'\n",
    "    browser.visit(url1)\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    \n",
    "    news_title = soup.find('div', class_='content_title').text\n",
    "    news_p = soup.find('div', class_='article_teaser_body').text\n",
    "    \n",
    "    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "    browser.visit(url2)\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    \n",
    "    browser.links.find_by_partial_text('FULL IMAGE').click()\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    \n",
    "    img_url = soup.find_all('img', class_='fancybox-image')[0]['src']\n",
    "    featured_image_url = f'https://www.jpl.nasa.gov{img_url}'\n",
    "    \n",
    "    url3 = 'https://twitter.com/marswxreport?lang=en'\n",
    "    browser.visit(url3)\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    \n",
    "    mars_weather = soup.find('article').text\n",
    "    mars_weather = mars_weather.replace('Mars Weather@MarsWxReport·15h', '')\n",
    "    \n",
    "    url4 = 'https://space-facts.com/mars/'\n",
    "    mars_table = pd.read_html(url4)\n",
    "    mars_df = mars_table[0]\n",
    "    table_string = mars_df.to_html()\n",
    "    \n",
    "    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "    browser.visit(url5)\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    \n",
    "    hemispheres = soup.find_all('div', class_='item')\n",
    "    hemisphere_image_urls = []\n",
    "\n",
    "    for hemisphere in hemispheres:\n",
    "        image = hemisphere.find('a', class_='itemLink product-item')['href']\n",
    "        title = hemisphere.find('h3').text\n",
    "        full_url = 'https://astrogeology.usgs.gov' + image\n",
    "        browser.visit(full_url)\n",
    "        html2 = browser.html\n",
    "        soup2 = BeautifulSoup(html2, 'html.parser')\n",
    "        img_url = 'https://astrogeology.usgs.gov' + soup2.find(\"img\", class_=\"wide-image\")[\"src\"]\n",
    "        hemisphere_image_urls.append({'title': title, 'img_url': img_url})\n",
    "    \n",
    "    mars_dict['news_title'] = news_title\n",
    "    mars_dict['news_p'] = news_p\n",
    "    mars_dict['featured_image_url'] = featured_image_url\n",
    "    mars_dict['mars_weather'] = mars_weather\n",
    "    mars_dict['mars_df'] = mars_df\n",
    "    mars_dict['table_string'] = table_string\n",
    "    mars_dict['hemisphere_image_urls'] = hemisphere_image_urls \n",
    "    \n",
    "    return mars_dict\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
