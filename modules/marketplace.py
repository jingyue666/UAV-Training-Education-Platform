import streamlit as st
from datetime import datetime
import geopy

def order_center():
    """接单大厅"""
    st.title("🎯 任务大厅")
    
    # 筛选条件
    col1, col2, col3 = st.columns(3)
    with col1:
        location = st.text_input("地点", placeholder="输入城市或区域")
    with col2:
        min_price, max_price = st.slider("预算范围", 0, 10000, (500, 5000))
    with col3:
        skill_level = st.multiselect(
            "所需技能",
            ["初级", "中级", "高级", "农业植保", "航拍", "巡检"]
        )
    
    # 订单列表
    orders = get_available_orders(location, min_price, max_price, skill_level)
    
    for order in orders:
        with st.container():
            st.markdown(f"### {order['title']}")
            col1, col2, col3 = st.columns([2,1,1])
            with col1:
                st.write(f"📅 {order['date']}")
                st.write(f"📍 {order['location']}")
                st.write(f"💰 ¥{order['price']}")
            with col2:
                st.metric("难度", order['difficulty'])
            with col3:
                if st.button("抢单", key=order['id']):
                    grab_order(order['id'])

def order_management():
    """订单管理"""
    st.title("📋 我的订单")
    
    tabs = st.tabs(["进行中", "待验收", "已完成", "已取消"])
    
    with tabs[0]:
        active_orders = get_active_orders()
        for order in active_orders:
            with st.container():
                st.write(f"**{order['title']}**")
                progress = st.progress(order['progress'])
                if st.button("上传进度", key=f"upload_{order['id']}"):
                    upload_progress(order['id'])

def realtime_monitoring():
    """实时监控"""
    st.title("📡 实时监控中心")
    
    # 地图显示
    import folium
    from streamlit_folium import st_folium
    
    # 创建地图
    m = folium.Map(location=[29.56, 106.55], zoom_start=12)  # 重庆坐标
    
    # 添加设备位置
    devices = get_active_devices()
    for device in devices:
        folium.Marker(
            [device['lat'], device['lng']],
            popup=f"设备{device['id']}",
            tooltip=device['status']
        ).add_to(m)
    
    # 显示地图
    st_folium(m, width=700, height=500)
    
    # 视频监控
    st.subheader("实时视频")
    video_url = get_live_video_url()
    if video_url:
        st.video(video_url)
    
    # 一键应急
    if st.button("🚨 紧急求助", type="primary"):
        trigger_emergency()
