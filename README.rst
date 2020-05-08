Flask-Python-Arango
===================

**Flask-Python-Arango** is a `python-arango`_ support for Flask applications using ArangoDB_

Installation
------------

To install a stable version from PyPi_:

.. code-block:: bash

    ~$ pip install Flask-Python-Arango


To install the latest version directly from GitHub_:

.. code-block:: bash

    ~$ pip install -e git+git@github.com:zvfvrv/flask-python-arango.git@master#egg=flask-python-arango

A Simple Example 
----------------

.. code-block:: python

    from flask import Flask, render_template
    from flask_python_arango import FlaskArango

    app = Flask(__name__)
    app.config['ARANGODB_HOST'] = 'http://localhost:8529'
    app.config['ARANGODB_DB'] = 'test'
    app.config['ARANGODB_USERNAME'] = 'root'
    app.config['ARANGODB_PSW'] = '12345678'

    ArangoDB = FlaskArango(app)

    @app.route('/')
    def home_page():
        # Execute an AQL query and iterate through the result cursor.
        cursor = ArangoDB.connection.aql.execute('FOR doc IN nodes RETURN doc')
        devices = [document for document in cursor]
        return render_template('index.html', devices=devices)


Contributing
------------

Please create an issue on GitHub_.

Links
-----

* `python-arango`_
* Flask Documentation: https://flask.palletsprojects.com/
* ArangoDB_


.. _`GitHub`: https://github.com/zvfvrv/flask-python-arango
.. _ArangoDB: https://www.arangodb.com
.. _`python-arango`: https://github.com/joowani/python-arango/releases
.. _PyPi: https://pypi.org/project/flask-python-arango/
