import uuid
class User:

    def __init__(self, username, first_name, last_name, password ,email=None, contact_number=None,
                 membership=None, remarks=None):

        self.__user_img = ''
        self.__user_id = uuid.uuid4().hex
        self.__username = username
        self.__first_name = first_name
        self.__last_name = last_name
        self.__password = password
        self.__email = email
        self.__first_name = first_name
        self.__last_name = last_name
        self.__membership = membership
        self.__remarks = remarks
        self.__contact_number = contact_number

    def set_user_img(self, user_img):
        self.__user_img = user_img

    def get_user_img(self):
        return self.__user_img

    def get_user_id(self):
        return self.__user_id

    def get_full_name(self):
        return str(self.__first_name) + ' ' + str(self.__last_name)

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_membership(self):
        return self.__membership

    def get_remarks(self):
        return self.__remarks

    def get_gender(self):
        return self.__gender

    def set_user_id(self,user_id):
        self.__user_id =user_id

    def set_first_name(self,first_name):
        self.__first_name=first_name

    def set_last_name(self,last_name):
        self.__last_name= last_name

    def set_gender(self,gender):
        self.__gender=gender

    def set_membership(self,membership):
        self.__membership= membership

    def set_remarks(self,remarks):
        self.__remarks = remarks

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def get_contact_number(self):
        return self.__contact_number

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_email(self, email):
        self.__email = email

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number


class UserStaff(User):
    def __init__(self, username, password, email=None, contact_number=None, first_name=None, last_name=None,
                 membership=None, remarks=None, admin_rights=None):
        super().__init__(username, password, email=None, contact_number=None, first_name=None, last_name=None,
                 membership=None, remarks=None)
        self.__admin_rights = admin_rights

    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_membership(self):
        return self.__membership

    def get_remarks(self):
        return self.__remarks

    def get_gender(self):
        return self.__gender

    def set_user_id(self,user_id):
        self.__user_id =user_id

    def set_first_name(self,first_name):
        self.__first_name=first_name

    def set_last_name(self,last_name):
        self.__last_name= last_name

    def set_gender(self,gender):
        self.__gender=gender

    def set_membership(self,membership):
        self.__membership= membership

    def set_remarks(self,remarks):
        self.__remarks = remarks

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def get_contact_number(self):
        return self.__contact_number

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_email(self, email):
        self.__email = email

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number


