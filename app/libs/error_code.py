from app.libs.error import ApiException


class Success(ApiException):
    code = 201
    msg = 'ok'
    error_code = 0


class ClientTypeError(ApiException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(ApiException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(ApiException):
    code = 404
    msg = 'the resource are not_found Q_Q...'
    error_code = 1001


class AuthFailed(ApiException):
    code = 401
    msg = 'authorization failed'
    error_code = 1005
