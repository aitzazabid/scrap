import datetime


# The reference date used for datetime to ordinal conversion.
ORDINAL_EPOCH = datetime.datetime(2001, 1, 1)


def timedelta_string(td, include_seconds = True):
    """
    Return a string representation of a timedelta object, in the format
    Hm Mm Ss. Seconds will be omitted it include_seconds is False.
    """
    seconds = td.total_seconds()
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    string = '%dh' % hours if hours > 0 else ''
    string = '%s %dm' % (string, minutes)
    if include_seconds:
        string = '%s %.2ds' % (string, seconds)
    return string


def datetime_to_ordinal(dt):
    """
    Return a number of seconds elapsed from the reference date to the passed
    datetime since the reference date; this will be negative for earlier dates.
    """
    if type(dt) is datetime.date:
        dt = datetime.datetime(year = dt.year, month = dt.month, day = dt.day)

    delta = dt - ORDINAL_EPOCH
    return int(delta.total_seconds())


def datetime_from_ordinal(ordinal):
    """
    Return a datetime from the passed ordinal, previously generated with
    datetime_to_ordinal().
    """
    return ORDINAL_EPOCH + datetime.timedelta(seconds = ordinal)


def seconds_until(dt):
    """
    Return the number of seconds until the passed local datetime; returns a
    negative number if dt is in the past.
    """
    td = dt - datetime.datetime.now()
    return td.total_seconds()
