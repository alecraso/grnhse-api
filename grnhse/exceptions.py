"""
    Generic exceptions for the Greenhouse APIs
"""


class InvalidAPIVersion(Exception):
    pass


class HTTPError(Exception):
    pass


class EndpointNotFound(Exception):
    pass
