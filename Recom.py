from Recommending_Movies import Recommending_Movies
from surprise import SVD


class Recom:
    
    def __init__(self, dataset):
        rd = Recommending_Movies(dataset)
        self.dataset = rd
    
    #This function calculates Top N recommendations mentioned by the user in the MainScreen
    def Top_N(self, ml, user_id, n):
        
        #Using recommender SVD
        Top_n = SVD(n_factors=100,random_state=10)
        
        #Building recommendation model...
        train__set = self.dataset.Train_Full()
        Top_n.fit(train__set)
            
        #Computing recommendations...
        test__set = self.dataset.Anti_Test(user_id)
        
        predictions = Top_n.test(test__set)
            
        recommendations = []
        
        for userID, movieID, actualRating, estimatedRating, _ in predictions:
            intMovieID = int(movieID)
            recommendations.append((intMovieID, estimatedRating))
            
        recommendations.sort(key=lambda x: x[1], reverse=True)
        recommendations=recommendations[:n]
        
        return recommendations




