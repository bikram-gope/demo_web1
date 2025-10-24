from operator import concat

import streamlit as st

name = st.text_input("Enter your Name:")
fname = st.text_input("Enter your father Name :")
mname = st.text_input("Enter your mather's Name :")
Gender = st.text_input("Enter your Gender :")
dateofbirth = st.text_input("Enter your Date of Birth :")
university = st.text_input("Enter your University/Collage Name :")
department = st.text_input("Enter your Department Name :")

adr = st.text_area("Enter your Text :")
Contactnumbder = st.text_input("Enter Your contact Number :")
Emailid = st.text_input("Enter your Email Id :")
fcontactnunber = st.text_input("Enter your Father's contact Number :")
femailid = st.text_input("Enter your father's email Id :")
classdata = st.selectbox("Enter your class :",[0,1,2,3,4,5,6,7,8,9,10,11,12])
#bf = st.text_input("Enter your bf Name:")

button = st.button("Done")
if button :
               st.markdown(f"""
Name : {name}
Father Name : {fname}
Mather's Name : {mname}
Gender : {gender}
Date of Birth : {dateofbirth}
university Name : {university}
Department Name : {department}
Address : {adr}
Contact Number : {concat}
Emailid : {email}
fcontact number :{fcontactnunber}
femailid :{femailid}
class : {classdata}
Boyfriend Name : {bf}""")
