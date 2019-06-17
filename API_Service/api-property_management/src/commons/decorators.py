#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""python custom decorators."""

import json
from functools import wraps

from flask import (
    jsonify,
    request,
)
from jsonschema import validate, ValidationError

from constants.custom_field_error import HTTP_400_BAD_REQUEST


def validate_json(f):
    """Validate format of request as json."""
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.json
        except ValueError as err:
            response = jsonify(
                {
                    "error": {
                        "code": "HTTP_400_BAD_REQUEST",
                        "message": err.message
                    }
                })
            response.status_code = HTTP_400_BAD_REQUEST
            return response
        return f(*args, **kw)
    return wrapper


def validate_schema(schema):
    """Validate json with generated schema."""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                validate(request.json, schema)
            except ValidationError as err:
                response = jsonresponse(err)
                return response, HTTP_400_BAD_REQUEST
            return f(*args, **kw)
        return wrapper
    return decorator


def jsonresponse(err):
    """jsonresponse."""
    response = json.loads(json.dumps(
        {
            "error": {
                "code": "HTTP_400_BAD_REQUEST",
                "message": err.args[0]
            }
        }))
    return response