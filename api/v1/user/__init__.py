from app.libs.redprint import Redprint

api = Redprint('user')

@api.route('/get')
def index():
    return 'red user'
