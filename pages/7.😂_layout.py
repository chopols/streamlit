# from tkinter.tix import COLUMN
import pyparsing as ps
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.set_page_config(
    page_icon='😊',
    page_title='스트림릿 배포하기',
    layout='wide',
)

empty1,con1,empty2 = st.columns([0.3,1.0,0.3])
empyt1,con2,con3,empty2 = st.columns([0.3,0.5,0.5,0.3])
empyt1,con4,empty2 = st.columns([0.3,1.0,0.3])
empyt1,con5,con6,empty2 = st.columns([0.3,0.5,0.5,0.3])

with empty1 :
    ps.Empty() # 여백부분1

with con1 :
    '''
    ![Baby](http://nas.ibzsoft.com/baby.png "인아 파이팅")  
    '''

with con2 :
    option = st.selectbox("How would you like to be contacted?",
            ("Email", "Home phone", "Mobile phone"),
            )
    options = st.multiselect(
        'What are your favorite colors',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])

    st.write('You selected:', options)

    st.radio("Set selectbox label visibility 👉",
        key="radio2",
        options=["visible", "hidden", "collapsed"],
    )

with con3 :
    ps.Empty()

with con4 :
    ps.Empty()

with con5 :
    video_file = open('d:/temp/ina.mp4', 'rb').read()
    st.video(video_file)     
with con6 :
        '''
        ## 우리 인아   
        **아직 백일도 안됐는데 우량아 다 됐네**   
        '''

with empty2 :
    ps.Empty() # 여백부분2
