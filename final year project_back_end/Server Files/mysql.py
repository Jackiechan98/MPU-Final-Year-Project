import pymysql
from flask import Flask

def doIt(query):
    conn=pymysql.Connect(host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='fyp',)

    cursor=conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def Execute(query):
    conn=pymysql.Connect(host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='fyp',)

    cursor=conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    cursor.close()
    conn.close()
    return 1

def getOne(query):
    conn=pymysql.Connect(host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='fyp',)

    cursor=conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result=cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def commit(query):

    conn=pymysql.Connect(host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='fyp',)

    cursor=conn.cursor(pymysql.cursors.DictCursor)
    try:
        # 执行sql语句
        cursor.execute(query)
        # 执行sql语句
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()
    conn.close()

def check_number_exist(newpassword):
    for x in newpassword:
        if x.isnumeric():
            return True

def check_letter_exist(newpassword):
    for x in newpassword:
        if x.isupper():
            return True
    return False

def check_total(newpassword):
    if  check_letter_exist(newpassword) and check_number_exist(newpassword) and len(newpassword) >= 6:
            return True
    return False

def is_number(s):
    try:
        float(s)        
        return True   
    except ValueError:        
        pass     
    try:        
        import unicodedata        
        unicodedata.numeric(s)        
        return True    
    except (TypeError, ValueError):        
        pass   
    return False