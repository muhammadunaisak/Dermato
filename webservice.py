
from flask import*

from src.dbconnectionnew import *

from werkzeug.utils import secure_filename
from src.CNN_PREDICTION import predict
import os


app=Flask(__name__)
app.secret_key="aaa"



@app.route('/login',methods=['POST'])
def login():

    username=request.form['uname']
    password=request.form['password']

    qry="SELECT `user`.`fname`,`lname`,`login`.* FROM `user` JOIN `login` ON `user`.`lid`=`login`.`id` WHERE `login`.`username`=%s AND `password`=%s AND type='user'"
    val=(username,password)
    res=selectone(qry,val)
    print(res)

    if res is None:
        return jsonify({'task':'invalid'})

    else:
        id= res['id']
        return jsonify({'task':'success','lid':id,'fname':res['fname'],'lname':res['lname']})

@app.route('/signup',methods=['POST'])
def signup():
    fname = request.form['firstname']
    lname = request.form['lastname']
    gender = request.form['gender']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    email = request.form['email']
    phone = request.form['phone']
    dob = request.form['age']


    username = request.form['username']
    password = request.form['password']

    qry = "insert into login values(null,%s,%s,'user')"

    val = (username, password)
    id = iud(qry, val)
    qry = "insert into user values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (str(id), fname, lname, gender, place, post, pin ,email, phone,dob)
    iud(qry, val)
    return jsonify({'task': 'success'})


@app.route('/viewdoc', methods=['POST'])
def viewdoc():
    qry="select *from doctor"
    res=selectall(qry)
    return jsonify(res)




@app.route('/viewsche', methods=['POST'])

def viewsche():
    print(request.form)
    did=request.form['did']
    qry = "select *from shedule where `docid`=%s"
    res = selectall2(qry,did)
    print(res)
    return jsonify(res)

@app.route('/viewbooking', methods=['POST'])
def viewbooking():
    uid=request.form['lid']
    qry = "SELECT `shedule`.*,`doctor`.`fname`,`lname`,`booking`.`status` FROM `booking` JOIN `shedule` ON `booking`.`sid`=`shedule`.`sid` JOIN `doctor` ON `doctor`.`lid`=`shedule`.`docid` WHERE `booking`.`userid`=%s"
    res = selectall2(qry,uid)
    return jsonify(res)


@app.route('/sendfeedback', methods=['POST'])
def sendfeedback():
    feed=request.form['feed1']
    lid=request.form['lid']
    qry = "INSERT INTO `feedback` VALUES(NULL,%s,%s,CURDATE())"
    val=(lid,feed)
    iud(qry,val)
    return jsonify({"task":"success"})


@app.route('/senddocrate', methods=['POST'])
def senddocrate():
    userid = request.form['uid']
    docid = request.form['docid']
    rate= request.form['rate']
    review = request.form['review']


    qry = "insert into review values(null,%s,%s,%s,%s)"
    val = (userid,docid,rate,review)
    iud(qry, val)

    return jsonify({'task': 'success'})


@app.route('/chatwin',methods=['POST'])
def chatwin():
    qry="SELECT *FROM `doctor`"
    res=selectall(qry)
    return jsonify(res)


@app.route('/viewprofile',methods=['POST'])
def viewprofile():
    lid=request.form['uid']
    q="SELECT * FROM `user` WHERE `lid`=%s"
    res=selectall2(q,lid)
    return  jsonify(res)



@app.route('/update',methods=['POST'])
def update():
    lid=request.form['lid']
    fname = request.form['fn1']
    lname = request.form['ln1']
    gender = request.form['gn1']
    place = request.form['pl1']
    post = request.form['post1']
    pin = request.form['pin1']
    email = request.form['email1']
    phone = request.form['phn1']
    dob = request.form['dob1']
    qry = "UPDATE `user`  SET `fname`=%s,`lname`=%s,`gender`=%s,`place`=%s,`post`=%s,`pin`=%s,`email`=%s,`phone`=%s,`dob`=%s WHERE `lid`=%s"
    val = (fname,lname,gender,place,post,pin,email,phone,dob,lid)

    iud(qry, val)

    return jsonify({'task': 'success'})


