"""
    Utilities for interacting with the Greenhouse APIs
"""
import datetime
import re

DT_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


def extract_header_links(link_header):
    # Adapted from https://github.com/victor-o-silva/python-links-from-link-header
    rels = {}
    if link_header is not None:
        links = [l.strip() for l in link_header.split(',')]
        pattern = r'<(?P<url>.*)>;\s*rel="(?P<rel>.*)"'
        for link in links:
            group_dict = re.match(pattern, link).groupdict()
            rels[group_dict['rel']] = group_dict['url']
    return rels


def strf_dt(dt):
    return dt.strftime(DT_FORMAT)


def strp_dt(sdt):
    return datetime.datetime.strptime(sdt, DT_FORMAT)
