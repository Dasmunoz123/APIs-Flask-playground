from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template


app = Flask(import_name=__name__)
options_list = ['Decision tree', 'Neural network']

@app.route(rule='/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect(location='/hello'))
    response.set_cookie(key='user_ip', value=user_ip) # type: ignore
    return response


@app.route(rule='/hello')
def hello():
    user_ip = request.cookies.get(key='user_ip')
    # return f"Testing Flask with IP {user_ip}"
    context = {
        'user_ip'   : user_ip,
        'options'   : options_list
    }
    return render_template(template_name_or_list='hello.html', **context)