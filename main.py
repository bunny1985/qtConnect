from sanic_openapi import swagger_blueprint
from sanic_jwt import Initialize
from api.version import version_blueprint
from api.eventsSocked import events_stream_blueprint
from settings.debug import DebugSetting
from settings.security import SecuritySeettings
from settings.cors import CorsSettings
from sanicApp import app
from middlewares.cors import CorsMiddleWare
from api.authentication import authenticate, additional_views, SecurityConfiguration, retrieve_user

Initialize(app, authenticate=authenticate, retrieve_user=retrieve_user, class_views=additional_views,
           strict_slashes=True, configuration_class=SecurityConfiguration)

DebugSetting.apply_to(app)
CorsSettings.apply_to(app)
SecuritySeettings.apply_to(app)

CorsMiddleWare.apply_to(app)

app.blueprint(swagger_blueprint)
app.blueprint(version_blueprint)
app.blueprint(events_stream_blueprint)

app.static('/static', './static')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, auto_reload=True)
