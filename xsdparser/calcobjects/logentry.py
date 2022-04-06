# logLevel	required	LogLevel
# instanceId	optional	String
# threadId	optional	String
# className	optional	String
# Message	1	String
# Exception	0 - 1	String


from util.dictionary_util import get_attr_key, get_dic_item, null, coalesce_str


class LogEntry:
    # The init method or constructor
    def __init__(self, dic):
        self.log_level = None
        self.instance_id = None
        self.thread_id = None
        self.class_name = None
        # self.message = None
        self.exception = None
        if dic is not None:
            # Fields
            self.log_level = get_dic_item(dic, get_attr_key(dic, 'loglevel'))
            self.instance_id = get_dic_item(dic, get_attr_key(dic, 'instanceid'))
            self.thread_id = get_dic_item(dic, get_attr_key(dic, 'threadid'))
            self.class_name = get_dic_item(dic, get_attr_key(dic, 'classname'))
            # temp_message = get_dic_item(dic, get_attr_key(dic, 'message'))
            # if isinstance(temp_message, dict):
            #     self.message = None
            # else:
            #     self.message = get_dic_item(dic, get_attr_key(dic, 'message'))
            self.exception = get_dic_item(dic, get_attr_key(dic, 'exception'))

    def __str__(self):
        print_str = "log_level=%s, instance_id= %s, thread_id= %s, class_name=%s, exception= %s" % \
                    (self.log_level, self.instance_id, self.thread_id,
                     self.class_name, self.exception)
        return print_str

    def to_json(self):
        return '{"logLevel": %s, ' \
               '"instanceId": %s, ' \
               '"threadId": %s, ' \
               '"className": %s, ' \
               '"Exception": %s}' % \
               (coalesce_str(self.log_level),
                coalesce_str(self.instance_id),
                coalesce_str(self.thread_id),
                coalesce_str(self.class_name),
                coalesce_str(self.exception))

