from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, IntegerField, FileField, \
    DecimalField,ValidationError


def validate_card_length(form, field):
    if len(str(field.data)) != 3:
        raise ValidationError('Enter your Card CVC!')

def validate_card_number(form, field):
    i = len(str(field.data))
    if i < 16 or i > 17:
        raise ValidationError('Enter Card Number!')


def validate_card_cvc(form, field):
    i = str(field.data)
    if i.isalnum() == True:
        raise ValidationError('Enter Card Number!')


class LoginUserForm(Form):
    login_username = StringField('Username', [validators.Length(min=1, max=150), validators.DataRequired()])
    login_password = StringField(label='Password', validators=[validators.Length(min=6, max=15)])


class CreateUserForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=150), validators.DataRequired()])
    first_name = StringField('First Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    password = StringField('Password', validators=[validators.Length(min=6, max=15),
                                                   validators.EqualTo('password_confirm',
                                                                      message='Passwords must match')])
    password_confirm = StringField('Password confirm', validators=[validators.Length(min=6, max=15)])
    email = StringField('E-mail', validators=[validators.Length(min=5, max=35), validators.Email()])
    contact_number = StringField('Contact Number', [validators.Length(min=8, max=8), validators.DataRequired()])

class UpdateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=50), validators.DataRequired()])
    current_password = StringField('Current Password', validators=[validators.Length(min=6, max=15)])
    password = StringField('Password', validators=[validators.Length(min=6, max=15),
                                                   validators.EqualTo('password_confirm',
                                                                      message='Passwords must match')])

    password_confirm = StringField('Password confirm', validators=[validators.Length(min=6, max=15)])
    email = StringField('E-mail', validators=[validators.Length(min=5, max=35),validators.DataRequired()])
    contact_number = StringField('Contact Number', [validators.Length(min=8, max=8), validators.DataRequired()])

class CreateStatusForm(Form):
    status = TextAreaField('Status', [validators.Length(max=100), validators.DataRequired()])


class CreateUserReview(Form):
    review = TextAreaField('Reviews', [validators.Optional()])

class CreateReview(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    review = TextAreaField('Reviews', [validators.Optional()])

class updateReview(Form):
    review = TextAreaField('Reviews', [validators.Optional()])

class CreateUserBMI(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    height = IntegerField('Height(CM)', [validators.DataRequired(message="Enter your Height!")])
    weight = IntegerField('Weight(KG)', [validators.DataRequired(message="Enter your Weight!")])
    remarks = TextAreaField('Remarks', [validators.Optional()])


class UpdateUserBMI(Form):
    height = IntegerField('Height(CM)', [validators.DataRequired(message="Enter your Height!")])
    weight = IntegerField('Weight(KG)', [validators.DataRequired(message="Enter your Weight!")])


class CreateUserPayment(Form):
    card_number = IntegerField('CARD NUMBER', [validate_card_number])
    card_name = StringField('CARD HOLDER NAME', [validators.Length(min=1, max=150),
                                                 validators.DataRequired(message="Enter your Name date!")])
    card_exp = StringField('CARD EXPIRY', [validate_card_cvc, validators.Length(min=5, max=5)])
    card_cvc = IntegerField('CARD CVC', [validate_card_length])


class AddProductForm(Form):
    product_img = FileField('Product Image')
    product_name = StringField('Product Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    product_price = DecimalField('Product Price', [validators.DataRequired()])

class AddUserImage(Form):
    user_img = FileField('User Image')

