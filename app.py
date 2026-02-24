import streamlit as st
import re

# 1. Page Config
st.set_page_config(
    page_title="Sims 4 Animation Search",
    layout="wide",
    page_icon="❇️" 
)

# 2. CSS Injection
st.markdown("""
    <style>
    /* Change default accent color */
    :root {
        --primary-color: #44bd32;
    }
    
    /* Title Style */
    h1 {
        color: #49B17A !important;
        text-shadow: 2px 2px 4px #00000033;
    }
    
    /* Button Style */
    div.stButton > button {
        background-color: #49B17A;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #2e8b57; /* Darker green on hover */
        transform: scale(1.05);
    }
    
    /* Input Box Focus Style */
    .stTextInput > div > div > input:focus {
        border-color: #44bd32;
        box-shadow: 0 0 5px rgba(68, 189, 50, 0.5);
    }
    
    /* Success Message Style */
    .stSuccess {
        background-color: #dff9fb;
        border-left-color: #44bd32;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Data Loading with Cache
@st.cache_data
def load_data(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        return None

# Title
st.title("❇️ Sims 4 Animation Codes Search")
st.write("#### **Up to Life and Death EP**")
st.caption("**[List](https://simfileshare.net/folder/207739/)** by **thepancake1** and shared by **onlyabidoang**")

# Input Section
col1, col2 = st.columns([4, 1])
with col1:
    keywords_input = st.text_input("Search keywords:", placeholder="e.g., clean counter")
with col2:
    st.write("") # Spacer
    st.write("") 
    search_clicked = st.button("Search 🔍", use_container_width=True)

# Load Data
file_path = "Sims_4_All_Animation_Codes_Up_to_Life_and_Death.txt"
all_lines = load_data(file_path)

if all_lines is None:
    st.error(f"⚠️ File '{file_path}' not found! Please ensure the .txt file is in the same directory.")
else:
    # Search Logic
    if keywords_input:
        keywords = keywords_input.strip().split()
        
        # Regex to find lines containing ALL keywords (in any order)
        regex_pattern = "".join([f"(?=.*{re.escape(k)})" for k in keywords])
        pattern = re.compile(regex_pattern, re.IGNORECASE)

        results = [line for line in all_lines if pattern.search(line)]

        if results:
            st.success(f"Found {len(results)} result(s):")
            
            # Display results in copy-friendly code blocks
            for line in results:
                st.code(line, language="text")
        else:
            st.warning("No matching results found. Try different keywords. 😢")
    
    elif search_clicked and not keywords_input:
        st.warning("Please enter at least one keyword.")
