from flask import Flask
from flask import request, jsonify
from flask_cors import CORS  # 解决跨域问题
import string
import hashlib  # encrypt
import json
import pymysql  # interactive with mysql
import mysql
from mysql import is_number, check_number_exist, check_letter_exist, check_total
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_mail import Message, Mail
import random
import time


import random
import base64
from urllib.parse import quote
import requests
import os

basedir = os.path.abspath(os.path.dirname(__file__))
Userid = ''
mailcode = ''

app = Flask(__name__)  # 创建程序实例
cors = CORS(app)  # 解决跨域问题

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',  # 邮箱服务器
    MAIL_PORT=587,  # 端口号
    MAIL_USE_SSL=False,  # 支持ssl协议
    MAIL_USERNAME='1160989489@qq.com',  # 邮箱账号
    MAIL_PASSWORD='cupcayafkhgpiaji'  # 授权码
)
mail = Mail(app=app)


@app.route("/")
def index():
    return '<h1>This is a final year project designed by Jacky.</h1>'


@app.route('/hello', defaults={'name': 'Wilson'})
@app.route("/hello/<name>")
def say_hello(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route("/user/login", methods=["POST"])
def login():
    global Userid
    # 获取全局变量用户ID
    email = request.json.get("email")
    password = request.json.get("password")
    # 加密密码
    password = hashlib.sha1(password.encode()).hexdigest()
    # 查询数据库
    result = mysql.doIt("SELECT email, uName, uTel, uid FROM user where email='" +
                        email+"' and `password`='"+password+"'")
    # 得到结果
    returnmsg = {"status": 0, 'desc': "登陸成功",
                 "uid": email, "data": result}
    if(len(result) == 0):
        returnmsg["status"] = 1
        returnmsg["desc"] = "您的賬戶或密碼輸入錯誤"

        returnmsg["uid"] = 0
    else:
        Userid = email
        returnmsg["uid"] = email
        returnmsg["info"] = result[0]
    return json.dumps(returnmsg)


@app.route("/user/register", methods=["POST"])
def register():
    # 引入全局变量用户id和邮箱验证码
    global Userid
    global mailcode
    userid = request.json.get("userid")
    username = request.json.get("username")
    password = request.json.get("password")
    confirmPassword = request.json.get("confirmPassword")
    email = request.json.get("email")
    code = request.json.get("code")
    utel = request.json.get("utel")
    returnmsg = {"status": 0, 'desc': "注冊成功", "uid": userid}
    if (all([userid, username, password, confirmPassword, email, utel, code]) & (password == confirmPassword)
            & (code == str(mailcode))):
        password = hashlib.sha1(password.encode()).hexdigest()
        Userid = userid
        mysql.commit("INSERT INTO user(uid, \
        password,uName,email,uTel,team_num, register_time) \
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %
                     (userid, password, username, email, utel, "null", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        returnmsg = {"status": 0, 'desc': "Register success", "uid": userid, "password": password,
                     "uName": username, "email": email, "utel": utel}

    else:
        returnmsg["status"] = 1
        returnmsg["desc"] = "資料未填寫完整或驗證碼錯誤,請再次確認"
        returnmsg["uid"] = 0
    return json.dumps(returnmsg)


@app.route("/user/changepw", methods=["POST"])
def change_pw():
    global Userid
    global mailcode
    email = request.json.get("email")
    code = request.json.get("code")
    oldpassword = request.json.get("oldpassword")
    newpassword = request.json.get("newpassword")
    confirmnewpassword = request.json.get("confirmnewpassword")
    returnmsg = {"status": 0, 'desc': "成功修改密碼", "uid": email}

    if all([oldpassword, newpassword, email, code]) & (newpassword == confirmnewpassword) & \
            (code == str(mailcode)):

        oldpassword = hashlib.sha1(oldpassword.encode()).hexdigest()

        result = mysql.doIt("SELECT * FROM user where email='" +
                            email+"' and `password`='"+oldpassword+"'")
        if(len(result) != 0):
            if check_total(newpassword):
                newpassword = hashlib.sha1(newpassword.encode()).hexdigest()
                mysql.commit("UPDATE user SET password='" +
                             newpassword+"' where email='"+email+"'")
                returnmsg["status"] = 0
                returnmsg["desc"] = "成功修改密碼"
                returnmsg["uid"] = email
                returnmsg = {"status": 0,
                             'desc': "成功修改密碼", "uid": email}
                Userid = email

            else:
                returnmsg["status"] = 1
                returnmsg["desc"] = "密碼至少包含6個字符，其中至少包含一個數字和一個大寫字幕."
                returnmsg["uid"] = 0
        else:
            returnmsg["status"] = 1
            returnmsg["desc"] = "驗證碼或舊密碼錯誤"
            returnmsg["uid"] = 0
    else:
        returnmsg["status"] = 1
        returnmsg["desc"] = "驗證碼或舊密碼錯誤"
        returnmsg["uid"] = 0
    msg = Message(
        subject='你已經成功修改第十四屆澳門資訊科技比賽系統的密碼',
        recipients=[Userid],  # 发送给谁
        sender='<1160989489@qq.com>'  # 发送人
    )

    msg.html = '<P>你已經成功修改第十四屆澳門資訊科技比賽系統的密碼</p>'
    mail.send(msg)
    return json.dumps(returnmsg)


@app.route("/user/forgetpw", methods=["POST"])
def forget_pw():
    global Userid
    global mailcode
    email = request.json.get("email")
    code = request.json.get("code")
    newpassword = request.json.get("newpassword")
    confirmnewpassword = request.json.get("confirmnewpassword")
    returnmsg = {"status": 0, 'desc': "", "uid": ""}

    if all([newpassword, email, code]) & (newpassword == confirmnewpassword) & \
            (code == str(mailcode)):

        # oldpassword = hashlib.sha1(oldpassword.encode()).hexdigest()

        # result = mysql.doIt("SELECT * FROM user where email='" +
        #                     email+"' and `password`='"+oldpassword+"'")
        # if(len(result) != 0):
        if check_total(newpassword):
            newpassword = hashlib.sha1(newpassword.encode()).hexdigest()
            mysql.commit("UPDATE user SET password='" +
                         newpassword+"' where email='"+email+"'")
            returnmsg["status"] = 0
            returnmsg["desc"] = "成功修改密碼"
            returnmsg["uid"] = email
            returnmsg = {"status": 0,
                         'desc': "成功修改密碼", "uid": email}
            Userid = email

        else:
            returnmsg["status"] = 1
            returnmsg["desc"] = "密碼至少包含6個字符，其中至少包含一個數字和一個大寫字幕."
            returnmsg["uid"] = 0
        # else:
        #     returnmsg["status"] = 1
        #     returnmsg["desc"] = "驗證碼或舊密碼錯誤"
        #     returnmsg["uid"] = 0
    else:
        returnmsg["status"] = 1
        returnmsg["desc"] = "驗證碼錯誤"
        returnmsg["uid"] = 0
    msg = Message(
        subject='你已經成功重設第十四屆澳門資訊科技比賽系統的密碼',
        recipients=[Userid],  # 发送给谁
        sender='<1160989489@qq.com>'  # 发送人
    )

    msg.html = '<P>你已經成功修改第十四屆澳門資訊科技比賽系統的密碼</p>'
    mail.send(msg)
    return json.dumps(returnmsg)


@app.route("/users/my")
def get_id():
    global Userid
    id = request.args.get("id")
    Userid = id
    returnmsg = {"id": Userid}
    return returnmsg


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    global Userid
    # 生成随机字符串，防止图片名字重复
    # ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))

    # 获取图片文件
    img = request.files.get('file')

    if img:
        folder = basedir + '/static/' + Userid
        if not os.path.exists(folder):
            os.makedirs(folder)
    # 定义一个图片存放的位置 存放在static/img下面
    path = basedir+"/static/img/"
    # 图片名称 给图片重命名 为了图片名称的唯一性
    #imgName = ran_str+img.filename
    imgName = img.filename
    # 图片path和名称组成图片的保存路径
    file_path = path + imgName
    folder = basedir + '/static/' + Userid + '/' + imgName
    # 保存图片
    img.save(folder)
    # 这个是图片的访问路径，需返回前端（可有可无）
    imgfile = basedir + \
        '/static/img/'+imgName
    url = 'http://api.exocr.com/ocr/v1/macau_id_card'
    app_key = '6212af43d3e04e73a7a1bf6401d5b727'
    app_secret = '3ef0df3476050df644b2ac796fdb4382'
    f = base64.b64encode(open(folder, 'rb').read())
    imgdata = f
    params = {
        'app_key': app_key,
        'app_secret': app_secret,
        # 'image_url' : imgurl,
        'image_base64': imgdata
    }
    result_ = requests.post(url, data=params)
    string_result = result_.text
    result_ = json.loads(string_result)
    name = result_['result']['name']['words']
    bir_id = result_['result']['id']['words']
    sex = result_['result']['sex']['words']
    birth_date = result_['result']['birth_date']['words']
    description = result_['description']
    error_code = result_['error_code']
    reg_res = str(name)+', '+str(bir_id)+', '+str(sex)+', ' + \
        str(birth_date)+', '+str(description)+', '+str(error_code)
    print(reg_res)
    mysql.commit("INSERT INTO id_card_info(bir_id, \
    sex,birthday, name, email) \
    VALUES ('%s', '%s', '%s', '%s', '%s')" %
                 (bir_id, sex, birth_date, name, Userid))
    path = basedir+"/static/instrution_file/"
    msg = Message(
        subject='你已經成功報名參加第十四屆澳門資訊科技比賽',
        recipients=[Userid],  # 发送给谁
        sender='<1160989489@qq.com>'  # 发送人
    )
    msg.html = '<P>你已經成功報名參加第十四屆澳門資訊科技比賽</p>'
    mail.send(msg)
    #folder = path + Userid
    # if not os.path.exists(folder):
    #     os.makedirs(folder)
    return reg_res


@app.route('/uploadstatement', methods=['GET', 'POST'])
def upload_statement():
    global Userid
    id = Userid
    # ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    file = request.files.get('wordfile')
    file_name = file.filename
    path = basedir+"/static/statement_file/" + file_name
    folder = basedir + '/static/' + Userid + '/'+file_name
    file.save(folder)
    mysql.commit("update id_card_info set is_upload_statement='" +
                 "true"+"' where email='"+id+"'")
    return path


@app.route('/uploadinstruction', methods=['GET', 'POST'])
def upload_instruction():
    global Userid
    id = Userid
    # ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    file = request.files.get('wordfile')
    file_name = file.filename
    path = basedir+"/static/instrution_file/"+file_name
    folder = basedir + '/static/' + Userid + '/' + file_name
    file.save(folder)
    mysql.commit("update id_card_info set is_upload_instruction='" +
                 "true"+"' where email='"+id+"'")
    return path


@app.route('/uploadvideo', methods=['GET', 'POST'])
def upload_video():
    global Userid
    id = Userid
    # userid=request.json.get("userid")
    # 生成随机字符串，防止视频名字重复
    #ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    # 获取视频文件 name = upload
    file = request.files['video']
    # 定义一个视频存放的位置 存放在static下面
    path = basedir+"/static/video/"
    # 视频名称 给视频重命名 为了图片名称的唯一性
    videoName = file.filename
    # 视频path和名称组成视频的保存路径
    file_path = path+videoName
    folder = basedir + '/static/' + Userid + '/' + videoName
    # 保存视频
    file.save(folder)
    # 这个是视频的访问路径，需返回前端（可有可无）
    mysql.commit("UPDATE id_card_info SET is_upload_video='" +
                 "true"+"' where email='"+id+"'")
    mysql.commit("UPDATE team_info SET video_name='" +
                 videoName+"' where email='"+id+"'")
    return file_path


@app.route("/details")
def get_id_card_detail():
    id = Userid
    detail = mysql.getOne("SELECT * FROM id_card_info WHERE email='"+id+"'")
    returnmsg = {"detail": detail, }
    return returnmsg

@app.route("/teamdetails")
def get_team_info_detail():
    id = Userid
    detail = mysql.getOne("SELECT * FROM team_info WHERE email='"+id+"'")
    returnmsg = {"team_detail": detail }
    return returnmsg



@app.route("/editidcard", methods=["POST"])
def edit_id_card():
    id = Userid
    edit_bir_id = request.json.get("edit_bir_id")
    edit_sex = request.json.get("edit_sex")
    edit_birthday = request.json.get("edit_birthday")
    edit_name = request.json.get("edit_name")

    if all([edit_bir_id]):
        mysql.commit("update id_card_info set bir_id='" +
                     edit_bir_id+"' where email='"+id+"'")

    if all([edit_sex]):
        mysql.commit("update id_card_info set sex='" +
                     edit_sex+"' where email='"+id+"'")
    if all([edit_birthday]):
        mysql.commit("update id_card_info set birthday='" +
                     edit_birthday+"' where email='"+id+"'")
    if all([edit_name]):
        mysql.commit("update id_card_info set name='" +
                     edit_name+"' where email='"+id+"'")
    returnmsg = {'desc': "修改成功"}
    return json.dumps(returnmsg)

@app.route("/editteaminfo", methods=["POST"])
def edit_team_info():
    id = Userid
    edit_team_num = request.json.get("edit_team_num")
    edit_tutor = request.json.get("edit_tutor")
    edit_team_mem_two = request.json.get("edit_team_mem_two")
    edit_team_mem_three = request.json.get("edit_team_mem_three")
    edit_team_type = request.json.get("edit_team_type")
    # print(edit_team_num+edit_team_mem_two)

    if all([edit_team_num]):
        mysql.commit("update team_info set team_num='" +
                     edit_team_num+"' where email='"+id+"'")
    if all([edit_tutor]):
        mysql.commit("update team_info set tutor='" +
                     edit_tutor+"' where email='"+id+"'")
    if all([edit_team_mem_two]):
        mysql.commit("update team_info set team_mem_two='" +
                     edit_team_mem_two+"' where email='"+id+"'")
    if all([edit_team_mem_three]):
        mysql.commit("update team_info set team_mem_three='" +
                     edit_team_mem_three+"' where email='"+id+"'")
    if all([edit_team_type]):
        mysql.commit("update team_info set team_type='" +
                     edit_team_type+"' where email='"+id+"'")
    returnmsg = {'desc': "修改成功"}
    return json.dumps(returnmsg)


@app.route("/uploadteaminfo", methods=["POST"])
def upload_team_info():
    global Userid
    id = Userid
    team_num = request.json.get("team_num")
    tutor = request.json.get("tutor")
    team_type = request.json.get("team_type")
    team_mem_two = request.json.get("team_mem_two")
    team_mem_three = request.json.get("team_mem_three")
    returnmsg = {}

    result = mysql.doIt("SELECT * FROM team_info where team_num='" +
                        team_num+"' ")
    if(len(result) != 0):
        returnmsg["desc"] = "您或您的隊友已經上傳參賽信息"
    else:
        if all([team_num, tutor, team_type, team_mem_two, team_mem_three]):
            mysql.commit("INSERT INTO team_info(team_num, \
            tutor,team_type,team_mem_two,team_mem_three,email,video_name) \
            VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %
                         (team_num, tutor, team_mem_two, team_mem_two, team_mem_three, id, "null"))
            mysql.commit("UPDATE user SET team_num='" +
                         team_num+"' where email='"+id+"'")

        returnmsg = {"team_num": team_num, 'tutor': tutor, "team_type": team_type, "team_mem_two": team_mem_two,
                     "team_mem_three": team_mem_three, "id": id, "desc": "參賽信息上传成功"}
    return json.dumps(returnmsg)


@app.route('/send', methods=["GET", "POST"])
def send_mail():

    email = request.json.get("email")
    msg = Message(
        subject='第十四屆澳門資訊科技比賽系統用戶註冊/修改密碼',
        recipients=[email],  # 发送给谁
        sender='<1160989489@qq.com>'  # 发送人
    )

    ramdom_code = random.randint(50, 100)
    global mailcode
    mailcode = ramdom_code
    msg.html = '<P>您的驗證碼為：' + str(ramdom_code) + '</p>'
    mail.send(msg)
    return '發送成功，請查看郵箱'


@app.route('/sendforget', methods=["GET", "POST"])
def send_mail_forget():

    email = request.json.get("email")
    msg = Message(
        subject='第十四屆澳門資訊科技比賽系統用戶重設密碼',
        recipients=[email],  # 发送给谁
        sender='<1160989489@qq.com>'  # 发送人
    )

    ramdom_code = random.randint(50, 100)
    global mailcode
    mailcode = ramdom_code
    msg.html = '<P>您的驗證碼為：' + str(ramdom_code) + '</p>'
    mail.send(msg)
    return '發送成功，請查看郵箱'


if __name__ == '__main__':
    app.run()

app.run(host="127.0.0.1", port=5000, debug=True)
