import datetime
import requests
from io import BytesIO
from PIL import Image
import streamlit as st
from datetime import time

# 페이지 기본설정
st.set_page_config(
    page_icon='😊',
    page_title='스트림릿 배포하기',
    layout='wide',
)

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False


st.subheader('다양한 입력방식(with columns)')
st.markdown('### st.checkbox, st.radio, st.text_input')
col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disabled")
    st.radio(
        "Set text input label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)
st.subheader('다양한 입력방식(without columns)')
with st.echo():    
    fname1 = st.text_input('이름을 입력하세요.')
    st.title(fname1)
    password = st.text_input('비밀번호를 입력하세요.', type='password')
    st.write(password)
    fname2 = st.text_input('이름을 입력하세요.(5자리이하)', max_chars=5)
    st.text(fname2)
    meg = st.text_area('메세지를 입력하세요.')
    st.write(meg)
    meg = st.text_area('메세지를 입력하세요.', height=10)
    st.write(meg)
    number = st.number_input('숫자 입력')
    st.write(number)
    number1 = st.number_input('숫자 입력', 1, 100)
    st.write(number1)
    number2 = st.number_input('숫자 입력', 0.0, 10.0)
    st.write(number2)
    my_date = st.date_input('날짜를 입력하세요.', datetime.date(2023,2,17))
    st.write(my_date)
    my_time = st.time_input('시간을 입력하세요.', datetime.time(14,10))
    st.write(my_time)
    color = st.color_picker('색을 선택하세요.')
    st.write(color)

st.markdown('### st.button')
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

code = '''
import streamlit as st

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(my_large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)
'''
st.code(code,language='python')

st.markdown('### st.download_button')
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

binary_contents = b'example content'
# Defaults to 'application/octet-stream'
st.download_button('Download binary file', binary_contents)

res = requests.get('http://nas.ibzsoft.com/baby.png')  
image = Image.open(BytesIO(res.content))
st.image(image, caption='baby name is Ina', width=400)
code = '''
with open("baby.png", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="baby.png",
            mime="image/png"
          )
'''
st.code(code,language='python')

st.markdown('### st.selectbox')
col1, col2 = st.columns(2)
with col1:
    st.checkbox("Disable selectbox widget", key="check1")
    st.radio(
        "Set selectbox label visibility 👉",
        key="radio1",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.radio1,
        disabled=st.session_state.check1,
    )

st.markdown('### st.multiselect')
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

st.markdown('### st.slider')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values[0])
st.write(type(values))

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

from datetime import datetime
start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

st.markdown('### st.file_uploader')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)    

st.markdown('### st.camera_input')
code = '''
# Examples
import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

# To read the image file buffer as bytes, you can use getvalue() on the UploadedFile object.

import streamlit as st

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
'''
st.code(code,language='python')

