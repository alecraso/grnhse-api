"""
    Generic exceptions for the Greenhouse APIs
"""


class InvalidAPIVersion(Exception):
    pass


class InvalidAPICallError(Exception):
    pass


class HTTPError(Exception):
    pass


class EndpointNotFound(Exception):
    pass
