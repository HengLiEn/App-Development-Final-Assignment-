class Status:
    status_id = 0

    def __init__(self, status):
        Status.status_id += 1
        self.__status_id = Status.status_id
        self.__status = status

    def get_status_id(self):
        return self.__status_id

    def get_status(self):
        return self.__status

    def set_status_id(self, status_id):
        self.__status_id = status_id

    def set_status(self, status):
        self.__status = status
