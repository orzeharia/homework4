from flask import Flask, jsonify, session
from datetime import timedelta
import mysql.connector

app = Flask(__name__)

app.config.from_pyfile('settings.py')

#app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)


from page.home.home import home
app.register_blueprint(home)

from page.contact.contact import contact
app.register_blueprint(contact)

from page.assignment3_1.assignment3_1 import assignment3_1
app.register_blueprint(assignment3_1)

from page.assignment3_2.assignment3_2 import assignment3_2
app.register_blueprint(assignment3_2)

from page.assignment4.assignment4 import assignment4
app.register_blueprint(assignment4)

@app.route('/session')
def session_func():
    return jsonify(dict(session))

def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='information_schema')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

if __name__ == '__main__':
    app.run(debug=True)
