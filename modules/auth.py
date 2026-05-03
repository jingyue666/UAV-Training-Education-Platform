import streamlit as st
import sqlite3
from datetime import datetime
import face_recognition_api  # 人脸识别接口

def show_login():
    """登录/注册界面"""
    tab1, tab2, tab3 = st.tabs(["登录", "注册", "人脸识别登录"])
    
    with tab1:
        username = st.text_input("用户名/手机号")
        password = st.text_input("密码", type="password")
        if st.button("登录"):
            authenticate(username, password)
    
    with tab2:
        reg_type = st.radio("注册类型", ["个人学员", "接单员", "企业用户"])
        # 不同角色的注册表单
        if reg_type == "接单员":
            show_pilot_registration()
    
    with tab3:
        st.info("请上传自拍进行人脸识别")
        uploaded_file = st.camera_input("拍照")
        if uploaded_file:
            if face_login(uploaded_file):
                st.success("识别成功")
                st.rerun()

def authenticate(username, password):
    """验证用户凭证"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, username, role, level FROM users 
        WHERE username=? AND password=?
    ''', (username, password))
    user = cursor.fetchone()
    
    if user:
        st.session_state.authenticated = True
        st.session_state.user_id = user[0]
        st.session_state.username = user[1]
        st.session_state.role = user[2]
        st.session_state.level = user[3]
        st.success("登录成功！")
        st.rerun()
    else:
        st.error("用户名或密码错误")
