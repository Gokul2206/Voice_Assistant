import streamlit as st
from speech_utils import listen, speak
from commands import process_command

# 1. Setup full-screen page config
st.set_page_config(page_title="Voice Assistant", page_icon="🎙️", layout="wide", initial_sidebar_state="collapsed")

# 2. Inject Custom CSS for a modern, Copilot-like interface
st.markdown("""
<style>
    /* Hide default Streamlit top header, menu, and footer */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Center the main interface and limit width for readability */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
    }
    
    /* Style the big Primary Button (The Microphone) */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #0078D4 0%, #00C6FF 100%);
        color: white;
        border-radius: 50px;
        height: 70px;
        font-size: 22px;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 15px rgba(0, 198, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    /* Add hover effect (glowing effect) for the mic button */
    .stButton > button[kind="primary"]:hover {
        transform: scale(1.03);
        box-shadow: 0 6px 25px rgba(0, 198, 255, 0.6);
    }
    
    /* Style the Secondary Button (Clear History) */
    .stButton > button[kind="secondary"] {
        border-radius: 50px;
        height: 70px;
        font-size: 18px;
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# 3. Custom Title
st.markdown("<h1 style='text-align: center; font-weight: 400; margin-bottom: 1rem;'>🎙️ Voice Assistant</h1>", unsafe_allow_html=True)

# 4. State Management
if "messages" not in st.session_state:
    st.session_state.messages = []

# Refactored message state to use roles for Streamlit's native chat UI
def add_message(role, msg):
    st.session_state.messages.append({"role": role, "content": msg})

# 5. Chat Interface (Fixed height keeps buttons anchored at the bottom)
chat_container = st.container(height=450)

with chat_container:
    if not st.session_state.messages:
        # Placeholder text when empty
        st.markdown("<h3 style='text-align: center; color: #888; font-weight: 300; margin-top: 120px;'>Tap the microphone and start speaking...</h3>", unsafe_allow_html=True)
    
    # Render all stored messages natively
    for msg in st.session_state.messages:
        # Assign avatars based on role
        avatar = "👤" if msg["role"] == "user" else "🤖"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

st.write("") # Spacer

# 6. Bottom Control Panel 
# Using columns to center the big mic button and put clear next to it
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    listen_btn = st.button("🎙️ Tap to Speak", type="primary", use_container_width=True)
    
with col3:
    if st.session_state.messages:
        clear_btn = st.button("🗑️ Clear", type="secondary", use_container_width=True)
    else:
        clear_btn = False

# 7. Core Functionality Logic
if listen_btn:
    # 1. Listen
    with st.spinner("🎙️ Listening..."):
        command = listen(duration=5)
    
    if command:
        # Show User Input
        add_message("user", command)
        
        # 2. Process
        with st.spinner("🧠 Thinking..."):
            response = process_command(command)
        
        # Show & Speak Assistant Output
        add_message("assistant", response)
        speak(response)
    else:
        # Error handling
        msg = "Sorry, I didn't catch that."
        add_message("assistant", msg)
        speak(msg)
        
    st.rerun()

if clear_btn:
    st.session_state.messages = []
    st.rerun()