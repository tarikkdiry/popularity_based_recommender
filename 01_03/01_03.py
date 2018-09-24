import pandas as pd
import numpy as np

frame = pd.read_csv('01_03/rating_final.csv')
cuisine = pd.read_csv('01_03/chefmozcuisine.csv')
geodata = pd.read_csv('01_03/geoplaces2.csv', encoding = 'mbcs')

places = geodata[['placeID', 'name']]
# print(places.head())
# print(cuisine.head())

rating = pd.DataFrame(frame.groupby('placeID')['rating'].mean())
# print(rating.head())

rating['rating_count'] = pd.DataFrame(frame.groupby('placeID')['rating'].count())
# print(rating.head())
# print(rating.describe())
rating.sort_values('rating_count', ascending=False).head()