def student_channel():
    """高校学生通道"""
    st.title("🎓 高校学生专用通道")
    
    # 学生认证
    if not st.session_state.get("student_verified"):
        st.info("请先进行学生认证")
        
        col1, col2 = st.columns(2)
        with col1:
            student_id = st.text_input("学号")
            university = st.text_input("学校")
        with col2:
            id_card_front = st.file_uploader("学生证正面", type=['jpg', 'png'])
            if id_card_front:
                st.image(id_card_front, caption="学生证正面")
        
        if st.button("提交认证"):
            verify_student(student_id, university, id_card_front)
    else:
        # 学生专享功能
        st.success("✅ 学生认证已通过")
        
        tabs = st.tabs(["实习订单", "课程折扣", "比赛活动", "就业推荐"])
        
        with tabs[0]:
            # 实习订单（仅对学生开放）
            intern_orders = get_intern_orders()
            for order in intern_orders:
                with st.container():
                    st.write(f"**{order['title']}**")
                    st.write(f"📍 {order['location']} | 🎓 实习证明 | 💰 {order['reward']}")
                    if st.button("申请实习", key=order['id']):
                        apply_internship(order['id'])

def veteran_channel():
    """退役军人/失业人员通道"""
    st.title("🪖 退役军人/失业人员支持通道")
    
    # 身份选择
    identity = st.radio("您的身份", ["退役军人", "失业人员"])
    
    # 支持政策
    st.subheader("支持政策")
    if identity == "退役军人":
        st.write("""
        - 学费减免50%
        - 优先安排实习岗位
        - 就业推荐优先
        - 创业基金支持
        """)
        
        if st.button("申请退役军人福利"):
            apply_veteran_benefits()
    
    elif identity == "失业人员":
        st.write("""
        - 政府补贴培训
        - 免费基础课程
        - 就业指导服务
        - 灵活就业支持
        """)
