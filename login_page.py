from flask import Blueprint
from flask import render_template,request,redirect,url_for,session
from connect_DB import *
import pymysql

# connect database
con = pymysql.connect(HOST,USER,PASSWORD,DATABASE)

login_page = Blueprint( 'login_page', __name__)

@login_page.route('/login')
def login():
    if "user_name" in session:
        return redirect(url_for('homepage.home_page'))
    return render_template('login_page.html')

@login_page.route("/check_login", methods=["POST"])
def check_login():
    user_name = request.form['user_name']
    password = request.form['password']
    with con:
        cur = con.cursor()
        sql = "SELECT * FROM tb_user where user_name = %s AND user_password = %s"
        cur.execute(sql,(user_name, password))
        data = cur.fetchall()
        cur.close()
        if len(data)  >= 1 :
            session["user_id"] = data[0][0]
            session["user_name"] = data[0][0]
            session["password"] = data[0][2]
            print(session)
            return redirect(url_for('homepage.home_page'))
    return render_template('login_page.html', alert = "Not Foud User ")

@login_page.route("/logout")
def logout():
    session.clear()
    return render_template('login_page.html')

