from flask import Flask, request, jsonify
from flask_cors import CORS
from src.api.routes import api_blueprint
app = Flask(__name__)
CORS(app)

app.register_blueprint(api_blueprint, url_prefix='/')

if __name__ == "__main__":
    app.run()
