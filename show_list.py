from flask import Blueprint
from flask import render_template,request,redirect,url_for,session
from connect_DB import *
import pymysql


# connect database
con = pymysql.connect(HOST,USER,PASSWORD,DATABASE)

show_list_page = Blueprint( 'show_list_page', __name__)

@show_list_page.route('/showlist')
def show_list():
    with con:
        cur = con.cursor()
        sql = "SELECT * FROM tb_list"
        cur.execute(sql)
        cur.close()
        datas = cur.fetchall()
        return render_template('show_list.html', datas = datas)




