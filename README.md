# Urban Explorer: Machine Learning-Driven Discoveries

**Table of Contents:**
- [Project Overview](#project-overview)
- [Project Goals](#project-goals)
- [Approach](#approach)
- [Data](#data)
- [Notebooks](#notebooks)
- [Technologies Used](#technologies-used)
- [Conclusion and Next Steps](#conclusion-and-next-steps)

## Project Overview
Urban Explorer leverages machine learning to provide personalized recommendations for dining and activities, transforming how users discover new experiences in their city or while traveling. This project, conducted during my capstone for BrainStation's bootcamp, enhances decision-making for users who face indecision about where to eat or what to do, especially in unfamiliar locales.

## Project Goals
- To offer tailored recommendations for restaurants and activities.
- To address the needs of users looking for inspiration or guidance in choosing dining spots and engaging in local activities.
- To improve upon existing recommendation systems by providing more personalized and dynamic suggestions.

## Approach
### Data Preparation
Conducted extensive Exploratory Data Analysis (EDA) and preprocessing on restaurant data, user ratings, and activity data across a dozen cities, focusing on ensuring data quality by filtering for well-reviewed businesses and active users.

### Model Development
Utilized Funk SVD modeling to factorize user-business rating matrices into latent factors, capturing the preferences and attributes that drive personalized recommendations.

### Model Training and Evaluation
Data was split into training and test sets to refine accuracy, employing RMSE as the primary evaluation metric to measure performance and guide improvements.

## Data
To replicate this project, download the dataset used from the Yelp Dataset page at [Yelp Dataset](https://www.yelp.com/dataset).

### Data Dictionaries

#### Business Data Set
| Field         | Description                                         |
|---------------|-----------------------------------------------------|
| business_id   | Unique identifier for the business                  |
| name          | Name of the business                                |
| address       | Address of the business                             |
| city          | City where the business is located                   |
| state         | State where the business is located                 |
| postal_code   | Postal code of the business location                |
| latitude      | Latitude coordinate of the business                 |
| longitude     | Longitude coordinate of the business                |
| stars         | Average star rating of the business                 |
| review_count  | Number of reviews received by the business          |
| is_open       | 1 if the business is open, 0 otherwise              |
| attributes    | Attributes associated with the business             |
| categories    | Categories associated with the business             |
| hours         | Operating hours of the business                     |

#### User Data Set
| Field         | Description                                         |
|---------------|-----------------------------------------------------|
| user_id       | Unique identifier for the user                      |
| name          | Name of the user                                    |
| review_count  | Number of reviews posted by the user                |
| yelping_since | Date the user joined Yelp                           |
| useful        | Number of useful votes the user has received        |
| funny         | Number of funny votes the user has received         |
| cool          | Number of cool votes the user has received          |
| elite         | Years the user was listed as "elite"                |
| friends       | List of user's friends' user_ids                    |
| fans          | Number of fans the user has                         |
| average_stars | Average rating of all reviews posted by the user    |
| compliment_*  | Various types of compliments received by the user   |

#### Review Data Set
| Field         | Description                                    |
|---------------|------------------------------------------------|
| review_id   	| Unique identifier for each review              |
| user_id 	    | Unique identifier for each user  	             |
| business_id  	| Unique identifier for businesses  	           |
| stars       	| Rating given to the business between 1 and 5	 |
| useful	      | Count of users who found the review useful     |
| funny	        | Count of users who found the review funny	     |
| cool	        | Count of users who found the review cool	     |
| text	        | Text of the review                             |
| date        	| Date the user submitted the review	           |

## Notebooks
1. **1.1-EDA.ipynb** - Initial exploratory data analysis and data preprocessing for restaurants, users, and reviews.
2. **1.2-TransformingData.ipynb** - Data transformation for data sets to begin modeling.
3. **02-Restaurant_Modeling.ipynb** - Development of predictive models for restaurant ratings based on user preferences.
4. **03-Activity_Modeling.ipynb** - Applying similar modeling techniques to predict user preferences for activities.
5. **04-UserExploration.ipynb** - Detailed user-specific analysis and prediction, utilizing the models to generate personalized recommendations.

## Technologies Used
- Python
- Jupyter Notebook
- Libraries: Pandas, Numpy, Matplotlib, Scikit-Surprise, Streamlit

## Conclusion and Next Steps
The project successfully implements a recommendation system for both dining and activities. Future work could involve integrating more cities and refining the recommendation engine.
