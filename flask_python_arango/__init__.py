#    Copyright 2020 Francesco Lombardo <franclombardo@gmail.com>

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

__all__ = ("FlaskArango")

from arango import ArangoClient
from flask import current_app, _app_ctx_stack


class FlaskArango(object):

    """Manages ArangoDB connections for your Flask app.
    FlaskArango objects provide access to ArangoDB MongoDB server via the :attr:`db`
    attribute. You must either pass the :class:`~flask.Flask`
    app to the constructor, or call :meth:`init_app`.
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        app.teardown_appcontext(self.teardown)

    def connect(self):

        host = self.app.config.get("ARANGODB_HOST", None)
        db_name = self.app.config.get("ARANGODB_DB", None)
        db_username = self.app.config.get("ARANGODB_USERNAME", None)
        db_password = self.app.config.get("ARANGODB_PSW", None)

        if host is None:
            raise ValueError(
                "You must set the ARANGO_HOST Flask config variable",
            )
        if db_name is None:
            raise ValueError(
                "You must set the ARANGODB_DB Flask config variable",
            )
        # Initialize the client for ArangoDB.
        client = ArangoClient(hosts=host)
        # Connect to database.
        return client.db(
            db_name, username=db_username, password=db_password)

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'arango_db'):
            del ctx.arango_db

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'arango_db'):
                ctx.arango_db = self.connect()
            return ctx.arango_db
