def contribution_system():
    """贡献值系统"""
    st.title("🏆 贡献值与激励体系")
    
    # 用户贡献值总览
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("总贡献值", "1,250", "+120")
    with col2:
        st.metric("当前等级", "中级接单员", "↑")
    with col3:
        st.metric("排名", "第15名", "↑3")
    with col4:
        st.metric("可兑换", "2,500元", "查看")
    
    # 贡献值明细
    st.subheader("贡献值记录")
    points_data = get_points_history()
    df = pd.DataFrame(points_data)
    st.dataframe(df, use_container_width=True)
    
    # 贡献值获取规则
    with st.expander("贡献值计算规则"):
        st.write("""
        - 完成订单：基础金额×难度系数
        - 客户好评：+50贡献值/次
        - 推荐新用户：+100贡献值/人
        - 参与公益活动：+200贡献值/次
        - 成为讲师：+500贡献值
        """)
    
    # 兑换商城
    st.subheader("🎁 兑换商城")
    rewards = get_available_rewards()
    for reward in rewards:
        col1, col2 = st.columns([3,1])
        with col1:
            st.write(f"**{reward['name']}**")
            st.write(reward['description'])
        with col2:
            if st.button(f"兑换 {reward['points']}积分", 
                        disabled=reward['points'] > current_points):
                process_reward_exchange(reward['id'])
