import pymongo 
from pymongo import MongoClient
from mongoengine import *
#from model import Post

#using pymongo
client = MongoClient()
db = client['hospitals'] 
hosp_details = db.hospital_details
hosp_data = {
    'hosp_id':'HD04',
    'hosp_name':'Sri Gowthami Multi Speciality Hospital',
    'hosp_email':'srigowthamimultispecialityhospital@gmail.com',
    'hosp_address':' D.No: 10-5-53, Nageswararao Street, Ramaraopeta, Kakinada - 04',
    'hosp_website':'inkakinada.com/list/sri-gowthami-multi-speciality-hospital',
    'hosp_specs':['Cardiology','General Surgeon','Gynecology','Dentist','General Medicine','Orthopaedics '],
    'hosp_mobile':['+(91)-0884-2376250','8842342398'],
    'hosp_facility':['ENMG','Stroke Care ICU',
                        '24 Hour Pharmacy','Ultra Sound Scanning'],
    'hosp_timings':'24 Hours',
    'doc_list':[{'hosp_id':'HD04','doc_id':'D022','doc_name':'Dr. Basker Jayaraman','doc_qualification':'MBBS, MD, DM','doc_specialization': 'Cardiology','doc_experience':'11 years','doc_fee':'500 /-'},
                {'hosp_id':'HD04','doc_id':'D023','doc_name':'Dr. P.V.V Satyanarayana','doc_qualification':'MBBS DV,MD','doc_specialization': 'General Surgeon','doc_experience':'22 years','doc_fee':'800 /-'},
                {'hosp_id':'HD04','doc_id':'D025','doc_name':'Dr.K Chandrakala','doc_qualification':'MBBS, DNB OBG','doc_specialization': 'Gynecology','doc_experience':'15 years','doc_fee':'800 /-'},
                {'hosp_id':'HD04','doc_id':'D026','doc_name':'Dr.T Mohanrao','doc_qualification':'M.d(dentist), M.B.B.S', 'doc_specialization':'Dentist','doc_experience':'16 years','doc_fee':'400 /-'},
                {'hosp_id':'HD04','doc_id':'D027','doc_name':'Dr.Vadrevu Ravi','doc_qualification':'M.D','doc_specialization': 'General Medicine','doc_experience':'10 years','doc_fee':'400 /-'},
                {'hosp_id':'HD04','doc_id':'D028','doc_name':'Dr. Sushanth Reddy','doc_qualification':'MBBS, D.Ortho, DNB Ortho', 'doc_specialization':'Orthopaedics','doc_experience':'21 years','doc_fee':'700 /-'}
                ]
}
hosp_details.insert_one(hosp_data)
print("inserted")
client.close()