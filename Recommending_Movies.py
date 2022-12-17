# This class builds train and test models
class Recommending_Movies:
    
    def __init__(self, data):
        self.fullTrainSet = data.build_full_trainset()
        
    #Full Train set of model
    def Train_Full(self):
        return self.fullTrainSet
    
    #Anti test set for the userId you have passed in argument
    #Then this testset is used tofind recommendations
    def Anti_Test(self, user_id):
        train_set = self.fullTrainSet
        fill = train_set.global_mean
        anti_test_set = []
        user_items = set([j for (j, _) in train_set.ur[user_id]])
        anti_test_set += [(str(user_id), str(i), fill) for
                         i in train_set.all_items() if
                         i not in user_items]
        return anti_test_set




