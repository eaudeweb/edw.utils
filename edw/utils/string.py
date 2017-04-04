import re


def camel_case_to__(txt):
    """
    Converts underscoreCase to underscore_case.

    >>> camel_case_to__('TestMe')
    'test_me'
    >>> camel_case_to__('testMe')
    'test_me'
    >>> camel_case_to__('test_Me')
    'test__me'
    """
    try:
        cc_re = camel_case_to__._cc_re
    except AttributeError:
        cc_re = camel_case_to__._cc_re = re.compile(
            '((?<=.)[A-Z](?=[a-z0-9])|(?<=[a-z0-9])[A-Z])')

    return re.sub(cc_re, r'_\1', txt).lower()

def str_to_constant_name(txt):
    """
    Converts the string to something usable as a constant name.

    >>> str_to_constant_name('moo')
    'MOO'
    >>> str_to_constant_name('Moo a Lot')
    'MOO_A_LOT'
    >>> str_to_constant_name('_moo_ _less_')
    '_MOO_LESS_'
     """
    txt = camel_case_to__(txt)
    txt = re.sub(r'[^\w]', '_', txt)
    txt = re.sub(r'__+', '_', txt)

    return txt.upper()
