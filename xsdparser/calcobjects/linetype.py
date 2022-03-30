# LineType	0 - 1	String (0 - 40)
# direction	optional	String (0 - 40)
# content	optional	String (0 - 40)
# status	optional	String (0 - 40)
# accumulationLocation	optional	String (0 - 40)

from util.dictionary_util import get_attr_key, get_dic_item


class LineType:
    # The init method or constructor
    def __init__(self, dic):
        self.line_type = get_dic_item(dic, get_attr_key(dic, 'text'))
        self.direction = get_dic_item(dic, get_attr_key(dic, 'direction'))
        self.content = get_dic_item(dic, get_attr_key(dic, 'content'))
        self.status = get_dic_item(dic, get_attr_key(dic, 'status'))
        self.accumulationLocation = get_dic_item(dic, get_attr_key(dic, 'accumulationLocation'))

    def __str__(self):
        print_str = "line_type = %s, direction = %s, content = %s, " \
                    "status = %s, accumulationLocation = %s" \
                    % (self.line_type, self.direction, self.content,
                       self.status, self.accumulationLocation)
        return print_str