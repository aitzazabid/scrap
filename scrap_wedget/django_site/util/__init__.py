"""
This package contains various general-utility functions.
"""
from ast import literal_eval
import random, string
import urllib
# from urllib.request import urlopen
import json
import util.rich_json


def csv_to_array(string):
    """
    Parse the passed string as the contents of a list; the interpreter is
    invoked on the string directly, but safely in that it may only literals -
    strings, ints, bools, etc.
    """
    if string == None:
        return []
    else:
        return literal_eval('[' + string + ']')


def csv_to_tuple(string):
    """
    Returns a tuple, similar to csv_to_array(). Tuples are immutable, so use
    this if you want a read-only sequence.
    """
    # Note tuples have a special syntax for single entry tuples.
    if string == None or len(string.strip()) == 0:
        return ()
    else:
        return literal_eval('(' + string + ',)')


def csv_strings_to_tuple(string):
    """
    Given a comma-separate list, return a list of strings. The other
    csv functions in this module assume the source string can simply be
    eval()'d, but a basic list of strings (as a user may enter) cannot because
    each string isn't quoted.
    The list is split on the comma character, and each element has strip()
    called on it to remove leading and trailing space.

    Example input:
        image.png, file.txt, another string

    Output:
        ['image.png', 'file.txt', 'another string']
    """
    if string == None:
        return []
    else:
        return [s.strip() for s in string.split(',')]


def list_to_csv(sequence):
    """
    Convert the passed sequence to a comma-separated string. Only strings are
    given special treatment (they are surrounded by single quotes); all other
    values are directly converted to strings.
    """
    string = ''
    for item in sequence:
        if len(string) > 0:
            string += ','

        if type(item) == str:
            string += "'{0}'".format(item)
        else:
            string += str(item)

    return string


def model_reload(instance):
    """
    Reload the passed instance from the DB.
    """
    return instance.__class__.objects.get(id = instance.id)


def get_page_num(request):
    """
    Pagination helper; get the value of the 'page' parameter from the GET
    dictionary of request. Returns 1 if no such key exists.
    """
    page = request.GET.get('page')
    return 1 if page == None else page


def random_string(length = 4):
    """
    Return a string of random uppercase ASCII characters of the specified length.
    """
    return ''.join(random.choice(string.ascii_uppercase) for x in range(length))


# def json_call(url, params):
    # """
    # Convert the passed parameters to json, post to the passed URL, and
    # return the json-decoded response object.
    # """
    # request = urllib.request(url, rich_json.dumps(params))
    # connection = urllib.urlopen(request)
    # response = connection.read()
    # connection.close()
    # return json.loads(response)


def update_dict(a, b):
    """
    A simple shortcut to add all values in dictionary b to dictionary a, and
    return a.
    """
    a.update(b)
    return a


def truncate_string(s, max_length = 64):
    """
    Return 's' if it is no longer than max_length, otherwise return a truncated
    version that is max_length characters long, including a trailing '...' (if
    possible).
    """
    if len(s) > max_length:
        if max_length < 3:
            return s[:max_length]
        else:
            return s[:max_length - 3] + '...'
    else:
        return s
