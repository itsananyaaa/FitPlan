import streamlit as st
import requests
import time

# --- 1. SET PAGE CONFIG ---
st.set_page_config(
    page_title="Vitality Pro | Fitness Planner",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CUSTOM UI THEMING (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        margin-bottom: 25px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background: linear-gradient(90deg, #00DBDE 0%, #FC00FF 100%);
        color: white !important;
        font-weight: bold;
        border: none;
    }

    /* Specialized Cards for Results */
    .diet-item {
        background: rgba(29, 38, 113, 0.3);
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #C33764;
        margin-bottom: 10px;
    }
    
    .workout-day {
        background: rgba(0, 242, 96, 0.1);
        padding: 15px;
        border-radius: 12px;
        border-top: 3px solid #00F260;
        margin-bottom: 10px;
    }

    [data-testid="stMetricValue"] { color: #00DBDE !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- 4. API INTEGRATION ---
def get_plan_from_api(age, weight, height, gender, preference):
    # This connects to the Flask backend we updated
    API_URL = "http://localhost:5000/api/generate-plan"
    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "gender": gender,
        "dietary_preference": preference
    }
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            return response.json()
    except:
        return None

# --- 5. PAGE: LOGIN ---
def show_login():
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        st.markdown("<h1 style='text-align: center; color: #00DBDE;'>⚡ VITALITY PRO</h1>", unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="main-card">', unsafe_allow_html=True)
            user = st.text_input("Username")
            pw = st.text_input("Password", type="password")
            if st.button("Access Dashboard"):
                st.session_state.logged_in = True
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

# --- 6. PAGE: DASHBOARD ---
def show_dashboard():
    c1, c2 = st.columns([4, 1])
    with c1:
        st.markdown("<h1>🚀 My Performance Roadmap</h1>", unsafe_allow_html=True)
    with c2:
        if st.button("Sign Out"):
            st.session_state.logged_in = False
            st.rerun()

    # Input Section
    with st.container():
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        colA, colB, colC = st.columns(3)
        with colA:
            age = st.number_input("Age", 15, 90, 25)
            gender = st.selectbox("Gender", ["Male", "Female"])
        with colB:
            weight = st.number_input("Weight (kg)", 40, 200, 75)
            height = st.number_input("Height (cm)", 100, 250, 175)
        with colC:
            diet_pref = st.selectbox("Diet Preference", ["Balanced", "Vegetarian", "Vegan", "Keto", "Paleo"])
        
        generate = st.button("GENERATE MY 7-DAY PLAN")
        st.markdown('</div>', unsafe_allow_html=True)

    # Output Section
    if generate:
        with st.spinner("Syncing with ZenFlow Engine..."):
            data = get_plan_from_api(age, weight, height, gender, diet_pref)
            
            if data:
                st.balloons()
                
                # --- ROW 1: MACROS ---
                st.markdown("### 📊 Nutritional Targets")
                nutri = data['nutritional_plan']
                m1, m2, m3, m4 = st.columns(4)
                m1.metric("Calories", f"{nutri['daily_calories']} kcal")
                m2.metric("Protein", f"{nutri['macros']['protein_g']}g")
                m3.metric("Carbs", f"{nutri['macros']['carbs_g']}g")
                m4.metric("Fats", f"{nutri['macros']['fats_g']}g")

                st.divider()

                # --- ROW 2: DIET & WORKOUT ---
                res_col1, res_col2 = st.columns([1, 1.5])
                
                with res_col1:
                    st.subheader("🍴 Daily Diet Plan")
                    for meal, desc in data['diet_plan'].items():
                        st.markdown(f"""
                            <div class="diet-item">
                                <strong>{meal}</strong><br>
                                <small>{desc}</small>
                            </div>
                        """, unsafe_allow_html=True)
                
                with res_col2:
                    st.subheader("🏋️ 7-Day Workout Schedule")
                    workout = data['workout_plan']
                    # Split workout into two mini-columns for better fit
                    w_left, w_right = st.columns(2)
                    days = list(workout.items())
                    
                    for i, (day, act) in enumerate(days):
                        target = w_left if i < 4 else w_right
                        target.markdown(f"""
                            <div class="workout-day">
                                <strong>{day}</strong><br>
                                <small>{act}</small>
                            </div>
                        """, unsafe_allow_html=True)
            else:
                st.error("Connection Error: Is the Flask backend running?")

# --- 7. APP LOGIC ---
if st.session_state.logged_in:
    show_dashboard()
else:
    show_login()