import json
from flask import (Flask, render_template, url_for,
                   redirect, request, make_response, flash)
from options import DEFAULTS


app = Flask(__name__)
app.secret_key = 'wghiwiguwgbit2grwdvUE32643874FGV&%#&!*#^'


def get_saved_data():
    try:
        # use json loads to convert json string into dict
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():
    return render_template('index.html', saves=get_saved_data())


@app.route('/builder')
def builder():
    return render_template('builder.html', saves=get_saved_data(), options=DEFAULTS)


@app.route('/save', methods=['POST'])
def save():
    flash('Alright! That looks awesome!')
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    # update stored cookie information before saving
    data.update(dict(request.form.items()))
    # set cookie of form converted into dict and then json
    response.set_cookie('character', json.dumps(data))
    return response


app.run(debug=True, host='127.0.0.1', port=8000)
