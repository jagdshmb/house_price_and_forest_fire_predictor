# House_price_and_forest_fire_predictor
A simple localhost website to estimate the probable price of the house in Bengaluru and to predict the probability of fire 
occurance in the forest of a particular region.

## Steps to run the project:
1. Make sure you have Python installed( I used Python 3.6.5 for this project)
2. Clone this repository `https://github.com/jagdshmb/house_price_and_forest_fire_predictor.git`
3. Open the `command prompt` in the downloaded repository directory.
4. Create a virtual environment `virtualenv env`
     - You need to have "virtualenv" python package already installed. If not install it. `pip install virtualenv`
5. Activate the virtual environment. `.\env\Scripts\activate`
6. Install all the required python packages. `pip install -r requirements.txt`
7. Run the `server.py` file.
8. Open the `./server/templates/HomePage.html` in any browser.
9. Click on the corresponding house or forest fire image to predict the the house price or forest fire respectively.

## Recorded Video
[Click here](https://youtu.be/4rKFt5kgJ-Y) to see the working of web application.

## Dataset
1. House price prediction dataset --> [Kaggle website](https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data)
2. Forest fire prediction dataset --> [Created own data set](https://github.com/jagdshmb/house_price_and_forest_fire_predictor/blob/a9fcdf6edf8d54ffd1e332c74072f0219c993639/model/Forest_fire.csv)

## Text stack & Packages used:
1. Python (3.6.5)
2. HTML (UI)
3. CSS (UI)
4. JavaScript (UI to Python  and viceversa)
5. Flask (Web Framework)
