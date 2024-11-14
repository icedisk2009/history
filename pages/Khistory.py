import streamlit as st
import requests
from bs4 import BeautifulSoup


    
museums = {
    "고구려": "https://baekjemuseum.seoul.go.kr/vr_file/2016/04/index.html",
    "백제": "https://premium.360vrmuseum.com/?m=iiubeU6mgfx&play=0&qs=0&hr=1",
    "신라": "https://gyeongju.museum.go.kr/kor/html/sub02/0203.html?mode=L&GotoPage=1"
}

st.title("삼국시대 박물관 VR 체험")

st.write("고구려, 백제, 신라 박물관을 생생하게 체험해보세요")

selected_museum = st.selectbox("박물관을 선택하세요", list(museums.keys()))

url = museums[selected_museum]

# HTML 링크를 생성하고 unsafe_allow_html=True를 사용하여 렌더링
st.markdown(f'자세한 정보는 <a href="{url}" target="_blank">여기</a>에서 확인하세요.', unsafe_allow_html=True)

# VR 체험 버튼 추가
if st.button("VR 체험 시작"):
    st.write(f"{selected_museum} 박물관 VR 체험을 시작합니다.")
    st.components.v1.iframe(url, width=800, height=600, scrolling=True)