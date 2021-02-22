
"""import pymongo 
from pymongo import MongoClient
from mongoengine import *
#from model import Post

#using pymongo
client = MongoClient()
db = client['hospitals'] 
hosp_details = db.hospital_details
hosp_data = {
    'hosp_id':'HD01',
    'hosp_name':'Kusuma Hospital',
    'hosp_email':'kusumahospital@gmail.com',
    'hosp_address':' Town Railway Station Road,Ramaraopeta, Kakinada - 04',
    'hosp_website':'http://www.inkakinada.com/category/services',
    'hosp_specs':['Cardiology','General Surgeon','Endocrinology','Gynecology','Dentist','Pediatricians','Ayurvedic'],
    'hosp_mobile':['+91 9238888358','91)-884-2364882'],
    'hosp_facility':['ENMG','24 Hour Pharmacy',' CT Scan','Pharmacy','MRI Scan'],
    'hosp_timings':'24 Hours',
    'doc_list':[{'hosp_id':'HD01','doc_id':'D001','doc_name':'Dr. Nitesh Prasad','doc_qualification':'MBBS, MD, DM','doc_specialization': 'Cardiologist','doc_experience':'10 years','doc_fee':'500 /-'},
                {'hosp_id':'HD01','doc_id':'D002','doc_name':'Dr. Anoop Kumar Modi','doc_qualification':'MBBS DV,MD','doc_specialization': 'General Surgeon','doc_experience':'18 years','doc_fee':'800 /-'},
                {'hosp_id':'HD01','doc_id':'D003','doc_name':'Dr. Manish Verma','doc_qualification':'MS(Clinical Endocrinology)','doc_specialization': 'Endocrinologist','doc_experience':'16 years','doc_fee':'850 /-'},
                {'hosp_id':'HD01','doc_id':'D004','doc_name':'Dr. Venkat Reddy ','doc_qualification':'MBBS, DNB OBG','doc_specialization': 'Gynecologist','doc_experience':'8 years','doc_fee':'300 /-'},
                {'hosp_id':'HD01','doc_id':'D005','doc_name':'Dr. Arun','doc_qualification':'M.d(dentist), M.B.B.S', 'doc_specialization':'Dentist','doc_experience':'10 years','doc_fee':'400 /-'},
                {'hosp_id':'HD01','doc_id':'D006','doc_name':'Dr. Savitha Nagendra','doc_qualification':'MBBS,DCH,MD','doc_specialization': 'Pediatricians','doc_experience':'16 years','doc_fee':'850 /-'},
                {'hosp_id':'HD01','doc_id':'D008','doc_name':'Dr. Diwya Tyagi','doc_qualification':'B.A.MS', 'doc_specialization':'Ayurvedic','doc_experience':'29 years','doc_fee':'800 /-'}
                ]
}
hosp_details.insert_one(hosp_data)
print("inserted")
client.close()

import pymongo 
from pymongo import MongoClient
from mongoengine import *
#from model import Post

#using pymongo
client = MongoClient()
db = client['hospitals'] 
hosp_details = db.hospital_details
hosp_data = {
    'hosp_id':'HD05',
    'hosp_name':'Srujana Multi Speciality Hospital',
    'hosp_email':'srujanamultispecialityhospital@gmail.com',
    'hosp_address':' D.No:2-28-24/1, Gokul Street, Sri Nagar, Kakinada - 03',
    'hosp_website':'http://www.inkakinada.com/list/srujana-multi-specialty-hospital',
    'hosp_specs':['Cardiology','General Surgeon','Pulmonology','Gynecology','Dentist','Anaesthesiology','Orthopedics '],
    'hosp_mobile':['+91 9440358358','+(91)-0884-2361669'],
    'hosp_facility':['ENMG','Stroke Care ICU',
                        '24 Hour Pharmacy','CT Scan',
                        'Pharmacy','MRI Scan'],
    'hosp_timings':'24 Hours',
    'doc_list':[{'hosp_id':'HD05','doc_id':'D029','doc_name':'Dr. P. Raju','doc_qualification':'MBBS, MD, DM','doc_specialization': 'Cardiology','doc_experience':'15 years','doc_fee':'500 /-'},
                {'hosp_id':'HD05','doc_id':'D030','doc_name':'Dr. Praveennath Ghanta','doc_qualification':'MBBS DV,MD','doc_specialization': 'General Surgeon','doc_experience':'12 years','doc_fee':'400 /-'},
                {'hosp_id':'HD05','doc_id':'D031','doc_name':'Dr Raju Pampana','doc_qualification':'MBBS, MD - Pulmonary Medicine','doc_specialization': 'Pulmonology','doc_experience':'11 years','doc_fee':'550 /-'},
                {'hosp_id':'HD05','doc_id':'D032','doc_name':'Dr. T. Ananatha Lakshmi','doc_qualification':'MBBS, DNB OBG','doc_specialization': 'Gynecology','doc_experience':'18 years','doc_fee':'800 /-'},
                {'hosp_id':'HD05','doc_id':'D033','doc_name':'Dr. P.Sai krishna','doc_qualification':'M.d(dentist), M.B.B.S', 'doc_specialization':'Dentist','doc_experience':'12 years','doc_fee':'400 /-'},
                {'hosp_id':'HD05','doc_id':'D034','doc_name':'Dr. K.Krishna Vara Prasad','doc_qualification':'MBBS, Diploma in Anesthesiology','doc_specialization': 'Anaesthesiology','doc_experience':'8 years','doc_fee':'400 /-'},
                {'hosp_id':'HD05','doc_id':'D035','doc_name':'Dr. Satish','doc_qualification':'MBBS, D.Ortho, DNB Ortho', 'doc_specialization':'Orthopedics','doc_experience':'28 years','doc_fee':'800 /-'}
                ]
}
hosp_details.insert_one(hosp_data)
print("inserted")
client.close()
#################################
import pymongo 
from pymongo import MongoClient
from mongoengine import *
#from model import Post

#using pymongo
client = MongoClient()
db = client['hospitals'] 
hosp_details = db.hospital_details
hosp_data = {
    'hosp_id':'HD06',
    'hosp_name':'Sri Sai Raghavendra Super Specialities Hospital',
    'hosp_email':'srisairaghavendrasuperspecialities@gmail.com',
    'hosp_address':' 8-5-19/1, Ontimamidi junction,Gandhi Nagar, Kakinada - 04',
    'hosp_website':'http://www.inkakinada.com/list/sri-sai-raghavendra-super-specialities-hospital',
    'hosp_specs':['Cardiology','General Surgeon','Pulmonology','Gynecology','Dentist','Anaesthesiology','Orthopedics'],
    'hosp_mobile':['+91 9238888358','(+91)-884-2364882'],
    'hosp_facility':['ENMG','Stroke Care ICU',
                        '24 Hour Pharmacy', 'CT Scan',
                        'Pharmacy','MRI Scan'],
    'hosp_timings':'24 Hours',
    'doc_list':[{'hosp_id':'HD06','doc_id':'D036','doc_name':'Dr. Satyanarayana Kondamuri','doc_qualification':'MBBS, MD, DM','doc_specialization': 'Cardiologist','doc_experience':'9 years','doc_fee':'500 /-'},
                {'hosp_id':'HD06','doc_id':'D038','doc_name':'Dr. Sravanthi Mandipudi','doc_qualification':'MBBS DV,MD','doc_specialization': 'General Surgeon','doc_experience':'22 years','doc_fee':'800 /-'},
                {'hosp_id':'HD06','doc_id':'D038','doc_name':'Dr. Kondamuri Satyanaraya','doc_qualification':'MBBS, MD - Pulmonary Medicine','doc_specialization': 'Pulmonologist','doc_experience':'14 years','doc_fee':'850 /-'},
                {'hosp_id':'HD06','doc_id':'D039','doc_name':'Dr. Aruna Kumari ','doc_qualification':'MBBS, DNB OBG','doc_specialization': 'Gynecologist','doc_experience':'6 years','doc_fee':'300 /-'},
                {'hosp_id':'HD06','doc_id':'D040','doc_name':'Dr. Ravi Chandra','doc_qualification':'M.d(dentist), M.B.B.S', 'doc_specialization':'Dentist','doc_experience':'12 years','doc_fee':'400 /-'},
                {'hosp_id':'HD06','doc_id':'D041','doc_name':'Dr. Animesh Majhi','doc_qualification':'MBBS, Diploma in Anesthesiology','doc_specialization': 'Anaesthesiology','doc_experience':'16 years','doc_fee':'800 /-'},
                {'hosp_id':'HD06','doc_id':'D042','doc_name':'Dr. Abhishek Chatterjee','doc_qualification':'MBBS, D.Ortho, DNB Ortho', 'doc_specialization':'Orthopedics Surgeons','doc_experience':'12 years','doc_fee':'800 /-'}
                ]
}
hosp_details.insert_one(hosp_data)
print("inserted")
client.close()

import pymongo 
from pymongo import MongoClient
from mongoengine import *
#from model import Post

#using pymongo
client = MongoClient()
db = client['hospitals'] 
hosp_details = db.hospital_details
hosp_data = {
    'hosp_id':'HD12',
    'hosp_name':'Baggu Sarojini Devi Hospital',
    'hosp_email':'baggusarojinidevihospital@gmail.com',
    'hosp_address':' Door No 2-2-132, Srikakulam Ho, Srikakulam - 532001, Near Illispuram Junction',
    'hosp_website':'https://www.medindia.net/patients/hospital_search/baggu-sarojini-devi-hospital-srikakulam-andhra-pradesh-28949-1.htm',
    'hosp_specs':['Cardiology','General Surgeon',' ENT','Gynecology','Dentist','Anaesthesiology','Orthopedics'],
    'hosp_mobile':['+91 9238888358','(+91)-884-2364882'],
    'hosp_facility':['ENMG','Stroke Care ICU',
                        '24 Hour Pharmacy', 'CT Scan',
                        'Pharmacy','MRI Scan'],
    'hosp_timings':'24 Hours',
    'doc_list':[{'hosp_id':'HD12','doc_id':'D043','doc_name':'Dr. K Sravani Reddy','doc_qualification':'MBBS, MD, DM','doc_specialization': 'Cardiology','doc_experience':'12 years','doc_fee':'600 /-'},
                {'hosp_id':'HD12','doc_id':'D044','doc_name':'Dr. Sravanthi Mandipudi','doc_qualification':'MBBS DV,MD','doc_specialization': 'General Surgeon','doc_experience':'22 years','doc_fee':'800 /-'},
                {'hosp_id':'HD12','doc_id':'D045','doc_name':'Dr. Shakuntala Ghosh','doc_qualification':'MBBS, MS - ENT','doc_specialization': ' ENT','doc_experience':'24 years','doc_fee':'900 /-'},
                {'hosp_id':'HD12','doc_id':'D046','doc_name':'Dr. Sudha Chitumalla ','doc_qualification':'MBBS, DNB OBG','doc_specialization': 'Gynecologist','doc_experience':'6 years','doc_fee':'300 /-'},
                {'hosp_id':'HD12','doc_id':'D048','doc_name':'Dr. Madhukar Neerudu','doc_qualification':'M.d(dentist), M.B.B.S', 'doc_specialization':'Dentist','doc_experience':'12 years','doc_fee':'400 /-'},
                {'hosp_id':'HD12','doc_id':'D048','doc_name':'Dr. Nikhil Saran','doc_qualification':'MBBS, Diploma in Anesthesiology','doc_specialization': 'Anaesthesiology','doc_experience':'16 years','doc_fee':'800 /-'},
                {'hosp_id':'HD12','doc_id':'D049','doc_name':'Dr. Rashmi','doc_qualification':'MBBS, D.Ortho, DNB Ortho', 'doc_specialization':'Orthopedics','doc_experience':'15 years','doc_fee':'800 /-'}
                ]
}
hosp_details.insert_one(hosp_data)
print("inserted")
client.close()

import pymongo 
from pymongo import MongoClient
from mongoengine import *
#from model import Post

#using pymongo
client = MongoClient()
db = client['hospitals'] 
hosp_details = db.hospital_details
hosp_data = {
    'hosp_id':'HD12',
    'hosp_name':'Kamala Hospital',
    'hosp_email':'kamalahospital@gmail.com',
    'hosp_address':' Srikakulam Ho, Srikakulam - 532001, Ellisipuram Junction',
    'hosp_website':'https://www.justdial.com/Srikakulam/Kamala-Hospital-Ellisipuram-Junction-Srikakulam-Ho/9999P8942-8942-090728130459-R5R3DC_BZDET',
    'hosp_specs':['Cardiology','General Surgeon',' ENT','Gynecology','Dentist','Pediatrics','Orthopedics'],
    'hosp_mobile':['+91 9238888358','(+91)-884-2364882'],
    'hosp_facility':['ENMG',
                        '24 Hour Pharmacy', 'CT Scan',
                        'Pharmacy','MRI Scan'],
    'hosp_timings':'24 Hours',
    'doc_list':[{'hosp_id':'HD12','doc_id':'D050','doc_name':'Dr. Vikram Dantoori','doc_qualification':'MBBS, MD, DM','doc_specialization': 'Cardiology','doc_experience':'14 years','doc_fee':'600 /-'},
                {'hosp_id':'HD12','doc_id':'D051','doc_name':'Dr. Rahul Reddy','doc_qualification':'MBBS DV,MD','doc_specialization': 'General Surgeon','doc_experience':'8 years','doc_fee':'800 /-'},
                {'hosp_id':'HD12','doc_id':'D052','doc_name':'Dr. Shakuntala Ghosh','doc_qualification':'MBBS, MS - ENT','doc_specialization': ' ENT','doc_experience':'17 years','doc_fee':'900 /-'},
                {'hosp_id':'HD12','doc_id':'D053','doc_name':'Dr. Srinivas Midivelly ','doc_qualification':'MBBS, DNB OBG','doc_specialization': 'Gynecologist','doc_experience':'11 years','doc_fee':'300 /-'},
                {'hosp_id':'HD12','doc_id':'D054','doc_name':'Dr. Chetan Varma','doc_qualification':'M.d(dentist), M.B.B.S', 'doc_specialization':'Dentist','doc_experience':'12 years','doc_fee':'400 /-'},
                {'hosp_id':'HD12','doc_id':'D055','doc_name':'Dr. Nikhila Ayyar','doc_qualification':'MD (Pediatrics), FPCCI','doc_specialization': 'Pediatrics','doc_experience':'6 years','doc_fee':'800 /-'},
                {'hosp_id':'HD12','doc_id':'D056','doc_name':'Dr. Rashmitha','doc_qualification':'MBBS, D.Ortho, DNB Ortho', 'doc_specialization':'Orthopedics','doc_experience':'15 years','doc_fee':'800 /-'}
                ]
}
hosp_details.insert_one(hosp_data)
print("inserted")
client.close()

import pymongo 
from pymongo import MongoClient
from mongoengine import *
#from model import Post

#using pymongo
client = MongoClient()
db = client['hospitals'] 
hosp_details = db.hospital_details
hosp_data = {
    'hosp_id':'HD01',
    'hosp_name':'Kusuma Hospital',
    'hosp_email':'kusumahospital@gmail.com',
    'hosp_address':' Town Railway Station Road,Ramaraopeta, Kakinada - 04',
    'hosp_website':'http://www.inkakinada.com/category/services',
    'hosp_specs':['Cardiology','General Surgeon','Endocrinology','Gynecology','Dentist','Pediatrics','Ayurvedic'],
    'hosp_mobile':['+91 9237788358','91)-884-2364772'],
    'hosp_facility':['ENMG','24 Hour Pharmacy',' CT Scan','Pharmacy','MRI Scan'],
    'hosp_timings':'24 Hours',
    'doc_list':[{'hosp_id':'HD01','doc_id':'D001','doc_name':'Dr. Nitesh Prasad','doc_qualification':'MBBS, MD, DM','doc_specialization': 'Cardiologist','doc_experience':'10 years','doc_fee':'500 /-'},
                {'hosp_id':'HD01','doc_id':'D002','doc_name':'Dr. Anoop Kumar Modi','doc_qualification':'MBBS DV,MD','doc_specialization': 'General Surgeon','doc_experience':'18 years','doc_fee':'800 /-'},
                {'hosp_id':'HD01','doc_id':'D003','doc_name':'Dr. Manish Verma','doc_qualification':'MS(Clinical Endocrinology)','doc_specialization': 'Endocrinologist','doc_experience':'16 years','doc_fee':'750 /-'},
                {'hosp_id':'HD01','doc_id':'D004','doc_name':'Dr. Venkat Reddy ','doc_qualification':'MBBS, DNB OBG','doc_specialization': 'Gynecologist','doc_experience':'8 years','doc_fee':'300 /-'},
                {'hosp_id':'HD01','doc_id':'D005','doc_name':'Dr. Arun','doc_qualification':'M.d(dentist), M.B.B.S', 'doc_specialization':'Dentist','doc_experience':'10 years','doc_fee':'400 /-'},
                {'hosp_id':'HD01','doc_id':'D006','doc_name':'Dr. Savitha Nagendra','doc_qualification':'MBBS,DCH,MD','doc_specialization': 'Pediatricians','doc_experience':'16 years','doc_fee':'750 /-'},
                {'hosp_id':'HD01','doc_id':'D007','doc_name':'Dr. Diwya Tyagi','doc_qualification':'B.A.MS', 'doc_specialization':'Ayurvedic','doc_experience':'29 years','doc_fee':'700 /-'}
                ]
}
hosp_details.insert_one(hosp_data)
print("inserted")
client.close()


import pymongo 
from pymongo import MongoClient
from mongoengine import *
#from model import Post

#using pymongo
client = MongoClient()
db = client['hospitals'] 
hosp_details = db.hospital_details
hosp_data = {
    'hosp_id':'HD12',
    'hosp_name':'Sindhura Hospital',
    'hosp_email':'sindhurahospital@gmail.com',
    'hosp_address':' Convent Jn ., Pasagada Layout,Ambedkar Junction, Srikakulam - 532001',
    'hosp_website':'https://www.justdial.com/Srikakulam/Sindhura-Hospitals-Ambedkar-Junction/9999P8942-8942-090820090705-Q9N4DC_BZDET',
    'hosp_specs':['Cardiology','Urology',' ENT','Gynecology','Dentist','Pediatrics','Orthopedics'],
    'hosp_mobile':['+91 9238907358','(+91)-774-2789882'],
    'hosp_facility':['ENMG',
                        '24 Hour Pharmacy', 'CT Scan',
                        'Pharmacy','MRI Scan'],
    'hosp_timings':'24 Hours',
    'doc_list':[{'hosp_id':'HD12','doc_id':'D057','doc_name':'Dr. Sriharsha Ajjur','doc_qualification':'MBBS, MD, DM','doc_specialization': 'Cardiology','doc_experience':'14 years','doc_fee':'400 /-'},
                {'hosp_id':'HD12','doc_id':'D060','doc_name':'Dr. Nipun ','doc_qualification':' MCh - Urology, MBBS','doc_specialization': 'Urologist','doc_experience':'10 years','doc_fee':'800 /-'},
                {'hosp_id':'HD12','doc_id':'D061','doc_name':'Dr. Premkumar K','doc_qualification':'MBBS, MS - ENT','doc_specialization': ' ENT','doc_experience':'12 years','doc_fee':'900 /-'},
                {'hosp_id':'HD12','doc_id':'D062','doc_name':'Dr. Prashanth Kulkarni ','doc_qualification':'MBBS, DNB OBG','doc_specialization': 'Gynecologist','doc_experience':'11 years','doc_fee':'300 /-'},
                {'hosp_id':'HD12','doc_id':'D063','doc_name':'Dr. Rajeev Bashetty','doc_qualification':'M.d(dentist), M.B.B.S', 'doc_specialization':'Dentist','doc_experience':'22 years','doc_fee':'400 /-'},
                {'hosp_id':'HD12','doc_id':'D064','doc_name':'Dr. Nikhila Reddy','doc_qualification':'MD (Pediatrics), FPCCI','doc_specialization': 'Pediatrics','doc_experience':'9 years','doc_fee':'800 /-'},
                {'hosp_id':'HD12','doc_id':'D065','doc_name':'Dr. Rohith Varma','doc_qualification':'MBBS, D.Ortho, DNB Ortho', 'doc_specialization':'Orthopedics','doc_experience':'15 years','doc_fee':'800 /-'}
                ]
}
hosp_details.insert_one(hosp_data)
print("inserted")
client.close()

import pymongo 
from pymongo import MongoClient
from mongoengine import *
#from model import Post

#using pymongo
client = MongoClient()
db = client['hospitals'] 
hosp_details = db.hospital_details
hosp_data = {
    'hosp_id':'HD12',
    'hosp_name':'Sri Venkata Sai Hospital',
    'hosp_email':'srivenkatasaihospital@gmail.com',
    'hosp_address':' Main Road, Pallipeta Junction, Narasannapeta, Srikakulam - 532421',
    'hosp_website':'https://www.justdial.com/Srikakulam/SRI-VENKATA-SAI-HOSPITAL-Narasannapeta/9999P8942-8942-171231223105-M1X2_BZDET',
    'hosp_specs':['Cardiology','Urology',' ENT','Gynecology','Dentist','Pediatrics','Orthopedics'],
    'hosp_mobile':['+91 897607358','8979189882'],
    'hosp_facility':['ENMG',
                        '24 Hour Pharmacy', 'CT Scan',
                        'Pharmacy','MRI Scan'],
    'hosp_timings':'24 Hours',
    'doc_list':[{'hosp_id':'HD12','doc_id':'D066','doc_name':'Dr. Arun L Naik','doc_qualification':'MBBS, MD, DM','doc_specialization': 'Cardiology','doc_experience':'8 years','doc_fee':'400 /-'},
                {'hosp_id':'HD12','doc_id':'D067','doc_name':'Dr. Praveen Ganigi ','doc_qualification':' MCh - Urology, MBBS','doc_specialization': 'Urologist','doc_experience':'10 years','doc_fee':'800 /-'},
                {'hosp_id':'HD12','doc_id':'D068','doc_name':'Dr. Sunil','doc_qualification':'MBBS, MS - ENT','doc_specialization': ' ENT','doc_experience':'17 years','doc_fee':'900 /-'},
                {'hosp_id':'HD12','doc_id':'D069','doc_name':'Dr. Akshay Hari ','doc_qualification':'MBBS, DNB OBG','doc_specialization': 'Gynecologist','doc_experience':'11 years','doc_fee':'300 /-'},
                {'hosp_id':'HD12','doc_id':'D070','doc_name':'Dr. Krishna Chaitanya','doc_qualification':'M.d(dentist), M.B.B.S', 'doc_specialization':'Dentist','doc_experience':'22 years','doc_fee':'400 /-'},
                {'hosp_id':'HD12','doc_id':'D071','doc_name':'Dr. Akhil Shetty','doc_qualification':'MD (Pediatrics), FPCCI','doc_specialization': 'Pediatrics','doc_experience':'9 years','doc_fee':'800 /-'},
                {'hosp_id':'HD12','doc_id':'D072','doc_name':'Dr. Naveen Varma','doc_qualification':'MBBS, D.Ortho, DNB Ortho', 'doc_specialization':'Orthopedics','doc_experience':'15 years','doc_fee':'800 /-'}
                ]
}
hosp_details.insert_one(hosp_data)
print("inserted")
client.close()


import pymongo 
from pymongo import MongoClient
from mongoengine import *
#from model import Post

#using pymongo
client = MongoClient()
db = client['hospitals'] 
hosp_details = db.hospital_details
hosp_data = {
    'hosp_id':'HD12',
    'hosp_name':'GMR Varalakshmi Care Hospital',
    'hosp_email':'gmr varalakshmicare@gmail.com',
    'hosp_address':'Hospital Rd, GMR Nagar, Near Andhra Bank GMR Nagar, Srikakulam District',
    'hosp_website':'http://gmrcarehospitals.in/home.html',
    'hosp_specs':['Cardiology','Urology',' ENT','Gynecology','Dentist','Pediatrics','Orthopedics'],
    'hosp_mobile':['+91 997007358','9989189882'],
    'hosp_facility':['ENMG',
                        '24 Hour Pharmacy', 'CT Scan',
                        'Pharmacy','MRI Scan'],
    'hosp_timings':'24 Hours',
    'doc_list':[{'hosp_id':'HD12','doc_id':'D073','doc_name':'Dr. Raghu M','doc_qualification':'MBBS, MD, DM','doc_specialization': 'Cardiology','doc_experience':'8 years','doc_fee':'400 /-'},
                {'hosp_id':'HD12','doc_id':'D074','doc_name':'Dr. Dhanraj ','doc_qualification':' MCh - Urology, MBBS','doc_specialization': 'Urologist','doc_experience':'10 years','doc_fee':'800 /-'},
                {'hosp_id':'HD12','doc_id':'D075','doc_name':'Dr. Sunitha','doc_qualification':'MBBS, MS - ENT','doc_specialization': ' ENT','doc_experience':'17 years','doc_fee':'900 /-'},
                {'hosp_id':'HD12','doc_id':'D076','doc_name':'Dr. Akshara Mohima ','doc_qualification':'MBBS, DNB OBG','doc_specialization': 'Gynecologist','doc_experience':'11 years','doc_fee':'300 /-'},
                {'hosp_id':'HD12','doc_id':'D077','doc_name':'Dr. Krishna Reddy','doc_qualification':'M.d(dentist), M.B.B.S', 'doc_specialization':'Dentist','doc_experience':'22 years','doc_fee':'400 /-'},
                {'hosp_id':'HD12','doc_id':'D078','doc_name':'Dr. Akhilasri','doc_qualification':'MD (Pediatrics), FPCCI','doc_specialization': 'Pediatrics','doc_experience':'9 years','doc_fee':'800 /-'},
                {'hosp_id':'HD12','doc_id':'D079','doc_name':'Dr. Gopal Varma','doc_qualification':'MBBS, D.Ortho, DNB Ortho', 'doc_specialization':'Orthopedics','doc_experience':'15 years','doc_fee':'800 /-'}
                ]
}
hosp_details.insert_one(hosp_data)
print("inserted")
client.close()

import pymongo 
from pymongo import MongoClient
from mongoengine import *
#from model import Post

#using pymongo
client = MongoClient()
db = client['hospitals'] 
hosp_details = db.hospital_details
hosp_data = {
    'hosp_id':'HD12',
    'hosp_name':'GMR Varalakshmi Care Hospital',
    'hosp_email':'gmr varalakshmicare@gmail.com',
    'hosp_address':'Hospital Rd, GMR Nagar, Near Andhra Bank GMR Nagar, Srikakulam District',
    'hosp_website':'http://gmrcarehospitals.in/home.html',
    'hosp_specs':['Cardiology','Urology',' ENT','Gynecology','Dentist','Pediatrics','Orthopedics'],
    'hosp_mobile':['+91 997007358','9989189882'],
    'hosp_facility':['ENMG',
                        '24 Hour Pharmacy', 'CT Scan',
                        'Pharmacy','MRI Scan'],
    'hosp_timings':'24 Hours',
    'doc_list':[{'hosp_id':'HD12','doc_id':'D080','doc_name':'Dr. Raghava','doc_qualification':'MBBS, MD, DM','doc_specialization': 'Cardiology','doc_experience':'8 years','doc_fee':'400 /-'},
                {'hosp_id':'HD12','doc_id':'D081','doc_name':'Dr. Dhanujay ','doc_qualification':' MCh - Urology, MBBS','doc_specialization': 'Urologist','doc_experience':'12 years','doc_fee':'800 /-'},
                {'hosp_id':'HD12','doc_id':'D082','doc_name':'Dr. Susmitha','doc_qualification':'MBBS, MS - ENT','doc_specialization': ' ENT','doc_experience':'7 years','doc_fee':'400 /-'},
                {'hosp_id':'HD12','doc_id':'D083','doc_name':'Dr. Akanksha ','doc_qualification':'MBBS, DNB OBG','doc_specialization': 'Gynecologist','doc_experience':'10 years','doc_fee':'300 /-'},
                {'hosp_id':'HD12','doc_id':'D084','doc_name':'Dr. Krishna Murali','doc_qualification':'M.d(dentist), M.B.B.S', 'doc_specialization':'Dentist','doc_experience':'22 years','doc_fee':'400 /-'},
                {'hosp_id':'HD12','doc_id':'D085','doc_name':'Dr. Anuhya','doc_qualification':'MD (Pediatrics), FPCCI','doc_specialization': 'Pediatrics','doc_experience':'4 years','doc_fee':'300 /-'},
                {'hosp_id':'HD12','doc_id':'D086','doc_name':'Dr. Vijaya K','doc_qualification':'MBBS, D.Ortho, DNB Ortho', 'doc_specialization':'Orthopedics','doc_experience':'15 years','doc_fee':'800 /-'}
                ]
}
hosp_details.insert_one(hosp_data)
print("inserted")
client.close()
"""