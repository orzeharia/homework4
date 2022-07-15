import requests as requests
from flask import Blueprint, render_template, request, redirect, session, jsonify

from DBmanager import interact_db

assignment4 = Blueprint('assignment4', __name__,
                        static_folder='static',
                        static_url_path='/assignment4',
                        template_folder='templates')


@assignment4.route('/assignment4')
def assignment4_fanc():
    return render_template('assignment4.HTML')


@assignment4.route('/outer_source')
def outer_source_fanc():
    return render_template('outer_source.HTML')


@assignment4.route('/users')
def users_fanc():
    return render_template('users.HTML')


# ------------------------------------------------- #
# ------------------- SELECT ---------------------- #
# ------------------------------------------------- #
@assignment4.route('/select_users')
def select_users():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    print(users_list)
    return render_template('assignment4.html', users=users_list)


# ------------------------------------------------- #
# ------------------------------------------------- #


# ------------------------------------------------- #
# -------------------- INSERT --------------------- #
# ------------------------------------------------- #
@assignment4.route('/insert_user', methods=['POST'])
def insert_user():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    print(f'{name} {email} {password}')
    query = "INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s')" % (name, email, password)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment4')


# ------------------------------------------------- #
# ------------------------------------------------- #


# ------------------------------------------------- #
# -------------------- DELETE --------------------- #
# ------------------------------------------------- #
@assignment4.route('/delete_user', methods=['POST'])
def delete_user_func():
    email = request.form['email']
    query = "DELETE FROM users WHERE email='%s';" % email

    interact_db(query, query_type='commit')
    return redirect('/assignment4')


# ------------------------------------------------- #


# -------------------UPDATE-------------#
@assignment4.route('/update_user', methods=['POST'])
def update_user():
    flag = False
    emailForupdate = request.form['emailForupdate']
    name = request.form['name']
    password = request.form['password']

    #  emails list
    emails_query = "select email from users"
    emails_list = interact_db(emails_query, query_type='fetch')
    emailsusers = []
    for user in emails_list:
        emailsusers.append(user.email)
    if emailForupdate not in emailsusers:
        session['update'] = "Update Failed: please fill correct email"
        flag = True

    if emailForupdate == "":
        session['update'] = "Update Failed: please fill  email text boxes"

    if flag == False and emailForupdate != "":
        if name != "":
            query = "update users set name='%s' where email='%s';" % (name, emailForupdate)
            interact_db(query, query_type='commit')
            session['update'] = "The update was successful"

        if password != "":
            query = "update users set password='%s' where email='%s';" % (password, emailForupdate)
            interact_db(query, query_type='commit')
            session['update'] = "The update was successful"

        if name == "" and password == "":
            session['update'] = "You did not enter data for change"
    return redirect('/assignment4')


# ---BBBBB---------------

users_back = []
users_send = []


@assignment4.route('/fetch')
def fetch_func():
    if request.args['user_id_back'] == "":
        session['message_back'] = "Select id 1-6 please"
        session['user_back'] = ""
        return render_template('outer_source.html')

    if 'type' in request.args:
        user_id = int(request.args['user_id_back'])
        session['user_back'] = ""
        if request.args['type'] == 'sync':
            users_data = requests.get(f'https://reqres.in/api/users').json()
            users_back.append(users_data['data'])
            session['user_back'] = found_user(users_back, user_id)
    return render_template('outer_source.html')


def found_user(users_back, user_id):
    users_send = []
    for user in users_back[0]:
        if user['id'] == user_id:
            user_found = {
                'first_name': user['first_name'],
                'avatar': user['avatar']
            }
            users_send.append(user_found)
            session['message_back'] = ""
    return users_send


# ----user

@assignment4.route('/users_fun')
def users_fun_json():
    users_res = {}
    query = "select * from users"
    list_of_users = interact_db(query, query_type='fetch')
    for user in list_of_users:
        users_dict = {}
        user_id = user.id
        users_dict['email'] = user.email
        users_dict['username'] = user.name
        users_dict['password'] = user.password
        users_res[user_id] = users_dict
    return jsonify(users_res)


# -----c
@assignment4.route('/assignment4/restapi_users/', defaults={'id':1})
@assignment4.route('/assignment4/restapi_users/<int:id>')
def partc_func(id):
    query = 'select * from users where id=%s;' % id
    users = interact_db(query=query, query_type='fetch')
    if len(users) == 0:
        res = {'error message': f'user {id} not found'}
    else:
        res = {
            'id': users[0].id,
            'name': users[0].name,
            'email': users[0].email,
            'password': users[0].password }
    return jsonify(res)
