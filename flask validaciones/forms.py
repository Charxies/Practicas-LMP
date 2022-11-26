from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField,
                     RadioField)
from wtforms.validators import InputRequired, Length


class registerForm(FlaskForm):
    nombre = StringField('Nombre: \t', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    apellidop = StringField('Apellido Paterno: ', validators=[InputRequired(),
                                              Length(min=1, max=100)])
    apellidom = StringField('Apellido Materno: ', validators=[InputRequired(),
                                              Length(min=1, max=100)])
    email = StringField('Email: \t', validators=[InputRequired(),
                                              Length(min=1, max=100)])
    telefono = IntegerField('Telefono: \t', validators=[InputRequired()])
    sexo = RadioField('\t\tSexo',
                       choices=['hombre', 'mujer', 'otro'],
                       validators=[InputRequired()])
