from flask import Blueprint
from flask import render_template,request,redirect,url_for,session
from connect_DB import *
import pymysql
import os


# connect database
con = pymysql.connect(HOST,USER,PASSWORD,DATABASE)

add_page = Blueprint( 'add_page', __name__)

@add_page.route('/additem')
def add():
    if "user_name" not in session:
        return redirect(url_for('login_page.login'))
    return render_template('add_item.html', alert = False)


@add_page.route('/addlist', methods=["POST"])
def add_list():
    if request.method == "POST":
        
        file = request.files['files']
        upload_folder = 'static/img'
        app_folder = os.path.dirname(__file__)
        img_folder = os.path.join(app_folder,upload_folder)
        file.save(os.path.join(img_folder,file.filename))
        path = upload_folder + "/" + file.filename

        user_id = session['user_id']
        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        phone = request.form["mob"]
        content = request.form["ans"]
        with con:
            cur = con.cursor()
            sql = "INSERT INTO tb_list (user_id, user_name, user_lname, content, img, phone, email) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            cur.execute(sql,(user_id, fname, lname, content, path, phone, email))
            cur.close()
        return render_template('add_item.html', alert = True)


