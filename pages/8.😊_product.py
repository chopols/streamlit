import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
# from streamlit_javascript import st_javascript
from common.clsdb_mssql import dbconn

st.set_page_config(
    page_icon='😊',
    page_title='스트림릿 배포하기',
    layout='wide',
)

st.subheader('상품정보')

st.sidebar.title('조건 검색 🌸')
select_name = st.sidebar.text_input('상품명을 입력하세요.')
select_gubun = st.sidebar.selectbox('매체를 선택하세요.',['1:국민','7:롯데'])
select_yn =st.sidebar.radio(
    "상품판매여부를 선택하세요.",
    ['Y', 'N'],
    horizontal=True
    )
select_row = st.sidebar.slider(
    "조회갯수",
     0, #시작 값 
     100, #끝 값  
    value=10 # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정가능
    # (2.5, 7.5) # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정가능
)
start_button = st.sidebar.button(
    "조회하기 ✌ "#"버튼에 표시될 내용"
)    

if start_button:
    try:
        conn = dbconn()
        str_sql = f'''
            select top {select_row}  a.상품코드, a.상품명, a.상품설명, b.매체구분, b.판매가, b.등록일자, a.상품이미지 
            from 상품정보 a inner join 매체상품정보 b on a.상품코드 = b.상품코드
            where a.판매여부 = '{select_yn}' and b.매체구분 = '{select_gubun.split(':')[0]}' and a.상품명 like '%{select_name}%'
        '''
        result = conn.selectquery(str_sql)
        conn.close()
        df = pd.DataFrame(result, columns = ['code','name','info','gubun','cost','lastdate','image'])
        df['name'] = df['name'].str.encode('ISO-8859-1').str.decode('cp949')
        df['info'] = df['info'].str.encode('ISO-8859-1').str.decode('cp949')
        df['image'] = df['image'].str.encode('ISO-8859-1').str.decode('cp949')
        df['cost1'] = df['cost'].map('{:,.0f}'.format)
        df['lastdate1'] = df['lastdate'].map('{:%Y-%m-%d}'.format) 
        # df = df.set_index('code')
        # df.loc[:, 'cost'] = df['cost'].map('{:,.0f}'.format)
        # df.loc[:, 'lastdate'] = df['lastdate'].map('{:%Y-%m-%d}'.format) 
        # df.loc[:, 'lastdate'] =df['lastdate'] .map('{:%Y-%m-%d %H:%M:%S}'.format) 
        # df.loc[:, 'lastdate'] =df['lastdate'].map('{: %Y}'.format)
        # st.table(df[['code','name','info','cost1','lastdate1','image']])
        # st.dataframe(df[['code','name','info','cost1','lastdate1','image']].style.highlight_max(axis=0))
        # st.dataframe(df[['name','info','cost1','lastdate1','image']], 1200, 600)
        AgGrid(df[['code','name','info','cost1','lastdate1','image']])
        # js = st_javascript("""
        #     function(e) {
        #         let api = e.api;     
        #         let sel = api.getSelectedRows();
        #         api.applyTransaction({remove: sel});
        #     };
        #     """)

        # gb_base = GridOptionsBuilder.from_dataframe(df, enableRowGroup=True, editable=True, groupable = True)
        # gb_base.configure_pagination(enabled=True, paginationAutoPageSize = False, paginationPageSize=20)
        # gb_base.configure_selection('multiple', use_checkbox=True)
        # gb_base.configure_grid_options(onRowSelected = js, pre_selected_rows = []) 
        # grid_options_base = gb_base.build()
        # table_base = AgGrid(df[['code','name','info','cost1','lastdate1','image']], gridOptions=grid_options_base, allow_unsafe_jscode=True, fit_columns_on_grid_load=True)        

    except Exception as e:
        # print(f'sql Error : Unknown Exception {str(e)}')
        # e = RuntimeError(str(e))
        st.exception(str(e))