@app.route('/booknow',methods=['POST'])
def booknow():
    lid=request.form['lid']
    sid = request.form['sid']
    qry="INSERT INTO `booking` VALUES(NULL,%s,%s,'pending',CURDATE())"
    v=(lid,sid)
    iud(qry,v)
    return jsonify({'task': 'success'})






# @app.route('/viewfriends',methods=['post'])
# def viewfriends():
#     lid=request.form['uid']
#     print(lid)
#     qry="SELECT `friend_request`.*,`user_registration`.* FROM `user_registration` JOIN `friend_request` ON `friend_request`.`fromid`=`user_registration`.`lid` WHERE `friend_request`.`toid`=%s AND `friend_request`.`status`='accepted' UNION SELECT `friend_request`.*,`user_registration`.* FROM `user_registration` JOIN `friend_request` ON  `friend_request`.`toid`=`user_registration`.`lid`" \
#         " WHERE `friend_request`.`fromid`=%s AND `friend_request`.`status`='accepted'"
#     value=(lid,lid)
#     res = selectall(qry,value)
#     return jsonify(res)


@app.route('/in_message2',methods=['post'])
def in_message2():
    print(request.form)
    fromid = request.form['fid']
    print("fromid",fromid)

    toid = request.form['toid']
    print("toid",toid)

    message=request.form['msg']
    print("msg",message)
    qry = "INSERT INTO `chat` VALUES(NULL,%s,%s,%s,CURDATE())"
    value = (fromid, toid, message)
    print("pppppppppppppppppp")
    print(value)
    iud(qry, value)
    return jsonify(status='send')

@app.route('/view_message2',methods=['post'])
def view_message2():
    print("wwwwwwwwwwwwwwww")
    fromid=request.form['fid']
    print(fromid)
    toid=request.form['toid']
    print(toid)
    lmid = request.form['lastmsgid']
    qry="SELECT `fromid`,`message`,`date`,`chatid` as toid FROM `chat` WHERE `chatid`>%s AND ((`toid`=%s AND  `fromid`=%s) OR (`toid`=%s AND `fromid`=%s)  )  ORDER BY chatid ASC"
    val=(str(lmid),str(toid),str(fromid),str(fromid),str(toid))
    print("fffffffffffff",val)
    res = selectall2(qry,val)
    print("resullllllllllll")
    print(res)
    if res is not None:
        return jsonify(status='ok', res1=res)
    else:
        return jsonify(status='not found')


@app.route('/rating',methods=['post'])
def rating():
    userid = request.form['userid']
    docid = request.form['docid']
    rate = request.form['rating']
    review = request.form['review']

    qry = "INSERT INTO `review` VALUES(NULL,%s,%s,%s,%s)"
    val = (str(userid), str(docid), str(rate), str(review))
    iud(qry, val)
    return jsonify(status='yeh')


@app.route('/imgupld',methods=['post'])
def imgupld():
    op=['basal cell carcinoma', 'melanoma', 'nevus', 'Normal', 'pigmented benign keratosis', 'vascular lesion']
    from datetime import datetime
    # use= request.form['img']
    print(request.files)
    image = request.files['file']
    fn=datetime.now().strftime("%Y%m%d%H%M%S")+".png"
    image.save(os.path.join('static/uploads',fn))
    res=predict(os.path.join('static/uploads',fn))
    print(res)
    opst=op[res[0]]
    img=fn
    print(img,"===========")
    q="SELECT * FROM `disease` WHERE disease=%s"
    res=selectone(q,opst)
    print(res['msg'],"============")
    return jsonify(status=opst,task="success",fn=img,des=res['description'],msg=res['msg'])


app.run(host='0.0.0.0',port=5000)