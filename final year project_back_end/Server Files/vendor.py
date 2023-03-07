from flask import Flask
from flask import request, jsonify
from flask_cors import CORS #解决跨域问题
import hashlib #encrypt
import json
import pymysql #interactive with mysql
import mysql
import requests
from mysql import is_number
import os
import shutil


app=Flask(__name__)
cors=CORS(app)
@app.route("/")
def index():
    return "HAHAHA"

@app.route("/user/login",methods=["POST"])
def login():
    #Get userid and pw
    userid=request.json.get("userid")
    password=request.json.get("password")
    #Encrypt
    password=hashlib.sha1(password.encode()).hexdigest()
    #Query database
    result=mysql.doIt("SELECT * FROM user where uid='"+userid+"' and `password`='"+password+"'")
    #Get the result

    returnmsg={"status":0,'desc':"login success","uid":userid,"data":result}
    if(len(result)==0):
        returnmsg["status"]=1
        returnmsg["desc"]="Wrong password or useid"
        returnmsg["uid"]=0
    else:
        returnmsg["uid"]=userid
        returnmsg["info"]=result[0]
    return json.dumps(returnmsg)

@app.route("/goods/brand_lists")
def get_brand_lists():
    #数据库查询分类
    brands=mysql.doIt("SELECT brand_id,brand_name FROM brand ORDER BY orderby")


    #数据库查询所有商品
    result=mysql.doIt("SELECT * FROM goods")
    for p in brands:
       # print(p.brand_id)
        p["data"]=[one for one in result if one["brand_id"]==p["brand_id"]]
    return json.dumps(brands)

@app.route("/goods/index")
def get_indexgoods():
    #数据库查询分类
    result=mysql.doIt("SELECT * from goods")
    return json.dumps(result)

@app.route("/goods/details")
def get_good_detail():
    id=request.args.get("id")
    detail=mysql.getOne("SELECT * FROM goods WHERE goods_id="+str(id))

    banners=mysql.doIt("SELECT image,image2,image3,image4,image5 FROM goods WHERE goods_id="+str(id))
    returnmsg={"detail":detail,"banners":banners}
    return returnmsg

@app.route("/goods/addgoods",methods=["POST"])
def addgoods():
    #Get userid and pw
    goodsid=request.json.get("goodsid")
    name=request.json.get("name")
    brand=request.json.get("brand")
    price=request.json.get("price")
    image=request.json.get("image")
    image2=request.json.get("image2")
    image3=request.json.get("image3")
    image4=request.json.get("image4")
    image5=request.json.get("image5")
    returnmsg={"status":0,'desc':"Add success","Goods_id":goodsid}

    # x=image[0:image.rfind('\\', 1) + 1]
    # os.rename(image,""+x+""+""+goodsid+".png")
    if all([image]):
        shutil.copy(image,"C:\\Users\\zqche\\Desktop\\Project File-finished-ver1(local vendor)\\Server Files\\static\\"+goodsid+"1.png")
        image="http://127.0.0.1:4444/static/"+goodsid+"1.png"
    if all([image2]):
        shutil.copy(image2,"C:\\Users\\zqche\\Desktop\\Project File-finished-ver1(local vendor)\\Server Files\\static\\"+goodsid+"2.png")
        image2="http://127.0.0.1:4444/static/"+goodsid+"2.png"
    if all([image3]):
        shutil.copy(image3,"C:\\Users\\zqche\\Desktop\\Project File-finished-ver1(local vendor)\\Server Files\\static\\"+goodsid+"3.png")
        image3="http://127.0.0.1:4444/static/"+goodsid+"3.png"
    if all([image4]):
        shutil.copy(image4,"C:\\Users\\zqche\\Desktop\\Project File-finished-ver1(local vendor)\\Server Files\\static\\"+goodsid+"4.png")
        image4="http://127.0.0.1:4444/static/"+goodsid+"4.png"
    if all([image5]):
        shutil.copy(image5,"C:\\Users\\zqche\\Desktop\\Project File-finished-ver1(local vendor)\\Server Files\\static\\"+goodsid+"5.png")
        image5="http://127.0.0.1:4444/static/"+goodsid+"5.png"
    # shutil.copy(image2,"C:\\Users\\Lognam\\Desktop\\year 3 b\\Information System Inplementation\\Project File\\Server Files\\static\\"+goodsid+"2.png")
    # shutil.copy(image3,"C:\\Users\\Lognam\\Desktop\\year 3 b\\Information System Inplementation\\Project File\\Server Files\\static\\"+goodsid+"3.png")
    # shutil.copy(image4,"C:\\Users\\Lognam\\Desktop\\year 3 b\\Information System Inplementation\\Project File\\Server Files\\static\\"+goodsid+"4.png")
    # shutil.copy(image5,"C:\\Users\\Lognam\\Desktop\\year 3 b\\Information System Inplementation\\Project File\\Server Files\\static\\"+goodsid+"5.png")
    
    # image2="http://127.0.0.1:4444/static/"+goodsid+"2.png"
    # image3="http://127.0.0.1:4444/static/"+goodsid+"3.png"
    # image4="http://127.0.0.1:4444/static/"+goodsid+"4.png"
    # image5="http://127.0.0.1:4444/static/"+goodsid+"5.png"

    if all([name,brand,price,goodsid,image]):
        mysql.commit("INSERT INTO goods(goods_id, \
        goods_name,price,brand_id,image,image2,image3,image4,image5) \
        VALUES ('%s', '%s', '%s', '%s','%s','%s','%s','%s','%s')" % \
        (goodsid, name,price,brand,image,image2,image3,image4,image5))
        returnmsg={"status":0,'desc':"Add success"}
        
    else:
        returnmsg["status"]=1
        returnmsg["desc"]="Incomplete form"
        returnmsg["uid"]=0
    # print(json.dumps(returnmsg))
    return json.dumps(returnmsg)

