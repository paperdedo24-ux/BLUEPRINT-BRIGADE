import streamlit as st
import google.generativeai as genai

# --- 1. CORE ENGINE CONFIGURATION ---
# Stable API connection logic
API_KEY = "AIzaSyD8i5aEqAp2xjWHRmMu2BA8HcdVwaenBb8"
genai.configure(api_key=API_KEY)

# Trying the most stable model strings
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    model = genai.GenerativeModel('gemini-pro')

# --- 2. PREMIUM UI CONFIGURATION ---
st.set_page_config(page_title="Blueprint Brigade | Solution Challenge", page_icon="🏗️", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700;800&display=swap');
    
    * { font-family: 'Space Grotesk', sans-serif; }
    .stApp { background-color: #f0f4f8 !important; }

    .hero-title {
        background: linear-gradient(90deg, #001D3D, #003566, #3D5A80);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 55px !important;
        font-weight: 800;
        margin-top: -50px;
    }

    /* Professional Sector Cards */
    .sector-card {
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .vol-bg { background-color: #001D3D; color: #ffffff; border-bottom: 8px solid #FFD60A; }
    .ngo-bg { background-color: #E0FBFC; color: #001D3D; border-bottom: 8px solid #3D5A80; }

    /* Fix Text Visibility in Inputs */
    .stTextArea label { 
        color: #001D3D !important; 
        font-weight: 800 !important;
        font-size: 1.1rem !important;
    }
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #001D3D !important;
    }

    /* Action Button */
    .stButton>button {
        background: linear-gradient(90deg, #003566, #3D5A80) !important;
        color: white !important;
        border-radius: 50px !important;
        height: 60px;
        font-size: 20px !important;
        font-weight: bold !important;
        width: 100%;
        border: none !important;
        box-shadow: 0 10px 20px rgba(0,53,102,0.3);
    }

    /* Analysis Report Box */
    .report-box {
        background: white;
        padding: 35px;
        border-radius: 25px;
        border-left: 12px solid #001D3D;
        box-shadow: 0 15px 40px rgba(0,0,0,0.1);
        margin-top: 30px;
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER ---
st.markdown("<h1 class='hero-title'>BLUEPRINT BRIGADE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #3D5A80;'>Strategic Volunteer & NGO Matching System</p>", unsafe_allow_html=True)
st.divider()

# --- 4. FUNCTIONAL INTERFACE ---
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("<div class='sector-card vol-bg'><h3>👤 Volunteer Profile</h3><p style='color: #e0e0e0;'>Tell us what you can help with.</p></div>", unsafe_allow_html=True)
    v_skills = st.text_area("Your Skills & Expertise", placeholder="Example: Coding, Teaching, Graphics...", height=150, key="vol_box")

with col2:
    st.markdown("<div class='sector-card ngo-bg'><h3>🏢 NGO / Mission</h3><p style='color: #3D5A80;'>Tell us what kind of help you need.</p></div>", unsafe_allow_html=True)
    ngo_need = st.text_area("Requirements & Needs", placeholder="Example: Need a math teacher for 10 kids...", height=150, key="ngo_box")

# --- 5. EXECUTION LOGIC ---
st.write("")
if st.button("RUN SMART ANALYSIS 🚀"):
    if v_skills and ngo_need:
        with st.spinner("Brigade AI is analyzing tactical alignment..."):
            try:
                # Direct generation call
                response = model.generate_content(f"Analyze match between Volunteer: {v_skills} and NGO: {ngo_need}. Provide: 1. Score % 2. Compatibility 3. 3-step action plan.")
                st.balloons()
                st.markdown("<div class='report-box'>", unsafe_allow_html=True)
                st.markdown("## 🎯 Strategic Alignment Report")
                st.markdown(response.text)
                st.markdown("</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error("Connection Error. Please check your internet or API key.")
    else:
        st.warning("Please fill both sectors to analyze.")

# --- 6. SIDEBAR ---
with st.sidebar:
    st.title("🏗️ Project Info")
    st.info("Solution Challenge 2026")
    st.write("**Architecture:** Gemini 1.5 Flash")
    st.success("System: Ready")