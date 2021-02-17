class user_payment():

    def __init__(self, card_number, card_name, card_exp, card_cvc):
        self.__card_number = card_number
        self.__card_name = card_name
        self.__card_exp = card_exp
        self.__card_cvc = card_cvc

    def set_card_number(self, card_number):
        self.__card_number=card_number
    def set_card_name(self, card_name):
        self.__card_name=card_name
    def set_card_exp(self, card_exp):
        self.__card_exp=card_exp
    def set_card_cvc(self, card_cvc):
        self.__card_cvc=card_cvc

    def get_card_number(self):
       return self.__card_number
    def get_card_name(self):
        return self.__card_name
    def get_card_exp(self):
        return self.__card_exp
    def get_card_cvc(self):
        return self.__card_cvc
