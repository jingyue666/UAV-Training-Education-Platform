import streamlit as st

st.set_page_config(
    page_title="无人机教培商业生态平台",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("🔐 用户登录")
    st.markdown("### 无人机教培商业生态平台")
    st.markdown("**重庆理工大学 · 低空经济创新大赛**")

    username = st.text_input("账号")
    password = st.text_input("密码", type="password")

    if st.button("登 录", type="primary", use_container_width=True):
        if username == "admin" and password == "123456":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("账号或密码错误")

else:
    with st.sidebar:
        st.title("📌 菜单")
        menu = st.radio("", ["🏠 首页", "📚 在线网课", "📦 订单接单", "🛒 设备租赁", "👤 个人中心"])
        st.markdown("---")
        st.markdown("当前身份：实习员")
        st.markdown("贡献值：28")

    if menu == "🏠 首页":
        st.title("🏠 无人机教培商业生态平台")
        st.subheader("培训 → 考证 → 接单 → 就业 → 创业 → 公益")

    elif menu == "📚 在线网课":
        st.title("📚 在线网课")
        tab1, tab2, tab3 = st.tabs(["初级", "中级", "高级"])
        with tab1:
            st.subheader("初级无人机课程")
            st.video("https://www.w3school.com.cn/i/movie.mp4")
        with tab2:
            st.subheader("山地植保课程")
            st.video("https://www.w3school.com.cn/i/movie.mp4")
        with tab3:
            st.subheader("城市巡检课程")
            st.video("https://www.w3school.com.cn/i/movie.mp4")

    elif menu == "📦 订单接单":
        st.title("📦 订单接单中心")
        orders = [
            {"名称":"江津柑橘植保","区域":"重庆江津","金额":2500,"权限":"实习员可接"},
            {"名称":"巫山山地测绘","区域":"重庆巫山","金额":8000,"权限":"初级员可接"}
        ]
        for i, o in enumerate(orders):
            with st.container(border=True):
                a,b,c,d = st.columns(4)
                a.write(o["名称"])
                b.write(o["区域"])
                c.write(f"¥{o['金额']}")
                if d.button("抢单", key=i):
                    st.success(f"抢单成功：{o['名称']}")

    elif menu == "🛒 设备租赁":
        st.title("🛒 设备租赁")
        st.table({"类型":["日租","周租","月租"],"价格":["100元","500元","1500元"]})

    elif menu == "👤 个人中心":
        st.title("👤 个人中心")
        st.info("姓名：重庆理工大学学员\n等级：实习员\n贡献值：28")