from typing import Optional

import requests


class HttpMethods:
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'
    PATCH = 'PATCH'


class Headers:
    JSON = {"Content-Type": "application/json"}


methods = {
    HttpMethods.GET: requests.get,
    HttpMethods.POST: requests.post,
    HttpMethods.DELETE: requests.delete,
    HttpMethods.PATCH: requests.patch
}


class HttpCodes:
    OK = 200
    NoContent = 204
    InternalServerError = 500


def create_request(
        method, url,
        headers: Optional[dict] = None,
        json: Optional[dict] = None):

    req_method = methods[method]

    if req_method:
        response = req_method(url, headers=headers, json=json)
    else:
        raise Exception(f'No such method: {method}')

    return response
