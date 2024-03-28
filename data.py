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


class Ingredients:
    INGREDIENT1 = '61c0c5a71d1f82001bdaaa6d'
