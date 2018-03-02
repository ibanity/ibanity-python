class Error(Exception):
    def __init__(self, errors):
        self.errors = errors

    def str(self):
        str(map(lambda error: self.__format_error(error), self.errors))

    @staticmethod
    def __format_error(error):
        if error["attribute"]:
            return "* " + error["code"] + ": " + error["attribute"] + " " + error["message"]
        else:
            return "* " + error["code"] + error["message"]
