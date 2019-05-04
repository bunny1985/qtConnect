# DEFULT SECURE HEADERS AND COOKIE SETTINGS (IN PRACTICE ALSO HEADERS )
from secure import SecureHeaders


class SecuritySeettings:
    @staticmethod
    def apply_to(app):
        secure_headers = SecureHeaders()

        @app.middleware("response")
        async def set_secure_headers(request, response):
            secure_headers.sanic(response)
