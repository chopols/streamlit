import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(
    page_icon='😊',
    page_title='스트림릿 배포하기',
    layout='wide',
)

st.subheader('파일 업로드')

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

[1. Headers 헤더](#1-headers헤더)  
[2. Horizontal Rules 수평선](#2-Horizontal-수평선)  
[3. Emphasis 강조](#3-Emphasis-강조)  
[4. Blockquotes 인용](#4-blockquotes-인용)  
[5. Lists 목록](#5-Lists-목록)  
[6. Backslash Escapes](#6-Backslash-Escapes)  
[7. 코드블럭](#7-코드블럭)  
[8. 표만들기](#8-표만들기)  
[9. 이미지](#9-이미지)  
[10. Links (Anchor) 링크](#10-Links-(Anchor)-링크)  
[11. 체크리스트](#11-체크리스트)  

# 1. Headers헤더 
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6   
test  


# 2. Horizontal 수평선
* * *
***
*****
- - -
-------------------   
test...  

# 3. Emphasis 강조 
_This will also be italic_  
**This will also be bold**  
~~This is canceled~~  
_You **can** ~~combine~~ them_  

이텔릭체는 *(asterisks)* 혹은 _(underscore)_를 사용하세요.    
두껍게는 **(asterisks)** 혹은 __(underscore)__를 사용하세요.   
*_이텔릭체와 두껍게*_를 같이 사용할 수 있습니다.   
취소선은 ~~tilde~~를 사용하세요.   
<u>밑줄은</u>를 사용하세요.  

# 4. Blockquotes 인용  
> 블럭쿼터> >블럭쿼터

 - 테스트 입니다.
 - 테스트 입니다.
 - 테스트 입니다.

인용문(blockQuote)

> 남의 말이나 글에서 직접 또는 간접으로 따온 문장.   
> _(네이버 국어 사전)_

BREAK!

> 인용문을 작성하세요!
>> 중첩된 인용문(nested blockquote)을 만들 수 있습니다.
>>> 중중첩된 인용문 1   
>>> 중중첩된 인용문 2   
>>> 중중첩된 인용문 3   

> # this is h1!  
> * list  
> `textbox`  


# 5. Lists 목록

1. 순서가 필요한 목록
1. 순서가 필요한 목록
    - 순서가 필요하지 않은 목록(서브) 
    - 순서가 필요하지 않은 목록(서브) 
1. 순서가 필요한 목록
    1. 순서가 필요한 목록(서브)
    1. 순서가 필요한 목록(서브)
1. 순서가 필요한 목록

- 순서가 필요하지 않은 목록에 사용 가능한 기호
  - 대쉬(hyphen)
  * 별표(asterisks)
  + 더하기(plus sign)


# 6. Backslash Escapes
*특수문자 출력안됨   
-특수문자 출력안됨  
\* 특수문자 출력  
\- 특수문자 출력  

# 7. 코드 블럭
```java
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("Hello, Honeymon");
  }
}
```


# 8. 표만들기

| 값 | 의미 | 기본값 |
|---|:---:|---:|
| `static` | 유형(기준) 없음 / 배치 불가능 | `static` |
| `relative` | 요소 자신을 기준으로 배치 |  |
| `absolute` | 위치 상 부모(조상)요소를 기준으로 배치 |  |
| `fixed` | 브라우저 창을 기준으로 배치 |  |

테이블 정렬

헤더1|헤더2|헤더3
:---|:---:|---:
Left|Center|Right
1|2|3
4|5|6
7|8|9

# 10. Links (Anchor) 링크 
[Google](https://developers.google.com/)

- 외부링크 : <http://google.com>
- [구글사이트](http://google.com)
- 이메일링크 : <chopols@naver.com>

# 11. 체크리스트
- [x] this is a complete item
- [ ] this is an incomplete item
- [x] @mentions, #refs, [links](), **formatting**, and ~~tags~~ supported

# 9. 이미지 
![Baby](http://nas.ibzsoft.com/baby.png "인아 파이팅")  
'''

# [![Baby](http://nas.ibzsoft.com/baby.png "인아 파이팅")](http://nas.ibzsoft.com/baby.png)
# <img src="http://nas.ibzsoft.com/baby.png" width="250px" height="100px" title="px(픽셀) 크기 설정" alt="Baby"></img><br/>

con5,con6,empty2 = st.columns([0.5,0.5,0.3])
with con5:
  video_file = open('d:/temp/ina.mp4', 'rb').read()
  st.video(video_file)