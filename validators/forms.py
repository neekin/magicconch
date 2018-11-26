from wtforms import StringField, IntegerField, ValidationError
from wtforms.validators import DataRequired, length, Regexp

from app.libs.enums import ClientTypeEnum
from models.user import User
from validators.base import BaseForm as Form


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])
    secret = StringField(validators=[DataRequired(), Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}')])
    nickname = StringField(validators=[DataRequired(), length(min=5, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()
