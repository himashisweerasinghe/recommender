import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from IPython import get_ipython

'''
In the script above we use the read_csv() method of the Pandas 
library to read the "ratings.csv" file. Next, we call the head() method from
 the dataframe object returned by the read_csv() function, which will display the 
 first five rows of the dataset.
'''

ratings_data = pd.read_csv("ratings.csv")
print(ratings_data.head())

'''
You can see from the output that the "ratings.csv" file contains the userId, movieId, ratings, and timestamp attributes. 
Each row in the dataset corresponds to one rating. The userId column 
contains the ID of the user who left the rating. The movieId column contains the Id of the movie, 
the rating column contains the rating left by the user. Ratings can have values between 1 and 5. 
And finally, the timestamp refers to the time at which the user left the rating.

There is one problem with this dataset. It contains the IDs of the movies but not their titles. 
We'll need movie names for the movies we're recommending. The movie names are stored in the "movies.csv" file. 
Let's import the file and see the data it contains. Execute the following script:
'''

movie_names = pd.read_csv("movies.csv")
print(movie_names.head())

'''
As you can see, this dataset contains movieId, the title of the movie, and its genre.
 We need a dataset that contains the userId, movie title, and its ratings.
  We have this information in two different dataframe objects: "ratings_data" and "movie_names".
   To get our desired information in a single dataframe, we can merge the two dataframes objects on the movieId column 
   since it is common between the two dataframes.

We can do this using merge() function from the Pandas library, as shown below:
'''

movie_data = pd.merge(ratings_data, movie_names, on='movieId')

movie_data.head()

'''
Now let's take a look at the average rating of each movie. 
To do so, we can group the dataset by the title of the movie and then calculate the mean of the rating for each movie. 
We will then display the first five movies along with their average rating using the head() method. 
Look at the the following script:
'''

print(movie_data.groupby('title')['rating'].mean().head())

'''
You can see that the average ratings are not sorted. Let's sort the ratings in the descending order of their average ratings:
'''

print(movie_data.groupby('title')['rating'].mean().sort_values(ascending=False).head())

'''
The movies have now been sorted according to the ascending order of their ratings. 
However, there is a problem. A movie can make it to the top of the above list even if only a single user has given it five stars. 
Therefore, the above stats can be misleading. 
Normally, a movie which is really a good one gets a higher rating by a large number of users.
Let's now plot the total number of ratings for a movie:
'''

print(movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head())

'''
Now you can see some really good movies at the top. 
The above list supports our point that good movies normally receive higher ratings.
 Now we know that both the average rating per movie and the number of ratings per movie are important attributes. 
 Let's create a new dataframe that contains both of these attributes.

Execute the following script to create ratings_mean_count dataframe and first add the average rating of each movie to this dataframe:
'''

ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())

'''
Next, we need to add the number of ratings for a movie to the ratings_mean_count dataframe. 
Execute the following script to do so:
'''

ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())
print(ratings_mean_count.head())








# sns.set_style('dark')
#
# get_ipython().run_line_magic('matplotlib', 'inline')
#
# plt.figure(figsize=(8,6))
# plt.rcParams['patch.force_edgecolor'] = True
# print(ratings_mean_count['rating_counts'].hist(bins=50))
#
# plt.figure(figsize=(8,6))
# plt.rcParams['patch.force_edgecolor'] = True
# ratings_mean_count['rating'].hist(bins=50)
#
# plt.figure(figsize=(8,6))
# plt.rcParams['patch.force_edgecolor'] = True
# sns.jointplot(x='rating', y='rating_counts', data=ratings_mean_count, alpha=0.4)

