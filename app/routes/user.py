from flask import Blueprint, render_template, redirect, flash

from ..functions import save_picture
from ..forms import RegistrationForm
from ..extensions import db, bcrypt
from ..models.users import User

user = Blueprint('user', __name__)

@user.route('/user/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, login=form.login.data, avatar=save_picture(form.avatar.data),
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect('/')
    else:
        print(form.errors)
    return render_template('user/register.html', form=form)