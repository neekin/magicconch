from app.libs.redprint import Redprint
from app.libs.token__auth import auth

api = Redprint('user')


@api.route('', methods=['GET'])
@auth.login_required
def index():
    return 'i am user'


# @api.route('', methods=['PUT'])
# def update_user():
#     return 'red user'
#
#
# @api.route('', methods=['DELETE'])
# def delete_user():
#     return 'red user'
#
#
# @api.route('', methods=['POST'])
# def add_user():
#     return 'red user'
