from flask import Blueprint
from api.v1 import client, user, token


def create_blueprint_v1():
    bp_v1 = Blueprint('bp_v1', __name__)
    user.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    return bp_v1
