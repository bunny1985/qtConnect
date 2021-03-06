import os


class CorsSettings:
    def apply_to(app):
        app.config.CORS_ORIGINS = '*'

        if 'CORS_ORIGINS' in os.environ:
            app.config.CORS_ORIGINS = list(map(
                lambda host: host.strip(),
                os.environ['CORS_ORIGINS'].split(',')
            ))
