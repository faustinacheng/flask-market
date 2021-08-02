from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    username = StringField(label="User Name: ", validators=[Length(min=2, max=30, message="Username must be between 2 to 30 characters long."), DataRequired()])
    email_address = StringField(label="Email Address: ", validators=[Email(message="Email address is invalid."), DataRequired()])
    password1 = PasswordField(label="Password: ", validators=[Length(min=6, message="Password must be at least 6 characters long."), DataRequired()])
    password2 = PasswordField(label="Confirm Password: ", validators=[EqualTo(fieldname="password1", message="Passwords do not match."), DataRequired()])
    submit = SubmitField(label="Create Account")

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists! Please try a different username")

    def validate_email_address(self, email_address_to_check):
        user = User.query.filter_by(email_address=email_address_to_check.data).first()
        if user:
            raise ValidationError("Email already exists! Please try a different email")


class LoginForm(FlaskForm):
    username = StringField(label="User Name: ", validators=[DataRequired()])
    password = PasswordField(label="Password: ", validators=[DataRequired()])
    submit = SubmitField(label="Sign In")


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item")


class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item")
