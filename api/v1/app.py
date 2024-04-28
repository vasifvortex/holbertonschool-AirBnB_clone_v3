#!/usr/bin/python3
"""Documentation"""

from flask import Flask
from models import storage
import os
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


app.register_blueprint(app_views)


@app.errorhandler(404)
def handle_404_error(error):
    return {"error": "Not found"}, 404


CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True, debug=True)
