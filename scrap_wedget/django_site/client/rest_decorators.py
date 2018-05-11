"""
Decorators for working with public and authenticated REST-style calls.

public_rest_call() provides fundamental support for JSON-over-http calls.

Private token verifcation (shared secret) is also supported; this is
fundamentally insecure (as anyone with the app can obtain the secret via
decompilation) but should deter casual hackers. However the underlying API
should be sufficiently robust to handle out-of-app access in any event.
"""
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseForbidden
from django.conf import settings
from django.db import transaction

from .constants import *
from util import rich_json
# from db_logging import db_logging
from django.http import JsonResponse


def respond(request, value):

    """
    Build a response string. If there was a 'callback' GET parameter, we return
    a JSONP response, otherwise the JSON is returned as-is.
    """
    json_string = rich_json.dumps(value, indent = 2 if settings.DEBUG else None)
    callback = request.GET.get('callback')
    if callback != None:
        response = HttpResponse('%s(%s)' % (callback, json_string),
                            content_type = 'text/javascript')
        return response
    else:
        response = HttpResponse(json_string, content_type = 'application/json')
        return response


def debug_call(message, func):
    print ('%s: %s.%s' % (message, func.__module__, func.__name__))

def public_rest_call(func):
    """
    This public_rest_calldecorator adds a dictionary 'json' to a request, populated from the
    request body, and converts the dictionary returned by the decorated function
    into json in a HttpResponse.
    """
    @csrf_exempt
    def wrapper(request, *args, **kwargs):
        request.json = rich_json.loads(request.body.decode('utf-8'))
        meta = request.META['HTTP_USER_AGENT']
        try:
            if settings.DEBUG:
                debug_call('Rest call', func)

            with transaction.atomic():
                request.json = rich_json.loads(request.body.decode('utf-8'))
                response = respond(request, func(request, *args, **kwargs))

        except Exception as e:
            if settings.DEBUG:
                exception_string = str(e) + '  raised_from  ' + str(meta) + ' user_name  ' + str(request.user)
                # print('Call failed: %s ' % exception_string)
                # db_logging.debug('Call failed: %s ' % exception_string)

            # db_logging.exception('Public rest call failed.')
            response = respond(request, {'rest_error_code': 1})
        return response

    return wrapper


def public_post_call(func):
    """
    A regular POST with parameters pass on command line
    """
    @csrf_exempt
    def wrapper(request, *args, **kwargs):
        request.json = rich_json.loads(request.body)
        meta = request.META['HTTP_USER_AGENT']

        try:
            if settings.DEBUG:
                debug_call('POST call', func)

            with transaction.atomic():
                if not request.method == 'POST':
                    return HttpResponseNotAllowed('Only POST allowed')
                return func(request, *args, **kwargs)
        except Exception as e:
            if settings.DEBUG:
                exception_string = str(e) + '  raised_from  ' + str(meta) + ' user_name  ' + str(request.user)
                print('Call failed: %s ' % exception_string)
                # db_logging.debug('Call failed: %s ' % exception_string)
                # db_logging.exception('Public POST call failed.')
            return HttpResponseForbidden(e.message)

    return wrapper
