import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
# from streamlit_javascript import st_javascript
from common.clsdb_mssql import dbconn

st.set_page_config(
    page_icon='π',
    page_title='μ€νΈλ¦Όλ¦Ώ λ°°ν¬νκΈ°',
    layout='wide',
)

st.subheader('μνμ λ³΄')

st.sidebar.title('μ‘°κ±΄ κ²μ πΈ')
select_name = st.sidebar.text_input('μνλͺμ μλ ₯νμΈμ.')
select_gubun = st.sidebar.selectbox('λ§€μ²΄λ₯Ό μ ννμΈμ.',['1:κ΅­λ―Ό','7:λ‘―λ°'])
select_yn =st.sidebar.radio(
    "μννλ§€μ¬λΆλ₯Ό μ ννμΈμ.",
    ['Y', 'N'],
    horizontal=True
    )
select_row = st.sidebar.slider(
    "μ‘°νκ°―μ",
     0, #μμ κ° 
     100, #λ κ°  
    value=10 # κΈ°λ³Έκ°, μ λ€λ‘ 2κ° μ€μ  /  νλλ§ νλ κ²½μ° value=2.5 μ΄λ° μμΌλ‘ μ€μ κ°λ₯
    # (2.5, 7.5) # κΈ°λ³Έκ°, μ λ€λ‘ 2κ° μ€μ  /  νλλ§ νλ κ²½μ° value=2.5 μ΄λ° μμΌλ‘ μ€μ κ°λ₯
)
start_button = st.sidebar.button(
    "μ‘°ννκΈ° β "#"λ²νΌμ νμλ  λ΄μ©"
)    

if start_button:
    try:
        conn = dbconn()
        str_sql = f'''
            select top {select_row}  a.μνμ½λ, a.μνλͺ, a.μνμ€λͺ, b.λ§€μ²΄κ΅¬λΆ, b.νλ§€κ°, b.λ±λ‘μΌμ, a.μνμ΄λ―Έμ§ 
            from μνμ λ³΄ a inner join λ§€μ²΄μνμ λ³΄ b on a.μνμ½λ = b.μνμ½λ
            where a.νλ§€μ¬λΆ = '{select_yn}' and b.λ§€μ²΄κ΅¬λΆ = '{select_gubun.split(':')[0]}' and a.μνλͺ like '%{select_name}%'
        '''
        result = conn.selectquery(str_sql)
        conn.close()
        df = pd.DataFrame(result, columns = ['code','name','info','gubun','cost','lastdate','image'])
        df['name'] = df['name'].str.encode('ISO-8859-1').str.decode('cp949')
        df['info'] = df['info'].str.encode('ISO-8859-1').str.decode('cp949')
        df['image'] = df['image'].str.encode('ISO-8859-1').str.decode('cp949')
        df['cost1'] = df['cost'].map('{:,.0f}'.format)
        df['lastdate1'] = df['lastdate'].map('{:%Y-%m-%d}'.format) 
        df = df.set_index('code')
        # df.loc[:, 'cost'] = df['cost'].map('{:,.0f}'.format)
        # df.loc[:, 'lastdate'] = df['lastdate'].map('{:%Y-%m-%d}'.format) 
        # df.loc[:, 'lastdate'] =df['lastdate'] .map('{:%Y-%m-%d %H:%M:%S}'.format) 
        # df.loc[:, 'lastdate'] =df['lastdate'].map('{: %Y}'.format)
        # st.table(df[['code','name','info','cost1','lastdate1','image']])
        # st.dataframe(df[['code','name','info','cost1','lastdate1','image']].style.highlight_max(axis=0))
        st.dataframe(df[['name','info','cost1','lastdate1','image']], 1200, 600)
        # AgGrid(df[['code','name','info','cost1','lastdate1','image']])
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

