import streamlit as st
import pandas as pd
import numpy as np

from time import time

# 페이지 기본설정
st.set_page_config(
    page_icon='😊',
    page_title='스트림릿 배포하기',
    layout='wide',
)

# 페이지 헤더, 서브헤더 제목 설정
st.header('Streamlit 기능 맛보기.👍')
# st.subheader('chopols 기능 맛보기')

'''
chopols site에 오신걸 환영합니다.

본 사이트는 Streamlit을 이용해서 Webpage를 쉽게 구현합니다.

'''
# 페이지 컬럼 분할(예: 부트스트랩 컬럼, 그리드)
cols = st.columns((1, 1, 2))
cols[0].metric("10/11", "15 °C", "2")
cols[0].metric("10/12", "17 °C", "2 °F")
cols[0].metric("10/13", "15 °C", "2")
cols[1].metric("10/14", "17 °C", "2 °F")
cols[1].metric("10/15", "14 °C", "-3 °F")
cols[1].metric("10/16", "13 °C", "-1 °F")

# 라인 그래프 데이터 생성(with. Pandas)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

# 컬럼 나머지 부분에 라인차트 생성
cols[2].line_chart(chart_data)

st.markdown('Streamlit is **_really_ cool**.')
st.markdown('This text is :red[colored red], and this is **:blue[colored]** and bold.')
st.markdown(':green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:')

'''
Streamlit is **_really_ cool**.

This text is :red[colored red], and this is **:blue[colored]** and bold.

:green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:
'''