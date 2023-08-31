from flask import render_template, session, request, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user, login_user
from shop import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User
from shop.products.models import Addproduct, Brand, Category


@app.route('/admin')
def admin():
    products = Addproduct.query.all()
    return render_template('admin/index.html', title='Admin page', products=products)


@app.route('/brands')
@login_required
def brands():
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title='Brand page', brands=brands)


@app.route('/category')
@login_required
def category():
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand.html', title='Category page', categories=categories)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.name.data}. Thanks for registering', 'success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title='Registration page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            session['email'] = form.email.data
            flash(f'Welcome {form.email.data}. You are logged in now.', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash(f'Wrong password. Please try again', 'danger')
    return render_template('admin/login.html', form=form, title='Login Page')


@app.route('/logout')
def admin_logout():
    logout_user()
    return redirect(url_for('admin'))


















