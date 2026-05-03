import streamlit as st
import pandas as pd
import plotly.express as px

def student_learning_center():
    """学员学习中心"""
    st.title("📚 学习中心")
    
    # 课程分类
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("初级课程", use_container_width=True):
            show_courses("初级")
    with col2:
        if st.button("中级课程", use_container_width=True):
            show_courses("中级")
    with col3:
        if st.button("高级课程", use_container_width=True):
            show_courses("高级")
    
    # 专项课程
    st.subheader("专项课程")
    specialties = ["农业植保", "城市治理", "应急救援", "电力巡检"]
    for spec in specialties:
        with st.expander(f"🎯 {spec}"):
            show_specialty_courses(spec)
    
    # 学习进度
    st.subheader("学习进度")
    progress_data = get_learning_progress()
    fig = px.bar(progress_data, x="课程", y="进度", color="状态")
    st.plotly_chart(fig)

def show_courses(level):
    """显示对应等级课程"""
    courses = get_courses_by_level(level)
    for course in courses:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {course['name']}")
                st.progress(course['progress']/100)
                st.caption(f"进度: {course['progress']}%")
            with col2:
                if st.button("进入学习", key=course['id']):
                    open_course_player(course['id'])

def flight_simulator():
    """飞行模拟器"""
    st.title("🕹️ 无人机飞行模拟器")
    
    # 模拟器选择
    sim_type = st.selectbox(
        "选择模拟场景",
        ["重庆山地飞行", "城市楼宇巡检", "农田植保作业", "电力线路巡视"]
    )
    
    # 嵌入模拟器
    if sim_type == "重庆山地飞行":
        st.components.v1.html("""
        <iframe src="simulator.html" width="100%" height="600"></iframe>
        """, height=600)
    
    # 操作说明
    with st.expander("操作指南"):
        st.write("1. 使用键盘WASD控制方向")
        st.write("2. 鼠标控制视角")
        st.write("3. 空格键起飞/降落")

def online_exam():
    """在线考核系统"""
    st.title("📝 在线考核")
    
    # 题库选择
    exam_type = st.selectbox(
        "选择考试类型",
        ["理论考试", "模拟飞行考核", "实操视频考核"]
    )
    
    if exam_type == "理论考试":
        show_theory_exam()
    elif exam_type == "实操视频考核":
        st.info("请上传飞行操作视频")
        video_file = st.file_uploader("选择视频文件", type=['mp4', 'mov'])
        if video_file:
            st.video(video_file)
            if st.button("提交考核"):
                grade_video_submission(video_file)
