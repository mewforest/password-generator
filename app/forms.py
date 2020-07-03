from flask_wtf import FlaskForm
from wtforms.fields import IntegerField, SubmitField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired, NumberRange


class Settings(FlaskForm):
    letters_number = IntegerRangeField('Количество символов', default=6,
                                  validators=[DataRequired(), NumberRange(min=1, max=32)])
    passwords_number = IntegerRangeField('Количество паролей', default=4,
                                    validators=[DataRequired(), NumberRange(min=1, max=20)])
    submit = SubmitField('Применить настройки')
