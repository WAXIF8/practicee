from .resources import Test,ContactsAPIs,LoginApi,PatientsApi,PatientApi,DoctorApi,DoctorsApi,deletePatientApi,deleteDoctorApi

def initialize_routes(api):
    api.add_resource(Test, "/api/test")
    api.add_resource(ContactsAPIs, "/api/contacts/<id>")
    api.add_resource(LoginApi, "/api/Login")
    api.add_resource(PatientsApi, "/api/patients")
    api.add_resource(PatientApi, "/api/patient/<id>")
    api.add_resource(DoctorsApi, "/api/doctors")
    api.add_resource(DoctorApi, "/api/doctor/<id>")
    api.add_resource(deleteDoctorApi, "/api/doctorsall")
    api.add_resource(deletePatientApi, "/api/patientsall")










