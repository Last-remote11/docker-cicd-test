import streamlit as st
import sys
import os
sys.path.append(os.getcwd())
from streamlit.server.server import Server
import requests

# 서비스 사용자한테는 프로토타입에 있었던 체크포인트, confidence threshold, 결과 해상도 지원 X
# 대신 사이드바에 위법 사진, 위법 내용, 시간을 표시할 예정


@st.cache(
    hash_funcs={
        st.delta_generator.DeltaGenerator: lambda x: None,
        "_regex.Pattern": lambda x: None,
    },
    allow_output_mutation=True,
)
def trigger_rerun():
    """
    mechanism in place to force resets and update widget states
    """
    session_infos = Server.get_current()._session_info_by_id.values() 
    for session_info in session_infos:
        this_session = session_info.session
    # this_session.request_rerun()
    st.experimental_rerun()


def main():

    st.set_page_config(page_title = "PM 위법행위 탐지 시스템", 
    page_icon=":scooter:")
    st.title("PM 위법행위 감지 시스템")
    st.write("영상에서 헬멧 미착용, 승차인원 초과행위를 탐지하는 시스템 입니다.")


    uploaded_file = st.file_uploader("사진을 선택하세요", type=['png', 'jpg'])

    if uploaded_file:
        bytes_data = uploaded_file.getvalue()
        response = requests.post('https://fastapi-ubghdxm5da-du.a.run.app/image', files={'image': bytes_data})
        st.image(response.content, caption='Result')

main()