class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    REGISTER_URL = BASE_URL + 'api/auth/register'
    LOGIN_URL = BASE_URL + 'api/auth/login'
    USER_URL = BASE_URL + 'api/auth/user'
    ORDER_URL = BASE_URL + 'api/orders'


class StatusCodes:
    FORBIDDEN = 403
    OK = 200
    UNAUTHORIZED = 401
    BAD_REQUEST = 400
    INTERNAL_SERVER_ERROR = 500


class Ingredients:
    KNOWN_INGREDIENT = '61c0c5a71d1f82001bdaaa6d'
    INVALID_INGREDIENT = '61c0c5a71d1f82001bdaaa'
