from flask import Blueprint

BLUEPRINT = Blueprint('routes', __name__)


@BLUEPRINT.route('/')
def hello_whale():
    return 'Whale, Hello there!'


@BLUEPRINT.route('/boom')
def hello_boom():
    return 'Boom, things add up!'
