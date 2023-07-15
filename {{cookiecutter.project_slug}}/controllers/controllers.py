import logging
from pathlib import Path
from utils.imports import *
from datetime import datetime as dt
from flask_cors import cross_origin
from config.config import config, app
from flask import jsonify, request, wrappers


load_dotenv()
logger = logging.getLogger(__name__)

@app.app.route("/ping", methods=["GET"])
def ping(username: str, suffix: str = None):
    resp = {"who": username, "at": dt.now().strftime("%Y-%m-%d, %H:%M:%S"), "suffix": suffix}

    pong = jsonify(resp)
    pong.status_code = 200

    return pong
