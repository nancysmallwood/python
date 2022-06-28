# Sender	0 - 1	String
# ApplicationProperty	0 - unlimited	String
# MessageLogging	0 - 1
# LogEntry	0 - unlimited
# ResponseTimeMS	0 - 1	Decimal
from calcobjects.applicationproperties import ApplicationProperties
from calcobjects.logentries import LogEntries
from calcobjects.messagelogging import MessageLogging
from util.dictionary_util import get_attr_key, get_dic_item, get_dic_key, coalesce_str, coalesce_num


class ApplicationData:
    # The init method or constructor
    def __init__(self, dic):
        self.sender = None
        self.response_time_ms = None
        self.application_properties = ApplicationProperties(dic)
        self.log_entries = LogEntries(dic)
        self.message_logging = MessageLogging(dic)
        if dic is not None:
            # Objects
            if get_dic_key(dic, 'applicationproperty') is not None:
                self.application_properties = \
                    ApplicationProperties(get_dic_item(dic, get_dic_key(dic, 'applicationproperty')))
            if get_dic_key(dic, 'logentry') is not None:
                self.log_entries = \
                    LogEntries(get_dic_item(dic, get_dic_key(dic, 'logentry')))
            if get_dic_key(dic, 'messagelogging') is not None:
                self.message_logging = \
                    MessageLogging(get_dic_item(dic, get_dic_key(dic, 'messagelogging')))
            # Fields
            self.sender = get_dic_item(dic, get_attr_key(dic, 'sender'))
            self.response_time_ms = get_dic_item(dic, get_attr_key(dic, 'responsetimems'))


    def __str__(self):
        print_str = "application_properties=%s, log_entries= %s, message_logging= %s, sender= %s, response_time_ms= %s" % \
                    (self.application_properties, self.log_entries, self.message_logging,
                     self.sender, self.response_time_ms)
        return print_str

    def to_json(self):
        return '{"Sender": %s, ' \
               '"ResponseTimeMS": %s, ' \
               '"ApplicationProperty": %s, ' \
               '"MessageLogging": %s, ' \
               '"LogEntry": %s}' % \
               (coalesce_str(self.sender),
                coalesce_num(self.response_time_ms),
                self.application_properties.to_json(),
                self.message_logging.to_json(),
                self.log_entries.to_json())
