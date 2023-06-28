from flask import Flask,render_template,request
import mysql.connector
user_dict={'admin':'1234','user':'5678'}
conn = mysql.connector.connect(host='localhost',user='root',password='',database='kindergarten')
mycursor=conn.cursor()
#create a flask application
app = Flask(__name__)

#Define the route 

@app.route('/first')
def hello1():
    return render_template('first.html')
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
@app.route('/home1')
def home1():
    return render_template('home.html')
@app.route('/')
def hello():
    return render_template('first.html')
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
@app.route('/classes')
def classes():
    return render_template('classes.html')
@app.route('/student')
def student():
    return render_template('add_student.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/home',methods=['POST'])
def home():
    uname=request.form['username']
    pwd=request.form['password']

    if uname not in user_dict:
        return render_template('login.html',msg='Invalid User')
    elif user_dict[uname] != pwd:
        return render_template('login.html',msg='Invalid Password')
    else:
        return render_template('home.html')
@app.route('/view')
def view():
    query="SELECT * FROM student"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)

@app.route('/search')
def searchpage():
    return render_template('search.html')


@app.route('/searchresult',methods=['POST'])
def search():
    studid = request.form['stud_id']
    query="SELECT * FROM student WHERE STUD_ID="+studid
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)
@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/delete1',methods=['POST'])
def delete1():
    studid = request.form['stud_id']
    query="DELETE FROM student WHERE STUD_ID="+studid
    mycursor.execute(query)
    return render_template('delete.html',msgdata='Deleted Successfully')
    
@app.route('/add')
def add():
    return render_template('add_student.html')

@app.route('/read',methods=['POST'])
def read():
    stud_id = request.form['stud_id']
    stud_name = request.form['stud_name']
    age= request.form['age']
    dob = request.form['dob']
    guardian = request.form['guardian']
    section = request.form['section']
    email = request.form['email']
    query = "INSERT INTO student(stud_id,stud_name,age,dob,guardian,section,email) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    data = (stud_id,stud_name,age,dob,guardian,section,email)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('add_student.html',msgdata='Added Successfully')

#Run the flask app
if __name__=='__main__':
    app.run(port=5001,debug = True)