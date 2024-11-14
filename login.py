import streamlit as st
import pandas as pd
import time

st.title("삼국시대 VR 체험하기")
st.image('image.jpg')
data = pd.read_csv("members.csv")
data["반"] = data["반"].astype(str)


with st.form("login_form"):   
    G5class = st.text_input("5학년 ()반",
                    placeholder = "자신의 반을 입력하세요.")

    SName = st.text_input("이름",
                    placeholder = "이름을 입력하세요.")
    submit_button = st.form_submit_button("로그인")


if submit_button:
    if not G5class or not SName:
        st.warning("반과 이름 모두 입력해주세요.")
    else:
        # 사용자 확인
        user = data[(data["반"] == G5class) & (data["이름"] == SName)]
        
        if not user.empty:
            st.success(f"{SName}님 환영합니다!")
            st.session_state["이름"]=SName
            
            progress_text = "로그인 중입니다."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()
            st.switch_page("pages\Khistory.py")
            
            
        else:
            st.error("아이디 또는 비밀번호가 일치하지 않습니다.")