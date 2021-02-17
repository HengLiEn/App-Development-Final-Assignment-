from User import User


class Staff(User):

    def __init__(self, username, first_name, last_name, password, email=None, contact_number=None,
                 membership=None, remarks=None):
        super().__init__(username, first_name, last_name, password, email=None, contact_number=None,
                         membership=None, remarks=None)
