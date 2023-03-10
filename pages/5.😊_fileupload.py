import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(
    page_icon='๐',
    page_title='์คํธ๋ฆผ๋ฆฟ ๋ฐฐํฌํ๊ธฐ',
    layout='wide',
)

st.subheader('ํ์ผ ์๋ก๋')

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

'''

[1. Headers ํค๋](#1-headersํค๋)  
[2. Horizontal Rules ์ํ์ ](#2-Horizontal-์ํ์ )  
[3. Emphasis ๊ฐ์กฐ](#3-Emphasis-๊ฐ์กฐ)  
[4. Blockquotes ์ธ์ฉ](#4-blockquotes-์ธ์ฉ)  
[5. Lists ๋ชฉ๋ก](#5-Lists-๋ชฉ๋ก)  
[6. Backslash Escapes](#6-Backslash-Escapes)  
[7. ์ฝ๋๋ธ๋ญ](#7-์ฝ๋๋ธ๋ญ)  
[8. ํ๋ง๋ค๊ธฐ](#8-ํ๋ง๋ค๊ธฐ)  
[9. ์ด๋ฏธ์ง](#9-์ด๋ฏธ์ง)  
[10. Links (Anchor) ๋งํฌ](#10-Links-(Anchor)-๋งํฌ)  
[11. ์ฒดํฌ๋ฆฌ์คํธ](#11-์ฒดํฌ๋ฆฌ์คํธ)  

# 1. Headersํค๋ 
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6   
test  


# 2. Horizontal ์ํ์ 
* * *
***
*****
- - -
-------------------   
test...  

# 3. Emphasis ๊ฐ์กฐ 
_This will also be italic_  
**This will also be bold**  
~~This is canceled~~  
_You **can** ~~combine~~ them_  

์ดํ๋ฆญ์ฒด๋ *(asterisks)* ํน์ _(underscore)_๋ฅผ ์ฌ์ฉํ์ธ์.    
๋๊ป๊ฒ๋ **(asterisks)** ํน์ __(underscore)__๋ฅผ ์ฌ์ฉํ์ธ์.   
*_์ดํ๋ฆญ์ฒด์ ๋๊ป๊ฒ*_๋ฅผ ๊ฐ์ด ์ฌ์ฉํ  ์ ์์ต๋๋ค.   
์ทจ์์ ์ ~~tilde~~๋ฅผ ์ฌ์ฉํ์ธ์.   
<u>๋ฐ์ค์</u>๋ฅผ ์ฌ์ฉํ์ธ์.  

# 4. Blockquotes ์ธ์ฉ  
> ๋ธ๋ญ์ฟผํฐ> >๋ธ๋ญ์ฟผํฐ

 - ํ์คํธ ์๋๋ค.
 - ํ์คํธ ์๋๋ค.
 - ํ์คํธ ์๋๋ค.

์ธ์ฉ๋ฌธ(blockQuote)

> ๋จ์ ๋ง์ด๋ ๊ธ์์ ์ง์  ๋๋ ๊ฐ์ ์ผ๋ก ๋ฐ์จ ๋ฌธ์ฅ.   
> _(๋ค์ด๋ฒ ๊ตญ์ด ์ฌ์ )_

BREAK!

> ์ธ์ฉ๋ฌธ์ ์์ฑํ์ธ์!
>> ์ค์ฒฉ๋ ์ธ์ฉ๋ฌธ(nested blockquote)์ ๋ง๋ค ์ ์์ต๋๋ค.
>>> ์ค์ค์ฒฉ๋ ์ธ์ฉ๋ฌธ 1   
>>> ์ค์ค์ฒฉ๋ ์ธ์ฉ๋ฌธ 2   
>>> ์ค์ค์ฒฉ๋ ์ธ์ฉ๋ฌธ 3   

> # this is h1!  
> * list  
> `textbox`  


# 5. Lists ๋ชฉ๋ก

1. ์์๊ฐ ํ์ํ ๋ชฉ๋ก
1. ์์๊ฐ ํ์ํ ๋ชฉ๋ก
    - ์์๊ฐ ํ์ํ์ง ์์ ๋ชฉ๋ก(์๋ธ) 
    - ์์๊ฐ ํ์ํ์ง ์์ ๋ชฉ๋ก(์๋ธ) 
1. ์์๊ฐ ํ์ํ ๋ชฉ๋ก
    1. ์์๊ฐ ํ์ํ ๋ชฉ๋ก(์๋ธ)
    1. ์์๊ฐ ํ์ํ ๋ชฉ๋ก(์๋ธ)
1. ์์๊ฐ ํ์ํ ๋ชฉ๋ก

- ์์๊ฐ ํ์ํ์ง ์์ ๋ชฉ๋ก์ ์ฌ์ฉ ๊ฐ๋ฅํ ๊ธฐํธ
  - ๋์ฌ(hyphen)
  * ๋ณํ(asterisks)
  + ๋ํ๊ธฐ(plus sign)


# 6. Backslash Escapes
*ํน์๋ฌธ์ ์ถ๋ ฅ์๋จ   
-ํน์๋ฌธ์ ์ถ๋ ฅ์๋จ  
\* ํน์๋ฌธ์ ์ถ๋ ฅ  
\- ํน์๋ฌธ์ ์ถ๋ ฅ  

# 7. ์ฝ๋ ๋ธ๋ญ
```java
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("Hello, Honeymon");
  }
}
```


# 8. ํ๋ง๋ค๊ธฐ

| ๊ฐ | ์๋ฏธ | ๊ธฐ๋ณธ๊ฐ |
|---|:---:|---:|
| `static` | ์ ํ(๊ธฐ์ค) ์์ / ๋ฐฐ์น ๋ถ๊ฐ๋ฅ | `static` |
| `relative` | ์์ ์์ ์ ๊ธฐ์ค์ผ๋ก ๋ฐฐ์น |  |
| `absolute` | ์์น ์ ๋ถ๋ชจ(์กฐ์)์์๋ฅผ ๊ธฐ์ค์ผ๋ก ๋ฐฐ์น |  |
| `fixed` | ๋ธ๋ผ์ฐ์  ์ฐฝ์ ๊ธฐ์ค์ผ๋ก ๋ฐฐ์น |  |

ํ์ด๋ธ ์ ๋ ฌ

ํค๋1|ํค๋2|ํค๋3
:---|:---:|---:
Left|Center|Right
1|2|3
4|5|6
7|8|9

# 10. Links (Anchor) ๋งํฌ 
[Google](https://developers.google.com/)

- ์ธ๋ถ๋งํฌ : <http://google.com>
- [๊ตฌ๊ธ์ฌ์ดํธ](http://google.com)
- ์ด๋ฉ์ผ๋งํฌ : <chopols@naver.com>

# 11. ์ฒดํฌ๋ฆฌ์คํธ
- [x] this is a complete item
- [ ] this is an incomplete item
- [x] @mentions, #refs, [links](), **formatting**, and ~~tags~~ supported

# 9. ์ด๋ฏธ์ง 
![Baby](http://nas.ibzsoft.com/baby.png "์ธ์ ํ์ดํ")  
'''

# [![Baby](http://nas.ibzsoft.com/baby.png "์ธ์ ํ์ดํ")](http://nas.ibzsoft.com/baby.png)
# <img src="http://nas.ibzsoft.com/baby.png" width="250px" height="100px" title="px(ํฝ์) ํฌ๊ธฐ ์ค์ " alt="Baby"></img><br/>

con5,con6,empty2 = st.columns([0.5,0.5,0.3])
with con5:
  video_file = open('d:/temp/ina.mp4', 'rb').read()
  st.video(video_file)