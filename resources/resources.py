from flask import request, Response, jsonify,render_template
from flask_restful import Resource
from database.models import contects,Login,Patients,Doctor
class ContactsAPIs(Resource):
    def delete(self,id):
        print("delete")
        contects.objects.get(id=id).delete()
        return {'id': str(id), 'delete': 'done'}, 200
    def put(self,id):
        print("put")
        reqdata=request.get_json()
        print(reqdata["name"])
        contects.objects.get(id=id).update(name=str(reqdata["name"]))
        return {'id': str(id)}, 200





class Test(Resource):
    def get(self):
        return jsonify({"msg":"Hello World"})
    def post(self):
        data = request.get_json()  # status code
        print(data)
        data.update(name="wasif")
        data.update(magic=78952369841)
        data.update(sep="operator")
        return data, 201
class LoginApi(Resource):
    def post(self):
        print("in Post")
        name=request.form["name"]
        password=request.form["password"]
        print("name",password)
        loginid=Login(name=str(name),password=str(password)).save()
        #return jsonify({"id":str(loginid.id),"name":str(name)})
        return render_template("Signup.html")
    def get(self):
        obj=Login.objects()
        print(obj[1]["name"])
        return Response(obj.to_json(), mimetype="application/json", status=200)
class PatientsApi(Resource):
    def get(self):
        patients = Patients.objects()
        return Response(patients.to_json(), mimetype="application/json", status=200)
    def post(self):
        body = request.get_json()
        if int(body["age"])<1:
            return {'msg': "Age is not correct"}, 200



        if body["bloodGroup"] not in ["A+","B+","AB+","AB-","O-","O+"]:
            return {'msg': "blood Group not correct"}, 200
        print(body["doctorid"])
        doctorid=None
        try:
            doctorid=Doctor.objects.get(id=str(body["doctorid"]))
        except Exception as e:
            print("Doctor not found")
            return {'msg': "Doctor Not Found"}, 200
        veh=Patients(**body).save()
        id = veh.id
        return {'id': str(id)}, 200

class PatientApi(Resource):
    def put(self,id):
        body = request.get_json()
        doctorid = None
        try:
            doctorid = Doctor.objects.get(id=str(body["doctorid"]))
        except Exception as e:
            print("Doctor not found")
            return {'msg': "Doctor Not Found"}, 200
        if int(body["age"])<1:
            return {'msg': "Age is not correct"}, 200



        if body["bloodGroup"] not in ["A+","B+","AB+","AB-","O-","O+"]:
            return {'msg': "blood Group not correct"}, 200
        Patients.objects.get(id=id).update(**body)
        return {'id': str(id)}, 200
    def delete(self,id):
        print("in patient delete")
        Patients.objects.get(id=id).delete()
        return {'msg':"deleted"}, 200
class DoctorsApi(Resource):
    def get(self):
        doc = Doctor.objects()
        print("In get")
        return Response(doc.to_json(), mimetype="application/json", status=200)
    def post(self):
        body = request.get_json()
        print(body)
        if int(body["age"]) < 1:
            return {'msg': "Age is not correct"}, 200
        veh=Doctor(**body).save()
        #veh = Vehicle(reg=body["reg"], model=body["model"]).save()
        id = veh.id
        return {'id': str(id)}, 200
class DoctorApi(Resource):
    def put(self,id):
        print("In put")
        body = request.get_json()
        if int(body["age"])<1:
            return {'msg': "Age is not correct"}, 200
        Doctor.objects.get(id=id).update(**body)
        return {'id': str(id)}, 200
    def Delete(self,id):
        print("in doctor delete")
        Doctor.objects.get(id=id).delete()
        obj=Patients.objects(doctorid=id).delete()
        return {'msg':"deleted"}, 200

class deleteDoctorApi(Resource):
    def delete(self):
        Doctor.objects.delete()
        Patients.objects.delete()
class deletePatientApi(Resource):
    def delete(self):
         Patients.objects.delete()
         return {'msg': "deleted"}, 200









