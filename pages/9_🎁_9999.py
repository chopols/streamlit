import streamlit as st
import pandas as pd
import urllib.parse
from common.clsdb_mssql import dbconn
from PIL import Image

st.set_page_config(
    page_icon='😊',
    page_title='상품정보',
    layout='wide',
)

st.subheader('> 상품정보')

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
    value=50 # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정가능
    # (2.5, 7.5) # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정가능
)
select_cost = st.sidebar.slider(
    "판매가",
    1000, 300000, (0, 10000)
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
            where a.판매여부 = '{select_yn}' 
            and b.매체구분 = '{select_gubun.split(':')[0]}' 
            and a.상품명 like '%{select_name}%'
            and b.판매가 between {select_cost[0]} and {select_cost[1]}
            and a.상품이미지 is not null 
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

            costwith = f'{"{:,}".format(select_cost[0])}원 ~ {"{:,}".format(select_cost[1])}원'
            st.markdown(f'### 가격대 : {costwith}')
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
                        col.write('판매가 : '+page_products.iloc[i]['cost1']+'원')
                        col.write(page_products.iloc[i]['info'])
            
    except Exception as e:
        # print(f'sql Error : Unknown Exception {str(e)}')
        # e = RuntimeError(str(e))
        st.exception(str(e))

