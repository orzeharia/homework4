from flask import Blueprint, render_template
from flask import Flask, redirect
from flask import url_for
from flask import render_template
from flask import request, session, jsonify

assignment3_1 = Blueprint('assignment3_1', __name__,
                          static_folder='static',
                          static_url_path='/assignment3_1',
                          template_folder='templates')




hobbies_dict = {
    'Trip': 'social',
    'play': 'social',
    'sea': 'social',
    'TV': 'alone',
    'eat': 'alone',
    '': 'alone'
}

social_li = []
alone_li = []

@assignment3_1.route('/assignment3_1')
def assignment3_1_func():
    social_li.clear()
    alone_li.clear()
    if 'user_hob' in request.args:
        hobbie = request.args.get('user_hob', "")
        if hobbie == '':
            return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li,
                                   alone_li=alone_li, message='You did not wrote a hobby')
        for key in hobbies_dict:
            if hobbie.upper() == key.upper():
                session['user_hobbie'] = hobbie
                session['have_hobbie'] = True
                session['hobbieFromList'] = True
                return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li, alone_li=alone_li, message='you choose something from the list')

            else:

                session['user_hobbie'] = hobbie
                session['have_hobbie'] = True
                return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li,
                                       alone_li=alone_li, message='The hobby you write is not on the list, interesting!')

    else:
        return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li, alone_li=alone_li)


@assignment3_1.route('/assignment3_1b')
def assignment3_1b_func():
    social_li.clear()
    alone_li.clear()
    if 'hob_type' in request.args:
        type = request.args.get('hob_type', "")
        if type.lower()=='social':
            social_li.append(session['user_hobbie'])
            return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li,
                                   alone_li=alone_li, message='insert social list')
        if type.lower()=='alone':
            alone_li.append(session['user_hobbie'])
            return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li,
                                   alone_li=alone_li, message='insert alone list')
        if type.lower()!='social' and type.lower()!='alone':
            return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li,
                                   alone_li=alone_li, message='You did not make the right choice, choose social or alone')

    return redirect('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li, alone_li=alone_li)

@assignment3_1.route('/delete_hobbie')
def delete_func():
    session['have_hobbie'] = False
    session['user_hobbie']=""
    session['hobbieFromList'] = False
    social_li.clear()
    alone_li.clear()
    return redirect(url_for('assignment3_1_func'))