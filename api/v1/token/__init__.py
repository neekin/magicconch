from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from validators.forms import ClientForm
from models.user import User

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()

    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }
    identity = promise[form.type](form.account.data, form.secret.data)
    token = generate_auth_token(identity['uid'], form.type.value)
    t = {'token': token.decode('ascii')}
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type
    })
