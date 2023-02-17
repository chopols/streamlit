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

 -------------------------------------------------------------------------------------
### 1. 요구사항 ###

**\#** **FY22 B2B Integration (**3/17일 이메일 기준)

1)  **Commerce API Connectivity (Api 연결)**\
    Below is the link to request for token generation and registration
    process details.\
    (<https://forums.cisco.com/OperationsExchange/s/article/Commerce-API-Connectivity>)

2)  **CCW Catalog - POE**\
    Please request for API Access for Catalog, you can find all details
    in provided IG document, kindly go through.\
    (<https://apiconsole.cisco.com/docs/read/external_apis/CCW_Catalog__POE>)

3)  **Sharing once again Implement Guidance(IG**):\
    (<https://forums.cisco.com/OperationsExchange/s/article/B2B-Integration-Guides-Catalog>)

**2. 진행사항**

1)  **Commerce API Connectivity**

-   **API 응용 프로그램 등록 및 액세스 토큰(Token) 발급 완료**

![텍스트이(가) 표시된 사진 자동 생성된
설명](media/image1.png){width="4.322222222222222in"height="3.770138888888889in"}\
\<API 등록 및 Key 발급 화면\>

-   **Generate Token for Cisco Commerce API\'s -- 테스트 완료**

![](media/image2.png){width="5.259722222222222in"height="3.282638888888889in"}

\<Postman을 통한 access_token 발급 확인\>

-   **Cisco Hello API -- 테스트 완료**

![](media/image3.png){width="5.363888888888889in"height="3.020138888888889in"}\
\<Postman을 통한 결과 확인\>

2)  **CCW Catalog -- POE (Cisco Commerce Catalog Web Service 문서) 확인 중**

> \- 연계 및 테스트에 필요한 사항 확인 중\
> ![테이블이(가) 표시된 사진 자동 생성된
> 설명](media/image4.png){width="5.25in" height="2.4895833333333335in"}
>
> \- 아래 2.4 Service Posman을 통한 연계 테스트 시도 - 실패\
> (실패 사유 : 연계에 필요한 정보 및 접근 권한 없음,)
>
> \- 연계 [테스트 환경 구축 후 추가적인 테스트 진행 가능]{.underline}
>
> [\
> ]{.underline}![텍스트이(가) 표시된 사진 자동 생성된
> 설명](media/image5.png){width="5.888221784776903in"> height="4.186860236220473in"}

\<Postman을 통해 테스트한 결과 "Not Authorized"\>

**3. 요청 및 확인 사항 (피드백 필요)**

1)  **CCW Catalog -- POE 접근 권한 필요**

![텍스트이(가) 표시된 사진 자동 생성된
설명](media/image6.png){width="6.145833333333333in"height="2.9458333333333333in"}

2)  **연계에 필요한 ID 제공**

> (기타 : 아래 항목 외 연계에 필요한 추가적인 정보가 있는지 확인 및> 제공)
>
> ![텍스트이(가) 표시된 사진 자동 생성된
> 설명](media/image7.png){width="5.452083333333333in"> height="3.79375in"}

3)  **CCW Catalog -- POE 개발 관련 문의**

> Catalog 서비스의 각 Api(Requet, Response) 결과를 아래의 샘플과 같이
> 포맷에 맞게 "파일을 생성"하면 되는 것인지 아니면 다른 방법으로
> 처리해야 하는지 [연계 프로세스를 간략하나마 제공]{.underline} 받았으면
> 좋겠습니다.
>
> ![텍스트이(가) 표시된 사진 자동 생성된
> 설명](media/image8.png){width="4.680555555555555in"> height="3.4472222222222224in"}

\<Cisco Commerce Catalog Web Service 발췌\>

이상 끝.

'''