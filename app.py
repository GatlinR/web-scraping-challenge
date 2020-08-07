{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "from pymongo import MongoClient\n",
    "import scrape_mars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mission_to_mars\"\n",
    "mongo = PyMongo(app)\n",
    "mongo.db.mars_data.drop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def index():\n",
    "    mars_db = mongo.db.mars_data.find_one()\n",
    "    return render_template(\"index.html\", mars=mars_db)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "    mars_col = mongo.db.mars_col\n",
    "    mars_data = scrape_mars.scrape()\n",
    "    mars_col.update({}, mars_data, upsert=True)\n",
    "\n",
    "    return redirect(\"/\", code=302)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