@app.route("/goods/search",methods=["POST"])
def goods_search():
    keyword=request.json.get("keyword")
    returnmsg={"status":1,'desc':"Add "}
    if all([keyword]):
        if len(keyword)<=3 and is_number(keyword):
            result=mysql.doIt("SELECT * FROM goods WHERE (goods_id  LIKE '%"+keyword+"%')")
        else:
            result=mysql.doIt("SELECT * FROM goods WHERE (goods_name  LIKE '%"+keyword+"%')")
        returnmsg={"status":0,'desc':"Add success","result":result}
        return returnmsg
    return returnmsg

@app.route("/goods/editgoods",methods=["POST"])
def editgoods():
    id=request.args.get("id")
    edit_name=request.json.get("edit_name")
    edit_description=request.json.get("edit_description")
    edit_brand=request.json.get("edit_brand")
    returnmsg={'desc':"edit successful"}
    if all([edit_name]):
        mysql.commit("update goods set goods_name='"+edit_name+"' where goods_id="+str(id))
    if all([edit_description]):
        mysql.commit("update goods set description='"+edit_description+"' where goods_id="+str(id))
    if all([edit_brand]):
        mysql.commit("update goods set brand_id='"+edit_brand+"' where goods_id="+str(id))
    return json.dumps(returnmsg)

@app.route("/vendor/my")
def get_order_status_vendor():
    status0=mysql.doIt("SELECT COUNT(*) AS status0 FROM orders WHERE orders.`status`=0")

    status1=mysql.doIt("SELECT COUNT(*) AS status1 FROM orders WHERE orders.`status`=1")

    status2=mysql.doIt("SELECT COUNT(*) AS status2 FROM orders WHERE orders.`status`=2")

    status3=mysql.doIt("SELECT COUNT(*) AS status3 FROM orders WHERE orders.`status`=3")

    returnmsg={"status0":status0,"status1":status1,"status2":status2,"status3":status3}
    return returnmsg

@app.route("/orders/vendorall")
def get_orders_vendor():
    data=mysql.doIt("SELECT orders.*, `user`.uName FROM orders INNER JOIN `user` WHERE orders.customer_id=`user`.uid ORDER BY order_date DESC")
    result=mysql.doIt("select * from orders ")
    returnmsg={"orders":data, "result":result}
    return returnmsg
    '''return id  +str(id)'''

@app.route("/orders/vendorpending")
def get_orders_vendor_pending():
    data=mysql.doIt("SELECT orders.*, `user`.uName FROM orders INNER JOIN `user` WHERE orders.`status`=0 AND orders.customer_id=`user`.uid ORDER BY order_date DESC")
    returnmsg={"orders":data}
    return returnmsg
    '''return id  +str(id)'''

@app.route("/orders/vendorhold")
def get_orders_vendor_hold():
    data=mysql.doIt("SELECT orders.*, `user`.uName FROM orders INNER JOIN `user` WHERE orders.`status`=1 AND orders.customer_id=`user`.uid ORDER BY order_date DESC")
    returnmsg={"orders":data}
    return returnmsg
    '''return id  +str(id)'''

@app.route("/orders/vendorpast")
def get_orders_vendor_past():
    data=mysql.doIt("SELECT orders.*, `user`.uName FROM orders INNER JOIN `user` WHERE (orders.`status`=2 OR orders.`status`=3) AND orders.customer_id=`user`.uid ORDER BY order_date DESC")
    returnmsg={"orders":data}
    return returnmsg
    '''return id  +str(id)'''

@app.route("/orders/orderdetail")
def get_order_detail():
    id=request.args.get("id")
    #detail=mysql.doIt("SELECT * FROM orders_detail WHERE order_id="+str(id))

    detail=mysql.doIt("SELECT orders.`status`,`user`.uName, `user`.uAddress, orders_detail.* FROM orders INNER JOIN `user` ON orders.customer_id=`user`.uid INNER JOIN orders_detail ON orders.order_id=orders_detail.order_id WHERE orders.order_id="+str(id)+" ORDER BY order_date DESC")
    banners=mysql.doIt("SELECT goods.image,goods.goods_name FROM goods INNER JOIN orders_detail on goods.goods_id=orders_detail.goods_id WHERE orders_detail.order_id="+str(id))
    result=mysql.doIt("SELECT * FROM orders WHERE order_id="+str(int(id)))

    returnmsg={"detail":detail,"banners":banners,"result":result}
    return returnmsg

@app.route("/orders/changestatus2")
def change_status_2():
    order_id = request.args.get("id")

    mysql.commit("UPDATE orders SET `status`=2 WHERE order_id="+str(order_id))
    return order_id


app.run(host="127.0.0.1",port=4444,debug=True) 




