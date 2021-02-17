class add_calendar():

    def __init__(self, key,date, name):
        self.__key = key
        self.__date = date
        self.__name = name

    def get_key(self):
        return self.__key
    def get_date(self):
       return self.__date
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
