# nonTaxableOverride	0 - 1  text 0 - 1	number amount
# overrideNonTaxableReasonCode	optional	String (1 - 4)

from util.dictionary_util import get_attr_key, get_dic_item


class NonTaxableOverride:
    # The init method or constructor
    def __init__(self, dic):
        self.non_taxable_override = get_dic_item(dic, get_attr_key(dic, 'text'))
        self.override_nontaxable_reason_code = get_dic_item(dic, get_attr_key(dic, 'overridenontaxablereasoncode'))

    def __str__(self):
        print_str = "non_taxable_override=%s, override_nontaxable_reason_code= %s" % \
                    (self.non_taxable_override, self.override_nontaxable_reason_code)
        return print_str
