import streamlit as st
from modules import auth, dashboard, training, marketplace, admin
import session_state

def main():
    # 页面配置
    st.set_page_config(
        page_title="无人机教培接单平台",
        page_icon="🚁",
        layout="wide"
    )
    
    # 初始化session state
    session_state.init()
    
    # 侧边栏导航
    with st.sidebar:
        st.image("logo.png", width=150)
        st.title("导航菜单")
        
        if not st.session_state.get("authenticated"):
            auth.show_login()
        else:
            user_role = st.session_state.get("role")
            
            menu_options = {
                "学员": ["学习中心", "模拟训练", "接单大厅", "个人中心"],
                "接单员": ["任务大厅", "我的订单", "技能提升", "收益中心"],
                "企业用户": ["发布需求", "人才库", "项目管理", "企业中心"],
                "管理员": ["用户管理", "订单监控", "内容管理", "数据分析"]
            }
            
            selected = st.selectbox(
                "选择功能模块",
                menu_options.get(user_role, [])
            )
            
            if st.button("退出登录"):
                auth.logout()
    
    # 主内容区路由
    if st.session_state.get("authenticated"):
        route_content(selected, user_role)
    else:
        show_landing_page()

def route_content(selected, role):
    """路由到对应模块"""
    if role == "学员":
        if selected == "学习中心":
            training.student_learning_center()
        elif selected == "模拟训练":
            training.flight_simulator()
    elif role == "管理员":
        if selected == "用户管理":
            admin.user_management()
        elif selected == "数据分析":
            admin.data_analytics()

if __name__ == "__main__":
    main()
