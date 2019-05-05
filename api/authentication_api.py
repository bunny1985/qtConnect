from sanic_jwt import exceptions, BaseEndpoint, Configuration
from authentication.authentication_helpers import AuthenticationManager, UserBasicData
from sanic_openapi import doc


class SecurityConfiguration(Configuration):
    access_token_name = 'jwt'
    strict_slashes = True


def retrieve_user(request, *args, **kwargs):
    payload = request.app.auth.extract_payload(request)
    if not payload or "user_id" not in payload:
        return {}

    user_id = payload.get("user_id")
    user = AuthenticationManager().get_user_by_email(user_id)
    user = user.to_ditct()
    user["password"] = ""
    return user


async def authenticate(request, *args, **kwargs):
    """ SANIC JVT authentication method"""
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    authentication_manager = AuthenticationManager()

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    if not authentication_manager.verify_pass_for_user(username, password):
        raise exceptions.AuthenticationFailed("Authenntication failed")

    user = authentication_manager.get_user_by_email(username)

    # mask password
    user = user.to_ditct()
    user["password"] = ""
    return user


class Register(BaseEndpoint):
    @doc.summary("Temporary functionality to register user directly")
    @doc.consumes({"email": str, "password": "str"})
    async def post(self, request, *args, **kwargs):
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        manager = AuthenticationManager()
        user = UserBasicData(email, password, hash_password=True)

        manager.save_user(user)
        user = user.to_ditct()

        access_token, output = await self.responses.get_access_token_output(
            request,
            user,
            self.config,
            self.instance)

        response = self.responses.get_token_reponse(
            request,
            access_token,
            output,

            config=self.config)

        return response


additional_views = (
    ('/register', Register),

)
