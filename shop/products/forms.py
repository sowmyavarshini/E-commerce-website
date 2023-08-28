from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators, DecimalField


class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])
    colors = TextAreaField('Colors', [validators.DataRequired()])

    image_1 = FileField('Image1', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg']),
                        "Images only please"])
    image_2 = FileField('Image2', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg']),
                        "Images only please"])
    image_3 = FileField('Image3', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg']),
                        "Images only please"])

