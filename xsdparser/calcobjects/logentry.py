# logLevel	required	LogLevel
# instanceId	optional	String
# threadId	optional	String
# className	optional	String
# Message	1	String
# Exception	0 - 1	String

from util.dictionary_util import get_attr_key, get_dic_item


class LogEntry:
    # The init method or constructor
    def __init__(self, dic):
        # Fields
        self.log_level = get_dic_item(dic, get_attr_key(dic, 'loglevel'))
        self.instance_id = get_dic_item(dic, get_attr_key(dic, 'instanceid'))
        self.thread_id = get_dic_item(dic, get_attr_key(dic, 'threadid'))
        self.class_name = get_dic_item(dic, get_attr_key(dic, 'classname'))
        self.message = get_dic_item(dic, get_attr_key(dic, 'message'))
        self.exception = get_dic_item(dic, get_attr_key(dic, 'exception'))

    def __str__(self):
        print_str = "log_level=%s, instance_id= %s, thread_id= %s, class_name=%s, message= %s, exception= %s" % \
                    (self.log_level, self.instance_id, self.thread_id,
                     self.class_name, self.message, self.exception)
        return print_str

