import functools
from flask import *
from src.dbconnectionnew import *
import _functools
app=Flask(__name__)
app.secret_key="hgy"



def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return render_template('loginINDEX.html')
        return func()

    return secure_function


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/')
def log():
    return render_template('loginINDEX.html')

@app.route('/LOGIN',methods=['get','post'])
def LOGIN():
    username=request.form['textfield']
    password=request.form['textfield2']
    qry="SELECT * FROM `login` WHERE `username`=%s AND `password`=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
     return'''<script>alert("invalid"); window.location='/'</script>'''
    elif res['type']=='admin':
        session['lid']=res['id']
        return '''<script>alert("welcome admin"); window.location='/admnhom'</script>'''
    elif res['type']=='doctor':
        try:
            qry = "SELECT `doctor`.`fname`,`lname` FROM `doctor` WHERE `lid`=%s"
            res1 = selectone(qry,res['id'])
            session['name'] = res1['fname']+" "+res1['lname']

            print(session['name'])

            session['lid'] = res['id']
            return '''<script>alert("welcome doctor"); window.location='/dochome'</script>'''
        except:
            session['lid'] = res['id']
            return '''<script>alert("welcome doctor"); window.location='/dochome'</script>'''
    else:
        return '''<script>alert("invalid"); window.location='/'</script>'''



@app.route('/adddoc',methods=['get','post'])
@login_required
def adddoc():
    return render_template('adddoctor.html')
@app.route('/adddoctor',methods=['get','post'])
def adddoctor():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    gender = request.form['radiobutton']
    Place=request.form['textarea2']
    Post=request.form['textfield3']
    Pin=request.form['textfield4']
    email =request.form['textfield5']
    Phn = request.form['textfield6']
    qualif=request.form['textarea3']
    exper = request.form['textarea4']
    regno=request.form['regno']
    username = request.form['textfield7']
    password = request.form['textfield8']
    qry="insert into login values(null,%s,%s,'doctor')"
    val=(username,password)
    id=iud(qry,val)
    qry = "insert into doctor values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (str(id),fname,lname,email,Phn,Place,Post,Pin,qualif,exper,gender,regno)
    iud(qry, val)
    return '''<script>alert("added");window.location='/mngdoc'</script>'''

@app.route('/addsch',methods=['get','post'])
@login_required
def addsch():

    return render_template('Addschedule.html')
@app.route('/admnhom',methods=['get','post'])
@login_required
def admnhom():
    return render_template('Adminhom.html')
@app.route('/dochome',methods=['get','post'])
@login_required
def dochome():
    return render_template('dochome.html')
@app.route('/login',methods=['get','post'])
@login_required
def login():
    return render_template('login.html')


@app.route('/manageschedule',methods=['get','post'])
@login_required
def manageschedule():
    qry="select * from shedule where docid=%s"
    res=selectall2(qry,session['lid'])
    print(res)
    return render_template('Manageschedule.html',val=res)


@app.route('/mngdoc',methods=['get','post'])
@login_required
def mngdoc():
    qry="select * from doctor"
    res=selectall(qry)

    return render_template('MNGDOC.html',val=res)


@app.route('/viewdcrev',methods=['get','post'])
@login_required
def viewdcrev():
    qry="SELECT `doctor`.`fname`,`lname`,`review`.* FROM `doctor` JOIN`review` ON`doctor`.`lid`=`review`.`docid`"
    res = selectall(qry)

    return render_template('viewdcrev.html',val=res)
@app.route('/viewfeed',methods=['get','post'])
@login_required
def viewfeed():
    qry="SELECT `user`. `fname`,`lname`,`feedback`.`feedback`,`date` FROM `user` JOIN `feedback` ON `user`.`lid`=`feedback`.`user_id`"
    res=selectall(qry)
    return render_template('viewfeed.html',val=res)

@app.route('/Viewprofile',methods=['get','post'])
@login_required
def Viewprofile():
    qry="SELECT * FROM `doctor`WHERE `lid`=%s"
    res=selectone(qry,session['lid'])
    print(session['lid'])
    return render_template('Viewprofile.html',val=res)
@app.route('/viewreviews',methods=['get','post'])
@login_required
def viewreviews():
    qry="SELECT `user`.fname,lname,`review`.* FROM `user`JOIN `review`ON `user`.lid=`review`.`userid`"
    res=selectall(qry)
    return render_template('viewreviews.html',val=res)




@app.route('/edit_sche')
def edit_sche():
    id = request.args.get('id')
    session['sid']=id
    qry = "select * from shedule where sid=%s"
    res = selectone(qry,id)
    return render_template('editschedule.html',i=res)


@app.route('/viewbooking',methods=['get','post'])
@login_required
def viewbooking():


    qry="SELECT `booking`.`bid`,`booking`.`date` AS bdate ,`booking`.`status`,`shedule`.*,`user`.`fname`,`lname` FROM `shedule` JOIN `booking` ON `shedule`.`sid`=`booking`.`sid` JOIN `user` ON `booking`.`userid`=`user`.`lid` WHERE `shedule`.`docid`=%s"
    val=(session['lid'])
    res=selectall2(qry,val)
    print(res)
    return render_template('viewbooking.html',val=res)

@app.route('/fromto',methods=['get','post'])
def fromto():
    return render_template('fromto.html')

@app.route('/fromto1',methods=['get','post'])
def fromto1():
    ffrom = request.form['textfield']
    to = request.form['textfield2']
    qry = "insert into shedule values(null,%s,%s,%s,curdate())"
    val = (str(session['lid']), ffrom, to)
    iud(qry, val)
    return '''<script>alert("Added"); window.location='/manageschedule'</script>'''


