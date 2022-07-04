
from flask import Blueprint, render_template


assignment4 = Blueprint('assignment4', __name__,
                 static_folder='static',
                 static_url_path='/assignment4',
                 template_folder='templates')

@assignment4.route('/assignment4')
def assignment4_fanc():
    return render_template('assignment4.HTML')

