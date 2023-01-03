from flask import Flask, jsonify,request, render_template,Response
from flask_restful import Api,Resource
from database import db
from resources import routes
from database.models import Login,Doctor,Patients
from flask_restful import Resource


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/clinic'}


api=Api(app)
db.initialize_db(app)
routes.initialize_routes(api)
@app.route('/signup')
def signup():
    return render_template("Signup.html")
@app.route('/register',methods=["POST"])
def register():
    username=request.form["username"]
    emails=request.form["email"]
    password=request.form["password"]
    obj = Login(name=username,email=emails,password=password).save()
    return render_template("Login.html")




@app.route('/')
def hello_world():  # put application's code here
    return render_template("Login.html")
@app.route('/addDoctor')
def addDoctor():
    return render_template("addDoctor.html")

@app.route('/addPatient' ,methods=["POST"])
def addpatient():
    return render_template("addPatient.html")

@app.route("/delpatient" ,methods=["POST"])
def delPati():
    id=request.form["pid"]
    Patients.objects.get(id=id).delete()
    return {'msg': "deleted"}, 200

@app.route("/deldoctor" ,methods=["POST"])
def delD():
    id=request.form["docid"]
    Doctor.objects.get(id=id).delete()
    obj = Patients.objects(doctorid=id).delete()
    return {'msg': "deleted"}, 200


@app.route("/showD")
def showD():
    return render_template("showDoctor.html")

@app.route("/updatePatient")
def updatepat():
    return  render_template("updatepatient.html")


@app.route("/updateP" ,methods=["POST"])
def updatep():
    id = request.form["id"]
    name = request.form["name"]
    age = request.form["age"]
    contact = request.form["contact"]
    bg = request.form["bg"]
    docid = request.form["docid"]
    try:
        Patients.objects.get(id=id).update(name=name,age=age,contact=contact,bloodGroup=bg,doctorid=docid)
    except Exception as e:
        return {'msg':"Error"}, 200
    return {'id': str(id)}, 200



@app.route("/updateD", methods=["POST"])
def updateD():
    id = request.form["id"]
    name=request.form["name"]
    age=request.form["age"]
    contact=request.form["contact"]
    spec=request.form["spec"]
    try:
        Doctor.objects.get(id=id).update(name=name,age=age,contact=contact,spec=spec)
    except Exception as e:
        return {'msg':"Error"}, 200
    return {'id': str(id)}, 200
@app.route("/updateDoctor")
def updateDoc():
    return render_template("updateDoctor.html")


@app.route("/searchpt",methods=["POST"])
def searchp():
    name = request.form["name"]
    obj = Patients.objects(name=name)
    list = [obj.name, obj.age, obj.contact, obj.bloodGroup, obj.doctorid]
    return render_template("showPatient2.html", li=list)




@app.route("/showP")
def showP():
    return render_template("showPatient.html")
@app.route("/login",methods=["POST"])
def login():
    email=request.form["name"]
    password=request.form["password"]
    obj=Login.objects(email=email)
    if len(obj)==0:
        print("Hello")
        return render_template("Login.html")
    for i in obj:
        if i.password==str(password):
            return render_template("Home.html")

    else:
        return render_template("Login.html")



if __name__ == '__main__':
    app.run()
