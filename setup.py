"""
Flask-Python-Arango
-------------

ArangoDB support for Flask applications.

Flask-Python-Arango is pip-installable:

    $ pip install Flask-Python-Arango

Source code is hosted on `GitHub <https://github.com/zvfvrv/flask-python-arango>`.
Contributions are welcome!
"""

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Flask-Python-Arango",
    version="0.0.1",
    url="https://github.com/zvfvrv/flask-python-arango",
    download_url="https://github.com/zvfvrv/flask-python-arango/tags",
    license="Apache-2.0",
    author="Francesco Lombardo",
    author_email="franclombardo@gmail.com",
    description="Python ArangoDB support for Flask applications",
    long_description=long_description,
    zip_safe=False,
    platforms="any",
    packages=find_packages(),
    install_requires=[
        "Flask>=0.12",
        "python-arango>=5.4.0",
        "six",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],

)