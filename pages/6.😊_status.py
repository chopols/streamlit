import streamlit as st
import time

st.set_page_config(
    page_icon='😊',
    page_title='스트림릿 배포하기',
    layout='wide',
)

st.subheader('Status elements')

st.markdown('### st.process')
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)

st.markdown('### st.spinner')
with st.spinner('Wait for it...'):
    time.sleep(2)
st.success('Done!')

st.markdown('### st.balloons')
st.balloons()

st.markdown('### st.snow')
st.snow()

with st.echo():
    st.markdown('### st.error')
    st.error('This is an error', icon="🚨")

    st.markdown('### st.warning')
    st.warning('This is a warning', icon="⚠️")

    st.markdown('### st.info')
    st.info('This is a purely informational message', icon="ℹ️")

    st.markdown('### st.success')
    st.success('This is a success message!', icon="✅")

    st.markdown('### st.exception')
    e = RuntimeError('This is an exception of type RuntimeError')
    st.exception(e)

    

