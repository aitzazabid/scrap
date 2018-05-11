from decimal import Decimal
from datetime import date, datetime
import json

from util.time_util import datetime_to_ordinal


class RichEncoder(json.JSONEncoder):
    """
    This JSON encoder adds support for the following types:

        Decimal - converted to floats.
        date, datetime - converted using time_util.datetime_to_ordinal.
    """
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, date) or isinstance(obj, datetime):
            return datetime_to_ordinal(obj)

        return json.JSONEncoder.default(self, obj)


def dumps(obj, *args, **kwargs):
    """
    Return a rich json string; this supports the additional types provided by
    RichEncoder.
    """
    s = RichEncoder(*args, **kwargs).encode(obj)
    return s


def loads(string, *args, **kwargs):
    """
    Wrapper around json.loads(); included so clients can import just rich_json
    to get both encode and decode functionality.
    """
    return json.loads(string, *args, **kwargs)


def debug(obj):
    return RichEncoder(indent = 2).encode(obj)
