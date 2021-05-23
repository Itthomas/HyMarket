# HyMarket
## Overview
This web application allows players of Minecraft: Hypixel Skyblock to easily review real-time market data for Skyblock's in-game economy. The app was created using the Django
framework and Python. The purpose for me writing this software is to learn how to use the Django framework, as it is my first time using it. Because it was purely educational
the website is not published under a public domain. To access the website from your local machine you must open a terminal window, navigate to the HyMarket directory (which 
contains the manage.py file), and run the command `python manage.py runserver`. when the server is running you can navigate to the web-app in a browser by navigating to 
[http://127.0.0.1:8000/](http://127.0.0.1:8000/). This will take you to the homepage of the HyMarket website where you will see the header with navigation links, a greeting 
message, and search bars for both the baazar and auctions.

## Web Pages

Each web page on HyMarket has the same header, and the header contains a navigation bar with links to Home, Baazar, and Auctions. The home page is simple, the body 
contains a greeting and two search bars for both the baazar market and auction market. On the baazar page each item loads into a little box which contains the name of the item
and some basic details about prices and order volumes. Each of these boxes are populated with information from the Hypixel API when the page loads. At the top of the body is
another search bar to filter baazar items by name. If the user clicks on an item box they are redirected to a dynamically generated URL which takes them to a page with more 
detailed market data for the item they clicked. The auctions page is very similar to the baazar page, it has item boxes with thousands of items that players have put up for
sale. Each box has inportant information about each auction, and there is a search bar at the top of the page which creates dynamic URLs to filter the results.

## Development Environment

I used Visual Studio Code as my IDE. The main tool in this project is the Django framework, which makes everything possible. I used a virtual environment to house Django and 
all other imports and installations. The other library I used was Requests to request the json data from the Hypixel API. Python was the language I used for the backend 
development, and I used HTML/CSS for the front-end.

## Demonstration Video
[Django Python Web App Demo | HyMarket](https://youtu.be/RKL6S4uGJZ8)

## Useful Websites

* [Django Documentation](https://docs.djangoproject.com/)
* [Django Full Course for Beginners | Free Code Camp](https://www.freecodecamp.org/news/python-django-course/)
* [HTML and CSS Course | Free Code Camp](https://www.freecodecamp.org/news/html-and-css-course/)
* [StackOverflow](https://stackoverflow.com/) (of course)
* [w3 schools](https://www.w3schools.com/)

## Future Work

* More search filters and criteria
* Store price history for each item in a database
* display historical price data on interactive graphs and charts
