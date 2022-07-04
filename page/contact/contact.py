
from flask import Blueprint, render_template


contact = Blueprint('contact', __name__,
                 static_folder='static',
                 static_url_path='/contact',
                 template_folder='templates')

@contact.route('/contact')
def contact_page():
    return render_template('contact.HTML')