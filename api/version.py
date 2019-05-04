from sanic.response import json

from sanic import Blueprint

version_blueprint = Blueprint('Version', url_prefix='/info', strict_slashes=True)


@version_blueprint.route('/version', methods=['GET'])
async def test(request):
    return json({"application": "qtconnect", "version": 0.2})
