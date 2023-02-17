import streamlit as st

# 페이지 기본설정
st.set_page_config(
    page_icon='😊',
    page_title='스트림릿 배포하기',
    layout='wide',
)

st.subheader('폼 다루기')

st.write('Inserting elements using "with" notation')
with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write('Inserting elements out of order')
form = st.form("my_form1")
slider_val = form.slider("Form slider")
checkbox_val = form.checkbox("Form checkbox")
submitted = form.form_submit_button("Submit")
if submitted:
    st.write("slider", slider_val, "checkbox", checkbox_val)

st.slider("Outside the form")
