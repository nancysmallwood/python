

class Payload:
    # The init method or constructor
    def __init__(self, login, application_data, message_type, message):
        self.login = login
        self.application_data = application_data
        self.message_type = message_type
        self.message = message


    def to_json(self):
        return '{"Login": %s, ' \
               '"OSPMessage": %s,' \
               '"ApplicationData": %s}' % \
               (self.login.to_json(),
                self.quote.to_json(),
                self.application_data.to_json())
