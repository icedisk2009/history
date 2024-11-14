import streamlit as st
import pandas as pd
import plotly.express as px



@st.cache_data
def load_data():
    df = pd.read_csv("korean_heritage.csv", encoding='utf-8')
    df = df.set_index('구분')
    df = df.drop(['합계'], axis=1)
    df = df.apply(pd.to_numeric, errors='coerce')
    return df

df = load_data()

def page_bar_chart():
    st.title("지역별 문화유산 유형 분포")
    
    regions = df.columns.tolist()
    selected_region = st.selectbox("지역을 선택하세요", regions)
    
    heritage_types = ['국보', '보물', '사적', '명승', '천연기념물', '국가무형유산', '국가민속문화유산']
    
    data = df.loc[heritage_types, selected_region]
    
    fig = px.bar(x=heritage_types, y=data.values, 
                 labels={'x': '문화유산 유형', 'y': '개수'},
                 title=f"{selected_region} 지역의 문화유산 유형별 분포")
    
    st.plotly_chart(fig)

def page_bubble_chart():
    st.title("대한민국 지역별 문화유산 분포")

    # 총 문화유산 개수 계산
    total_heritage = df.sum().reset_index()
    total_heritage.columns = ['region', 'count']

    # 지역 이름과 좌표 매핑
    region_coords = {
        '서울': [37.5665, 126.9780], '부산': [35.1796, 129.0756], '대구': [35.8714, 128.6014],
        '인천': [37.4563, 126.7052], '광주': [35.1601, 126.8514], '대전': [36.3504, 127.3845],
        '울산': [35.5384, 129.3114], '세종': [36.4800, 127.2890], '경기': [37.4138, 127.5183],
        '강원': [37.8228, 128.1555], '충북': [36.6357, 127.4914], '충남': [36.6588, 126.6728],
        '전북': [35.8203, 127.1088], '전남': [34.8161, 126.4629], '경북': [36.4919, 128.8889],
        '경남': [35.4606, 128.2132], '제주': [33.4996, 126.5312]
    }

    # 좌표 추가
    total_heritage['lat'] = total_heritage['region'].map({k: v[0] for k, v in region_coords.items()})
    total_heritage['lon'] = total_heritage['region'].map({k: v[1] for k, v in region_coords.items()})

    fig = px.scatter_mapbox(total_heritage,
                            lat="lat",
                            lon="lon",
                            size="count",
                            color="count",
                            hover_name="region",
                            hover_data=["count"],
                            color_continuous_scale=px.colors.sequential.Viridis,
                            size_max=50,
                            zoom=5,
                            center={"lat": 35.9, "lon": 127.7},
                            mapbox_style="open-street-map")

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    st.plotly_chart(fig)

def main():
    st.sidebar.title("데이터 시각화")
    page = st.sidebar.radio("선택", ["지역별 문화유산 유형 분포", "문화유산 지역 분포"])
    
    if page == "지역별 문화유산 유형 분포":
        page_bar_chart()
    else:
        page_bubble_chart()

if __name__ == "__main__":
    main()