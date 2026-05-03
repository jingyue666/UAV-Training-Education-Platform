import streamlit as st
import json
import os

# ================== 页面配置 ==================
st.set_page_config(
    page_title="御宇 · 无人机教培平台",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================== 界面美化 ==================
st.markdown("""
<style>
    .main { background-color: #f9fbfd; }
    .stButton>button {
        background-color: #165DFF;
        color: white;
        border-radius: 12px;
        height: 70px;
        font-size: 16px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ================== 用户数据 ==================
USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_user(username, pwd):
    users = load_users()
    users[username] = pwd
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False)

# ================== 状态 ==================
if "login" not in st.session_state:
    st.session_state.login = False
if "user" not in st.session_state:
    st.session_state.user = ""
if "page" not in st.session_state:
    st.session_state.page = "home"

# ================== 登录 / 注册 ==================
if not st.session_state.login:
    col_center = st.columns([1, 2, 1])[1]
    with col_center:
        st.markdown("<h1 style='text-align:center; color:#165DFF'>🛸 御 宇</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center; margin-bottom:40px;'>无人机教培商业生态平台</h3>", unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["🔐 登录", "📝 注册"])
        with tab1:
            username = st.text_input("账号")
            pwd = st.text_input("密码", type="password")
            if st.button("登 录", use_container_width=True):
                users = load_users()
                if username in users and users[username] == pwd:
                    st.session_state.login = True
                    st.session_state.user = username
                    st.rerun()
                else:
                    st.error("账号或密码错误")

        with tab2:
            new_u = st.text_input("设置账号")
            new_p = st.text_input("设置密码", type="password")
            if st.button("注 册", use_container_width=True):
                if new_u and new_p:
                    users = load_users()
                    if new_u in users:
                        st.warning("账号已存在")
                    else:
                        save_user(new_u, new_p)
                        st.success("注册成功！请登录")
                else:
                    st.warning("请输入账号密码")

# ================== 主平台 ==================
else:
    def go_page(page):
        st.session_state.page = page

    # 顶部栏
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1: st.markdown("### 🛸 御宇")
    with col3:
        st.markdown(f"欢迎：{st.session_state.user}")
        if st.button("退出登录"):
            st.session_state.login = False
            st.rerun()

    st.divider()

    if st.session_state.page == "home":
        st.markdown("<h1 style='text-align:center;'>御宇无人机教培平台</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; font-size:18px;'>培训 · 网课 · 考证 · 个人中心</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1: st.button("📚 在线网课", use_container_width=True, on_click=go_page, args=("class",))
        with c2: st.button("🎖️ CAAC 考证", use_container_width=True, on_click=go_page, args=("exam",))
        with c3: st.button("👤 个人中心", use_container_width=True, on_click=go_page, args=("center",))

    elif st.session_state.page == "class":
        st.title("📚 在线网课学习中心")
        st.button("← 返回主页", on_click=go_page, args=("home",))
        t1, t2, t3 = st.tabs(["初级课程", "中级课程", "高级课程"])
        with t1:
            st.subheader("初级无人机操作（120课时）")
            st.video("https://www.w3school.com.cn/i/movie.mp4")
        with t2:
            st.subheader("中级山地植保课程")
            st.video("https://www.w3school.com.cn/i/movie.mp4")
        with t3:
            st.subheader("高级城市巡检课程")
            st.video("https://www.w3school.com.cn/i/movie.mp4")

    elif st.session_state.page == "exam":
        st.title("🎖️ CAAC 无人机考证服务")
        st.button("← 返回主页", on_click=go_page, args=("home",))
        st.info("1. 学习课程 → 2. 模拟考试 → 3. 线下考核 → 4. 颁发证书")

    elif st.session_state.page == "center":
        st.title("👤 个人学习中心")
        st.button("← 返回主页", on_click=go_page, args=("home",))
        st.success(f"账号：{st.session_state.user}\n等级：实习学员\n学习进度：35%")
        st.progress(35)
