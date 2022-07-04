from flask import Blueprint, render_template
from flask import Flask, redirect
from flask import url_for
from flask import render_template
from flask import request, session, jsonify




assignment3_2 = Blueprint('assignment3_2', __name__,
                          static_folder='static',
                          static_url_path='/assignment3_2',
                          template_folder='templates')




user_dict = {'user1': {'name': 'Yossi', 'email': 'Yossi@gmail.com', 'password': '1212'},
             'user2': {'name': 'or', 'email': 'or@gmail.com', 'password': '1111'},
             'user3': {'name': 'ron', 'email': 'ron@gmail.com', 'password': '8787'},
             'user4': {'name': 'gal', 'email': 'gal@gmail.com', 'password': '4747'},
             'user5': {'name': 'tal', 'email': 'tal@gmail.com', 'password': '4545'}}

usersDetail = list(user_dict.values())

emails = []
for i in range(len(usersDetail)):
    emails.append(usersDetail[i]['email'])


def index_by_email(email):
    for i in range(len(usersDetail)):
        if usersDetail[i]['email'] == email:
            return i


@assignment3_2.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2_func():
    if request.method == 'GET':
        if 'email' in request.args:
            email = request.args['email']

            if email == '':
                return render_template('assignment3_2.HTML', usersDetail=usersDetail,
                                       message='If you want to search for one user write Email')

            if email in emails:
                index = index_by_email(email)
                username = usersDetail[index]['name']
                user_password = usersDetail[index]['password']
                return render_template('assignment3_2.html', name=username, email=email, password=user_password)
            else:
                return render_template('assignment3_2.HTML', message='not found this user')

    if request.method == 'POST':
        usermail = request.form['mail']
        print(usermail)
        password = request.form['password']
        print(password)
        if password == '' and usermail == '':
            return render_template('assignment3_2.html', message='Fill in the field of the password and email')
        if usermail == '':
            return render_template('assignment3_2.html', message='Fill in the field of the email')
        if password == '':
            return render_template('assignment3_2.html', message='Fill in the field of the password')
        if usermail in emails:
            Index = index_by_email(usermail)
            user_password = usersDetail[Index]['password']
            username = usersDetail[Index]['name']
            print(user_password)
            if user_password == password:
                session['user_name'] = username
                session['logedin'] = True
                return render_template('assignment3_2.html', message='Success')
            else:
                return render_template('assignment3_2.html', message='Wrong password try again!')
        else:
            return render_template('assignment3_2.html', message='Wrong email try again!')
    return render_template('assignment3_2.html')


@assignment3_2.route('/log_out')
def log_out():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('assignment3_2_func'))





