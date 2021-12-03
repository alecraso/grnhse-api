import re

from io import open
from setuptools import setup, find_packages
from noom_versioning.versioning import calver_version

README = 'README.md'
CHANGES = 'CHANGES.md'
VERSION_FILE = 'grnhse/__init__.py'


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def find_version():
    version_file = read(VERSION_FILE)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M)
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


setup(
    name='grnhse-api',
    version=calver_version(),
    author='Aaron Biller',
    author_email='aaronbiller@gmail.com',
    description='Python wrapper for the Greenhouse APIs',
    long_description=read(README) + '\n' + read(CHANGES),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/aaronbiller/grnhse-api',
    packages=find_packages(),
    tests_require=[
        'pytest',
        'pytest-cov',
        'mock',
    ],
    install_requires=[
        'requests~=2.20,>=2.20.1',
        'pytest-runner==4.2',
    ],
    include_package_data=True,
    scripts=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
