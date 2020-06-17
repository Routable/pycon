import datetime

class Project:

    def __init__(self, options):
        self.options = options

    def date(self):
        return self._get_date()

    def _get_date(self):
        return datetime.datetime.now().strftime("%y")

    def get_user_options(self):
        return self.options.known