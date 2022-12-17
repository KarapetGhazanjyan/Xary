from surprise import Dataset
from surprise import Reader
import pandas as pd

#Class which loads data and pick a movie name
class Movie:

    ID_to_name = {}
    ratings = "data\\ratings.csv"
    movies = "data\\movies.csv"
    
    #Function loads data and show ratings for each movie
    def Load_Movie_Data(self):

        self.ID_to_name = {}
        self.name_to_movieID = {}

        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)
        #Loading ratings dataset
        ratings_data = Dataset.load_from_file(self.ratings, reader=reader)
        
        ds=pd.read_csv(self.movies)
        ids=list(ds['movieId'])
        mname=list(ds['title'])
        for i in range(len(ids)):
                self.ID_to_name[ids[i]] = mname[i]
                self.name_to_movieID[mname[i]] = ids[i]
            
        return ratings_data
    
    def Get_Movie_Name(self, movieID):
        if movieID in self.ID_to_name:
            return self.ID_to_name[movieID]
        else:
            return ""