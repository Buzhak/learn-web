from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db, User

app = create_app()

with app.app_context():
    username = input('Enter username: ')

    if User.query.filter(User.username == username).count():
        print('This username already yet')
        sys.exit(0)

    password1 = getpass('Enter password: ')
    password2 = getpass('Repeat password')

    if not password1 == password2:
        sys.exit(0)
    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('Ures with id {} added'.format(new_user.id))