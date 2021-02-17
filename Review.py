class userReview():

    def __init__(self,user_id ,first_name, last_name, review):
        self.__review = review
        self.__first_name = first_name
        self.__last_name = last_name
        self.__user_id = user_id

    def get_user_id(self):
        return self.__user_id

    def get_full_name(self):
        return self.__first_name + ' ' + self.__last_name

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_review(self):
        return self.__review

    def set_review(self, review):
        self.__review = review

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_user_id(self,user_id):
        self.user_id = user_id

