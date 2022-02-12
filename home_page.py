from flask import Blueprint
from flask import render_template,request,redirect,url_for,session

homepage = Blueprint( 'homepage', __name__)

@homepage.route("/homepage")
def home_page():
     if "user_name" not in session:
          return redirect(url_for('login_page.login'))
     return render_template("home_page.html")

