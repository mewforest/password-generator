from flask import render_template, session, redirect, url_for
from app import app
from app.forms import Settings
import string
import random


@app.route('/')
def index():
    random_passwords = []
    base_symbols = '!"#$%&\'()' + string.ascii_letters + string.digits
    letters_number = session.get('letters_number', 6)
    passwords_number = session.get('passwords_number', 4)
    rand = random.SystemRandom()
    for _ in range(passwords_number):
        password = ''
        for __ in range(letters_number):
            password += rand.choice(base_symbols)
        random_passwords.append(password)
    return render_template('passwords.html', passwords=random_passwords)


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    form = Settings()
    if form.validate_on_submit():
        session['letters_number'] = form.letters_number.data
        session['passwords_number'] = form.passwords_number.data
        return redirect(url_for('index'))
    return render_template('settings.html', form=form)