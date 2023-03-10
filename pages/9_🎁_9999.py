import streamlit as st
import pandas as pd
import urllib.parse
from common.clsdb_mssql import dbconn
from PIL import Image

st.set_page_config(
    page_icon='π',
    page_title='μνμ λ³΄',
    layout='wide',
)

st.subheader('> μνμ λ³΄')

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
    value=50 # κΈ°λ³Έκ°, μ λ€λ‘ 2κ° μ€μ  /  νλλ§ νλ κ²½μ° value=2.5 μ΄λ° μμΌλ‘ μ€μ κ°λ₯
    # (2.5, 7.5) # κΈ°λ³Έκ°, μ λ€λ‘ 2κ° μ€μ  /  νλλ§ νλ κ²½μ° value=2.5 μ΄λ° μμΌλ‘ μ€μ κ°λ₯
)
select_cost = st.sidebar.slider(
    "νλ§€κ°",
    1000, 300000, (0, 10000)
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
            where a.νλ§€μ¬λΆ = '{select_yn}' 
            and b.λ§€μ²΄κ΅¬λΆ = '{select_gubun.split(':')[0]}' 
            and a.μνλͺ like '%{select_name}%'
            and b.νλ§€κ° between {select_cost[0]} and {select_cost[1]}
            and a.μνμ΄λ―Έμ§ is not null 
            order by 5
        
        '''
        result = conn.selectquery(str_sql)
        conn.close()
        if len(result) > 0:
            df = pd.DataFrame(result, columns = ['code','name','info','gubun','cost','lastdate','image'])
            df['name'] = df['name'].str.encode('ISO-8859-1').str.decode('cp949')
            df['info'] = df['info'].str.encode('ISO-8859-1').str.decode('cp949')
            df['image'] = df['image'].str.encode('ISO-8859-1').str.decode('cp949')
            df['cost1'] = df['cost'].map('{:,.0f}'.format)
            df['lastdate1'] = df['lastdate'].map('{:%Y-%m-%d}'.format) 

            # Define the number of columns per page
            cols_per_page = 4
            col_width = 600
            col_height = 600
            # Calculate the number of pages needed
            num_pages = len(df) // cols_per_page + (len(df) % cols_per_page > 0)
            # Define the base URL for the images
            base_url = 'http://nas.worldms.net/image/'

            costwith = f'{"{:,}".format(select_cost[0])}μ ~ {"{:,}".format(select_cost[1])}μ'
            st.markdown(f'### κ°κ²©λ : {costwith}')
            # Loop through each page and display the products
            for page in range(num_pages):
                start_idx = page * cols_per_page
                end_idx = min(start_idx + cols_per_page, len(df))
                page_products = df.iloc[start_idx:end_idx]
                
                # Use st.columns to create the columns for the current page
                cols = st.columns(cols_per_page)
                # cols.set_min_width(col_width)
                # cols.set_min_height(col_height)
                for i, col in enumerate(cols):
                    if i < len(page_products):
                        if 'http://' in page_products.iloc[i]['image']:
                            image_url = urllib.parse.quote(page_products.iloc[i]['image'], safe='')
                        else:
                            image_url = base_url + urllib.parse.quote(page_products.iloc[i]['image'], safe='')
                        image = Image.open(urllib.request.urlopen(image_url))
                        new_image = image.resize((200, 250))
                        # col.image(new_image, caption=page_products.iloc[i]['name'])
                        col.image(new_image)
                        col.write(page_products.iloc[i]['name'])
                        col.write('νλ§€κ° : '+page_products.iloc[i]['cost1']+'μ')
                        col.write(page_products.iloc[i]['info'])
            
    except Exception as e:
        # print(f'sql Error : Unknown Exception {str(e)}')
        # e = RuntimeError(str(e))
        st.exception(str(e))

