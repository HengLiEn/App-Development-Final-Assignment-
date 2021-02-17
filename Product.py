class add_product():

    def __init__(self, product_img, product_name, product_price):
        self.__product_img = product_img
        self.__product_name = product_name
        self.__product_price = product_price

    def set_product_img(self, product_img):
        self.__product_img = product_img

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_product_price(self, product_price):
        self.__product_price = product_price

    def get_product_img(self):
        return self.__product_img

    def get_product_name(self):
        return self.__product_name

    def get_product_price(self):
        return self.__product_price
