from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import ApiException

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, ApiException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return ApiException(msg, code, error_code)
    else:
        return ApiException()


if __name__ == '__main__':
    app.run(debug=True)