@app.route('/viewusr',methods=['get','post'])
def viewusr():
    qry="select * from user"
    res=selectall(qry)

    return render_template('viewusr.html',val=res)

@app.route('/chatwin',methods=['get','post'])
def chatwin():
    qry="SELECT *FROM `user`"
    res=selectall(qry)
    return render_template('chatwin.html',val=res)
@app.route('/updoc',methods=['get','post'])
def updoc():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    gender = request.form['radiobutton']
    Place = request.form['textarea2']
    Post = request.form['textfield3']
    Pin = request.form['textfield4']
    email = request.form['textfield5']
    Phn = request.form['textfield6']
    qualif = request.form['textarea3']
    exper = request.form['textarea4']

    qry="UPDATE `doctor`SET `fname`=%s,`lname`=%s,`gender`=%s,`place`=%s,`post`=%s,`pin`=%s,`email`=%s,`phone`=%s,`qualification`=%s,`experience`=%s where `lid`=%s"
    val = (fname, lname, gender ,  Place, Post, Pin, email,Phn, qualif, exper,session['lid'])
    iud(qry, val)
    return '''<script>alert("updated"); window.location='/dochome'</script>'''
# @app.route('/editsched',methods=['get','post'])
# def editsched():
#     ffrom = request.form['textfield']
#     to = request.form['textfield2']
#     qry=""
@app.route('/delsche',methods=['get','post'])
def delsche():
    id=request.args.get('id')

    qry="delete from shedule where sid=%s"
    iud(qry, id)
    return '''<script>alert("deleted"); window.location='/manageschedule'</script>'''

@app.route('/updateschedule',methods=['get','post'])
def updateschedule():
    fromto = request.form['textfield']
    totime = request.form['textfield2']
    qry="UPDATE `shedule`SET `from_time`=%s,`to_time`=%s where `sid`=%s"
    val=(fromto, totime,str(session['sid']) )
    iud(qry, val)
    return '''<script>alert("updated"); window.location='/manageschedule'</script>'''

@app.route('/edit_doc',methods=['get','post'])
def edit_doc():
    id = request.args.get('id')
    session['docid'] = id
    qry="select * from doctor where lid=%s"
    res=selectone(qry,id)
    print(res)
    return render_template('editdoctor.html',val=res)


@app.route('/edit_doc1',methods=['get','post'])
def edit_doc1():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    gender = request.form['radiobutton']
    Place=request.form['textarea2']
    Post=request.form['textfield3']
    Pin=request.form['textfield4']
    email =request.form['textfield5']
    Phn = request.form['textfield6']
    qualif=request.form['textarea3']
    exper = request.form['textarea4']
    qry = "UPDATE `doctor`SET `fname`=%s,`lname`=%s ,`gender`=%s,`place`=%s,`post`=%s,`pin`=%s,`email`=%s,`qualification`=%s,`experience`=%s,`phone`=%s where `lid`=%s"
    val = (fname,lname,gender,Place,Post,Pin,email,qualif,exper,Phn,session['docid'])
    iud(qry, val)
    return '''<script>alert("YEAH YOU UPDATED !!");window.location='/mngdoc'</script>'''

@app.route('/dlt_doc',methods=['get','post'])
def dlt_doc():
    id=request.args.get('id')
    qry="delete from doctor where lid=%s"
    iud(qry, id)
    q="delete from login where id=%s"
    iud(q,str(id))
    return '''<script>alert("deleted"); window.location='/mngdoc'</script>'''



# ///////////////////////////////////////////////////
@app.route("/chat2")
def chatsp():
    pid=request.args.get('uid')
    print(pid,"==============================")
    session['pid']=pid
    qry="SELECT * FROM `user` WHERE `lid`=%s"
    res=selectone(qry,pid)


    print(res)

    qry="   SELECT * FROM `chat` WHERE `fromid`=%s AND `toid`=%s OR `fromid`=%s AND `toid`=%s"


    val=(session['lid'],session['pid'],session['pid'],session['lid'])
    res1=selectall2(qry,val)

    print(res)

    fname=res['fname']
    lname=res['lname']
    return render_template("chat2.html",data=res1,fname=fname,lname=lname,fr=session['lid'])



@app.route('/send',methods=['post'])
def sendchat():
    message=request.form['textarea']
    to_id = session['pid']
    from_id = session['lid']
    qry="insert into chat values(null,%s,%s,%s,CURDATE())"
    val=(from_id,to_id,message)
    iud(qry,val)


    return redirect("chatss")
@app.route("/chatss")
def chatss():
    pid=session['pid']
    qry="SELECT * FROM `user` WHERE `lid`=%s"
    res=selectone(qry,pid)
    qry="   SELECT * FROM `chat` WHERE `fromid`=%s AND `toid`=%s OR `fromid`=%s AND `toid`=%s"
    val=(session['lid'],session['pid'],session['pid'],session['lid'])
    res1=selectall2(qry,val)
    print('1234567',res1)
    fname=res['fname']
    lname=res['lname']
    return render_template("chat2.html",data=res1,fname=fname,lname=lname,fr=session['lid'])


@app.route('/accept',methods=['get','post'])
def accept():
    id=request.args.get('id')
    qry = "update booking set status='accepted' where bid =%s"
    iud(qry,str(id))
    return '''<script>alert("YEAH YOU accepted !!");window.location='/viewbooking'</script>'''




@app.route('/reject',methods=['get','post'])
def reject():
    id=request.args.get('id')
    qry = "update booking set status='rejected' where bid =%s"
    iud(qry, str(id))
    return'''<script>alert(" Rejected !!");window.location='/viewbooking'</script>'''



app.run(debug=True)







