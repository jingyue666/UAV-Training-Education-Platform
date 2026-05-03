def user_management():
    """用户管理后台"""
    st.title("👥 用户管理")
    
    # 搜索和筛选
    col1, col2, col3 = st.columns(3)
    with col1:
        search = st.text_input("搜索用户")
    with col2:
        role_filter = st.multiselect("角色", ["学员", "接单员", "企业", "讲师"])
    with col3:
        status_filter = st.multiselect("状态", ["正常", "禁用", "待审核"])
    
    # 用户列表
    users = get_users(search, role_filter, status_filter)
    df = pd.DataFrame(users)
    
    # 可编辑的数据表
    edited_df = st.data_editor(
        df,
        column_config={
            "id": st.column_config.NumberColumn("ID", disabled=True),
            "username": "用户名",
            "role": st.column_config.SelectboxColumn(
                "角色",
                options=["学员", "接单员", "企业", "讲师", "管理员"]
            ),
            "status": st.column_config.SelectboxColumn(
                "状态",
                options=["正常", "禁用", "待审核"]
            ),
            "actions": st.column_config.CheckboxColumn("操作")
        },
        use_container_width=True
    )
    
    if st.button("保存更改"):
        update_users(edited_df)
        st.success("用户信息已更新")

def data_analytics():
    """数据分析仪表板"""
    st.title("📊 数据统计与分析")
    
    # 关键指标
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("总用户数", "2,458", "+12%")
    with col2:
        st.metric("月订单量", "324", "+8%")
    with col3:
        st.metric("完成率", "92%", "+2%")
    with col4:
        st.metric("总收入", "¥156,800", "+15%")
    
    # 图表区域
    tab1, tab2, tab3 = st.tabs(["用户增长", "订单分析", "收入分布"])
    
    with tab1:
        # 用户增长趋势
        user_growth = get_user_growth_data()
        fig = px.line(user_growth, x="date", y="count", title="用户增长趋势")
        st.plotly_chart(fig)
    
    with tab2:
        # 订单分布
        order_data = get_order_distribution()
        fig = px.pie(order_data, values="count", names="type", title="订单类型分布")
        st.plotly_chart(fig)
    
    with tab3:
        # 收入结构
        revenue_data = get_revenue_data()
        fig = px.bar(revenue_data, x="source", y="amount", title="收入来源分布")
        st.plotly_chart(fig)
