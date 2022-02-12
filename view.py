from flask import Flask
from flask import render_template,session
from home_page import *
from login_page import *
from add_item import *
from show_list import *
from datetime import timedelta


app = Flask(__name__)

# key for encoding
app.secret_key = "Ez"

# time in system
app.permanent_session_lifetime = timedelta(hours=2)

# register all page
app.register_blueprint(homepage)
app.register_blueprint(login_page)
app.register_blueprint(add_page)
app.register_blueprint(show_list_page)

# first page
@app.route("/")
def login():
     return redirect(url_for('login_page.login'))


if __name__ == '__main__':
    app.run(debug=True)
