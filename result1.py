import streamlit as st
import json
import os

# ================== 页面配置 ==================
st.set_page_config(
    page_title="御宇 · 无人机教培平台",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================== 样式美化 ==================
st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button {
        background-color: #165DFF;
        color: white;
        border-radius: 8px;
        height: 3.2em;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
    }
    [data-testid=stSidebar] {
        background-color: #0f172a;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ================== 用户数据存储 ==================
USER_DB = "users.json"

def load_users():
    if os.path.exists(USER_DB):
        with open(USER_DB, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_user(username, password):
    users = load_users()
    users[username] = password
    with open(USER_DB, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False)

# ================== 会话状态 ==================
if "login" not in st.session_state:
    st.session_state.login = False
if "user" not in st.session_state:
    st.session_state.user = ""

# ================== 登录 / 注册 ==================
if not st.session_state.login:
    st.markdown("<h1 style='text-align: center; color:#165DFF'>🛸 御宇无人机教培平台</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; margin-bottom:40px;'>重庆理工大学 | 低空经济创新大赛</h4>", unsafe_allow_html=True)

    tab = st.tabs(["🔐 登录", "📝 注册"])
    with tab[0]:
        username = st.text_input("账号", key="login_user")
        password = st.text_input("密码", type="password", key="login_pwd")
        if st.button("登 录", use_container_width=True):
            users = load_users()
            if username in users and users[username] == password:
                st.session_state.login = True
                st.session_state.user = username
                st.success("登录成功！")
                st.rerun()
            else:
                st.error("账号或密码错误")

    with tab[1]:
        new_user = st.text_input("设置账号")
        new_pwd = st.text_input("设置密码", type="password")
        if st.button("注 册", use_container_width=True):
            if new_user and new_pwd:
                users = load_users()
                if new_user in users:
                    st.warning("账号已存在")
                else:
                    save_user(new_user, new_pwd)
                    st.success("注册成功！请登录")
            else:
                st.warning("请输入账号密码")

    st.markdown("<p style='text-align:center; color:#999; margin-top:60px'>© 2025 御宇平台 · 重庆理工大学</p>", unsafe_allow_html=True)

# ================== 主平台 ==================
else:
    with st.sidebar:
        st.markdown("<h2 style='color:white; text-align:center'>🛸 御宇</h2>", unsafe_allow_html=True)
        menu = st.radio("", [
            "🏠 首页",
            "📚 在线网课",
            "📦 订单接单",
            "🛒 设备租赁",
            "👤 个人中心"
        ])
        st.markdown("---")
        st.markdown(f"**学员：{st.session_state.user}**")
        st.markdown("**等级：实习员**")
        st.markdown("**贡献值：28**")
        st.markdown("---")
        if st.button("退出登录"):
            st.session_state.login = False
            st.rerun()

    # -------------------- 首页 --------------------
    if menu == "🏠 首页":
        st.markdown("<h1 style='color:#165DFF'>🛸 御宇 · 无人机教培商业生态平台</h1>", unsafe_allow_html=True)
        st.markdown("### 教培 · 考证 · 接单 · 就业 · 创业 · 公益")
        st.markdown("---")

        col1, col2, col3, col4 = st.columns(4)
        with col1: st.button("📚 在线网课", use_container_width=True)
        with col2: st.button("✈️ 模拟飞行", use_container_width=True)
        with col3: st.button("📦 订单中心", use_container_width=True)
        with col4: st.button("🎖️ CAAC 考证", use_container_width=True)

        st.success("### 御宇平台使命")
        st.markdown("""
        解决无人机行业“**考证难落地、就业无渠道、服务不标准**”三大痛点，
        打造低空经济时代**教培+就业+服务+公益**一体化生态。
        """)

    # -------------------- 在线网课 --------------------
    elif menu == "📚 在线网课":
        st.title("📚 御宇在线网课中心")
        t1, t2, t3 = st.tabs(["初级课程", "中级课程", "高级课程"])

        with t1:
            st.subheader("✅ 初级无人机操作（120课时）")
            st.video("https://www.w3school.com.cn/i/movie.mp4")
            st.markdown("- 基础操作｜安全规范｜空域法规")
            st.button("开始学习", type="primary", use_container_width=True)

        with t2:
            st.subheader("✅ 中级山地植保（180课时）")
            st.video("https://www.w3school.com.cn/i/movie.mp4")
            st.markdown("- 重庆山地作业｜精准植保｜多机协同")
            st.button("开始学习", type="primary", use_container_width=True)

        with t3:
            st.subheader("✅ 高级城市巡检（240课时）")
            st.video("https://www.w3school.com.cn/i/movie.mp4")
            st.markdown("- 三维建模｜数据采集｜应急救援")
            st.button("开始学习", type="primary", use_container_width=True)

    # -------------------- 订单接单 --------------------
    elif menu == "📦 订单接单":
        st.title("📦 御宇订单中心")
        orders = [
            {"name":"江津柑橘植保作业","area":"重庆江津","money":"2500元","level":"实习员可接"},
            {"name":"巫山山地测绘","area":"重庆巫山","money":"8000元","level":"初级员可接"},
            {"name":"主城管网巡检","area":"重庆主城","money":"12000元","level":"中级员可接"}
        ]

        for i, o in enumerate(orders):
            with st.container(border=True):
                a,b,c,d = st.columns(4)
                a.markdown(f"**{o['name']}**")
                b.write(o['area'])
                c.write(f"**{o['money']}**")
                if d.button("立即抢单", key=i):
                    st.success(f"✅ 抢单成功：{o['name']}")

    # -------------------- 设备租赁 --------------------
    elif menu == "🛒 设备租赁":
        st.title("🛒 御宇设备租赁")
        st.table({
            "租赁类型": ["日租", "周租", "月租"],
            "价格": ["100元", "500元", "1500元"],
            "适用场景": ["临时作业", "短期项目", "长期运营"]
        })
        st.button("立即租赁", type="primary", use_container_width=True)

    # -------------------- 个人中心 --------------------
    elif menu == "👤 个人中心":
        st.title("👤 个人中心")
        st.info(f"""
        学员账号：{st.session_state.user}
        平台等级：实习员
        贡献值：28
        可接订单：基础植保、物资运输
        """)
        st.markdown("### 学习进度")
        st.progress(35)
        st.write("当前进度：35%")
