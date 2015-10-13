'''
Created on Oct 12, 2015

@author: Naji Dmeiri
@author: Bogdan Vasilescu
'''
from pygments.token import *

SUPPORTED_LANGUAGE_STRINGS = {
    'Ruby',
    'Python',
    'JavaScript',
    'PHP',
    'Java',
    'Scala',
    'C',
    'C++',
    'Objective-C',
    'Swift'
}


def languageForLexer(lexer):
    """
    :param lexer:   A `Lexer` object as defined in `pygments.lexer`
    :returns:       A string indicating the language supported by the lexer
                    Currently supported return values:  'Ruby',
                                                        'Python',
                                                        'JavaScript',
                                                        'PHP',
                                                        'Java',
                                                        'Scala',
                                                        'C',
                                                        'C++',
                                                        'Objective-C',
                                                        'Swift'
    """
    mapping = {
        'Ruby':         'Ruby',
        'Python':       'Python',
        'JavaScript':   'JavaScript',
        'Php':          'PHP',
        'Java':         'Java',
        'Scala':        'Scala',
        'C':            'C',
        'Cpp':          'C++',
        'Objective-C':  'Objective-C',
        'Swift':        'Swift'
    }
    assert mapping[lexer.name] in SUPPORTED_LANGUAGE_STRINGS # sanity check; can be disabled in release build
    return mapping[lexer.name]


def tokensForTokenType(tokens, tokenType, ignoreSubtypes = False):
    """
    :param tokens:          A list of `Token` objects as defined in `pygments.token`
    :param tokenType:       A `TokenType` object as defined in `pygments.token`
    :param ignoreSubtypes:  When set to True, the returned list will include subtypes of `tokenType` ; default is `False`.
    :returns:               An iterable of tuples that each hold information about a `tokenType` tokens.
    """
    if tokenType not in STANDARD_TYPES:
        raise ValueError("%s is not a standard Pygments token type." % tokenType)

    if not ignoreSubtypes:
        return [t for t in tokens if is_token_subtype(t[0], tokenType)]
    else:
        return [t for t in tokens if t[0] == tokenType]


def tokensExceptTokenType(tokens, tokenType, ignoreSubtypes = False):
    """
    :param tokens:          A list of `Token` objects as defined in `pygments.token`
    :param tokenType:       A `TokenType` object as defined in `pygments.token`
    :param ignoreSubtypes:  When set to True, the returned list will include subtypes of `tokenType` ; default is `False`.
    :returns:               An iterable of tuples that each hold information about a `tokenType` tokens.
    """
    if tokenType not in STANDARD_TYPES:
        raise ValueError("%s is not a standard Pygments token type." % tokenType)

    if not ignoreSubtypes:
        return [t for t in tokens if not is_token_subtype(t[0], tokenType)]
    else:
        return [t for t in tokens if not t[0] == tokenType]

