from sanic.response import HTTPResponse


class CorsMiddleWare:

    @staticmethod
    def apply_to(app):
        @app.middleware('request')
        async def cors(request):
            if request.method == 'OPTIONS':
                return HTTPResponse(status=200)

        @app.middleware('response')
        async def cors(request, response):
            response.headers['Access-Control-Allow-Origin'] = app.config.CORS_ORIGINS
            response.headers['Access-Control-Allow-Headers'] = '*'
            response.headers['Access-Control-Allow-Methods'] = '*'
