class userBMI():

    def __init__(self, user_id, weight, height):
        self.__user_id = user_id
        self.__weight = weight
        self.__height = height

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_bmi(self):
        return round(float(self.__weight) / ((float(self.__height) / 100) ** 2), 2)
