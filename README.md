# WineBot - A web app wine recommender system :wine_glass: 
**Machine Learning Application**

Web-based wine review & recommender system using Django and Scikit-learn.
[Click here to the web app](http://dylankuo.pythonanywhere.com/reviews/)


### Technologies used:
>* Django+Bootstrap
>* Sqlite
>* Pandas
>* SciPy
>* Scikit-learn.
>* Algorithms Used for reccomendations: Clustering User Data and K-Means Clustering


### Prerequisites
You need to install these libraries listed in the requirement.txt
```
Django~=3.1
numpy~=1.19.1
Pandas~=1.1.0
SciPy~=1.5.2
Scikit-learn~=0.23.2
django-bootstrap4~=2.2.0
django-registration-redux~=2.8
```

### Installation
#### - Clone
Clone this repo to your local machine using git clone 

```bash
git clone https://github.com/dylan-kuo/wine-recommendation.git
```

#### - Create an admin user  
```bash
python manage.py createsuperuser
```

#### - Run the app
```bash
python manage.py runserver 
```

#### - Open up your browser and type in the url:
```bash
https://localhost:8000/reviews
```

## How it works:
This Recommender System (I call it WineBot) uses machine learning to determine which wine a user is most likely to try and serve them more of it, by finding wines that are liked by people with similar wine preferences.

- When users open WineBot for the first time, they are shown a list of 12 latest wine reviews & scores.

- Users need to register their own account first in order to get the wine suggestion.

- At first, WineBot will just return wines a user has never reviewed before.

- Once users leave review & score to wines. The algorithm will collect the data about the user and is able to map a user's preferences in relation to similar users and group them into "clusters" based on similar assigned scores of corresponding wines.

- Using machine learning, the algorithm sends wines to users based on their proximity to other clusters of users and won't send the one that the user already tried (ie. already left review & scores)

---

### Usage <br>

### 1. Register an account or log in an exisiting account. 

![The latest review list](https://github.com/dylan-kuo/wine-recommendation/blob/master/winebot/1.jpg)
![Register an account](https://github.com/dylan-kuo/wine-recommendation/blob/master/winebot/2.jpg) <br>

### 2. Go to wine list, leave a review and score. 

![Review & Score](https://github.com/dylan-kuo/wine-recommendation/blob/master/winebot/3.jpg) <br><br>

### 3. Click on the **Get Wine Suggestions!** button and you will be provided a list of wine suggestions by the algorithm. 

![Get recommendations](https://github.com/dylan-kuo/wine-recommendation/blob/master/winebot/4.jpg) <br>
---
#### The logic behind the clustering algorithms (K-means) for the recommendation system
This webapp can be a superb recommender without being an real wine expert! It just needs to find a person (other users on the webapp) with similar preferences to our friend. Then ask the second person for his favorite wines and suggest them to our first friend, not including those that our first friend have already tried. 

In order to do this task, you need to leave at least one review and give it a score (if not, the app will just recommend the items from all users). The app will pre-cluster all the users in the system by its wine reviews scores. By doing so we will have groups (clusters) of similar users. Then, when a user asks for recommendations, we will look for them in the cluster this user is in. (all the users in that cluster share the similar taste.) The app will provide the user suggestions other users in the same cluster have.


### Deployment
* [Wine Recommender Web App](http://dylankuo.pythonanywhere.com/reviews/) 

