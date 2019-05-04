from sanic.blueprints import Blueprint

events_stream_blueprint = Blueprint('EventsStream', url_prefix='/events', strict_slashes=True)


@events_stream_blueprint.websocket('/feed')
async def feed(request, ws):
    while True:
        data = 'hello!'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)
