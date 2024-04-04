# BrainStation-Capstone
This is my capstone for the duration of the bootcamp at BrainStation
## Urban Explorer: Machine Learning-Driven Discoveries

### Overview
Urban Explorer leverages machine learning to provide personalized recommendations for dining and activities, transforming the way users discover new experiences in their city or while traveling. By focusing on the recommendation system aspect, this project aims to enhance decision-making for users who face indecision about where to eat or what to do, especially in unfamiliar locales.

### Project Goals
- To offer tailored recommendations for restaurants and activities.
- To address the needs of users looking for inspiration or guidance in choosing dining spots and engaging in local activities.
- To improve upon existing recommendation systems by providing more personalized and dynamic suggestions.

### Approach
- **Data Preparation:** Conducted extensive EDA and preprocessing on restaurant data and user ratings. The focus was on ensuring data quality by filtering for well-reviewed businesses and active users across six cities.
- **Model Development:** Utilized Funk SVD modeling to factorize user-business rating matrices into latent factors, capturing the preferences and attributes that drive personalized recommendations.
- **Model Training and Evaluation:** Split data into training and test sets to refine accuracy, employing RMSE as the primary evaluation metric to measure performance and guide improvements.


# Yelp Data Sets
# Business Data Set
#### Data Dictionary
- **business_id**  	Unique identifier for the business  	**string**
- **name**	        Name of the business	                **string**
- **address**	Address where the business is located	**string**
- **city**	City where the business is located	**string**
- **state**	State where the business is located	**string**
- **postal_code**	postal_code where the business is located	**string**
- **latitude**	Geographical latitude of the business	**float64**
- **longitude**	Geographical longitude of the business	**float64**
- **stars**	Star rating of the business	**float64**
- **review_count**	Number of reviews the business has received	**int64**
- **is_open**	0 is closed and 1 is open	**int64**
- **attributes**	Attribute: Boolean	**string-Dict**
- **categories**	Categories the business falls under	**string**
- **hours**	Day of the week: Hours of operation	**string-Dict**

# User Data Set
#### Data Dictionary
- **user_id**  	Unique identifier for each user  	**string**
- **name**	        Name of user	                **string**
- **review_count**	Number of reviews by user	**int64**
- **yelping_since**	Date account opened	**Datetime**
- **useful**	Count of how many other users found current user reviews useful	**int64**
- **funny**	Count of how many other users found current user reviews funny	**int64**
- **cool**	Count of how many other users found current user reviews cool	**int64**
- **elite**	years user was labeled as elite reviewer	**string**
- **friends**	list of friends user ids	**string**
- **fans**	number of other users considered fans	**int64**
- **average_stars**	average number of stars given to businesses	**float64**
- **compliment_hot**	compliments received labeled as hot	**int64**
- **compliment_more**	compliments received labeled as more	**int64**
- **compliment_profile**	compliments received labeled as profile	**int64**
- **compliment_cute**	compliments received labeled as cute	**int64**
- **compliment_list**	compliments received labeled as list	**int64**
- **compliment_note**	compliments received labeled as note	**int64**
- **compliment_plain**	compliments received labeled as plain	**int64**
- **compliment_cool**	compliments received labeled as cool	**int64**
- **compliment_funny**	compliments received labeled as funny	**int64**
- **compliment_writer**	compliments received labeled as writer	**int64**
- **compliment_photos**	compliments received labeled as photos	**int64**

# Review Data Set
#### Data Dictionary
- **review_id**  	Unique identifier for each review  	**string**
- **user_id**  	Unique identifier for each user  	**string**
- **business_id**  	Unique identifier for businesses  	**string**
- **stars**	rating given to the business between 1 and 5	**float64**
- **useful**	count of users who found the review useful	**string**
- **funny**	count of users who found the review funny	**string**
- **cool**	count of users who found the review cool	**int64**
- **text**	text of the review	**int64**
- **date**	date the user submitted the review	**datetime**
