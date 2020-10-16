import json
from flask import Blueprint, Response, request
ROUTINES = Blueprint('routines', __name__)


@ROUTINES.route('/health', methods=['GET', 'OPTIONS'])
def index():
    """Health of application"""
    return Response(json.dumps({'Status': 'OK'}))