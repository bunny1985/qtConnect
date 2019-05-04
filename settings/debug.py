import os


class DebugSetting:
    @staticmethod
    def apply_to(app):
        if os.environ.get('DEBUG', '').lower() in ('true', '1', 'y', 'yes'):
            app.config.DEBUG = True
