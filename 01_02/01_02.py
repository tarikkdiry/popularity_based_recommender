import pandas as pd
import numpy as numpy

frame = pd.read_csv('rating_final.csv')
cuisine = pd.read_csv('chefmozcuisine.csv')

frame.head()
cuisine.head()

rating_count = pd.DataFrame(frame.groupby('placeID')['rating'].count())
rating_count.sort_values('rating', ascending=False).head()

most_rated_places = pd.DataFrame([135085, 132825, 135032, 135052, 132834], index=np.arange(5), columns=['placeId'])
summary = pd.merge(most_rated_places, cuisine, on='placeID')


