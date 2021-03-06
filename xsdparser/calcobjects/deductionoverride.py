# ExemptOverride	0 - 1
# NonTaxableOverride	0 - 1
from calcobjects.exemptoverride import ExemptOverride
from calcobjects.nontaxableoverride import NonTaxableOverride
from util.dictionary_util import get_dic_item, get_dic_key


class DeductionOverride:
    # The init method or constructor
    def __init__(self, dic):
        self.exempt_override = ExemptOverride(dic)
        self.nontaxable_override = NonTaxableOverride(dic)
        if dic is not None:
            # Objects
            if get_dic_key(dic, 'exemptoverride') is not None:
                self.exempt_override = ExemptOverride(get_dic_item(dic, get_dic_key(dic, 'exemptoverride')))
            if get_dic_key(dic, 'nontaxableoverride') is not None:
                self.nontaxable_override = NonTaxableOverride(get_dic_item(dic, get_dic_key(dic, 'nontaxableoverride')))

    def __str__(self):
        print_str = "exempt_override = %s, nontaxable_override = %s" \
                    % (self.exempt_override, self.nontaxable_override)
        return print_str

    def to_json(self):
        return '{"ExemptOverride": %s, ' \
               '"NonTaxableOverride": %s}' % \
               (self.exempt_override.to_json(),
                self.nontaxable_override.to_json())
