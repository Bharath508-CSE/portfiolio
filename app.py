import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_lottie import st_lottie
import requests

st.set_page_config(layout="wide")


st.write("##")
st.subheader("Welcome to the Streamlit App")
st.title("My Portfolio Website")
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("C:/Users/ctech/OneDrive/Desktop/jarvis/app/style.css")

lottie_contact = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")


st.write("This is a simple portfolio website built with Streamlit.")
st.write("[Read More](https://streamlit.io/)")
st.write("---")
st.sidebar.image("C:/Users/ctech/Downloads/IMG_20250615_185609.jpg",width=200)
st.sidebar.title("C Bharath")
with st.container():
    selected= option_menu(
        menu_title=None,
        options=["About", "Projects", "Contact"],
        icons=["person", "code-slash", "chat-left-text-fill"],
        orientation="horizontal"

    )
if selected == "About":
    with st.container():
        col1,col2= st.columns(2)
        with col1:
            st.write("#")
            st.subheader("I'm C Bharath")
            st.header("Pursuing my B.Tech in Computer Science and Engineering at MITS, Madanapalle.")
            st.write("[Read More](https://streamlit.io/)")

        with col2:
            st.write("##")

            st.image("C:/Users/ctech/Downloads/giphy.gif", width=500)
    st.write("---")
    with st.container():
        col3, col4 ,col5= st.columns(3)
        with col3:
            st.subheader("""
                         Education 
                        - B.Tech
                            - Computer Science and Engineering
                            -MITS, Madanapalle
                            - Grade: 8.1 CGPA
                        - DIPLOMA
                            - Computer Science and Engineering
                            - Government Polytechnic College, NAGARI
                            - Grade: 71%
                        - SSC
                            - ZP High School, AMUDALA
                            - Grade: 84%
                         """)
        with col4:
            st.subheader("""
                        Skills
                        - Python
                        - Java
                        - HTML/CSS
                        - JavaScript
                         """)
        with col5:
            st.subheader("""
                        Hobbies
                        - Playing Cricket
                        - Playing Chess
                        - Reading Books
                        - Watching Movies
                         """)
if selected == "Projects":
    with st.container():
        st.write("#")
        st.subheader("My Projects")
        st.write("##")
        col6,col7=st.columns(2)
        with col6:
            st.image("C:/Users/ctech/OneDrive/Pictures/Screenshots/Screenshot 2025-06-18 220804.png",width=400)

        with col7:
             st.subheader("Voice Assistant – JARVIS")
             st.markdown("""
             **Tech Stack:** Python, SpeechRecognition, pyttsx3, pywhatkit, OS  
             **Description:** A voice-controlled desktop assistant that responds to the wake word "Jarvis" and performs tasks like opening/closing applications, telling time, playing YouTube videos, and answering basic questions.  
             **Features:**
            - Voice Wake Word Detection  
            - Open/Close system apps (Chrome, Notepad, Calculator, etc.)  
            - Play YouTube videos by command  
            - Text-to-Speech response system  
             **Future Scope:** Integration with IoT devices, AI chat features, and smart automation.
            """)
    st.write("---")
    with st.container():
        col8,col9=st.columns(2)
        with col8:

            st.title("Mushroom Classification Project")

            st.subheader("🍄 Mushroom Classification")
            st.write("""
            A machine learning model built to classify mushrooms as edible or poisonous using UCI Mushroom Dataset.  
            - Achieved 95%+ accuracy using Random Forest.  
            - Data preprocessing involved encoding 100% categorical features.  
            - Visualized feature importance and class balance.
            """)

        with col9:
            st.image("C:/Users/ctech/OneDrive/Pictures/Screenshots/Screenshot 2025-06-18 230207.png", width=400)
    st.write("---")
    with st.container():
        col10,col11=st.columns(2)
        with col10:
            st.image("C:/Users/ctech/OneDrive/Pictures/Screenshots/Screenshot 2025-06-18 233913.png", width=400)
        with col11:
            st.subheader("🔐 Password Generator & Strength Checker")
            st.write("""
            A secure password generator and real-time strength checker built using Streamlit.

            **Features**  
            - ✅ Generate secure random passwords  
            - ✅ Strength levels: Weak 🔴, Moderate 🟠, Strong 🟢  
            - ✅ Color-coded feedback  
            - ✅ Fast and user-friendly interface  

            [🔗 View Code on GitHub](https://github.com/Bharath508-CSE/Basic-Task-2.git)  
            """)
if selected == "Contact":
    st.header("Get in Touch")
    st.write("##")
    st.write("##")
    contact_form = """
   <form class="student-form" action="https://formsubmit.co/bharath23695a0508@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="_autoresponse" value="Thank you for contacting me! I have received your message and will get back to you soon.">
    <h2>Student Contact Form</h2>
    <div class="form-group">
        <label for="student_name">Your Name</label>
        <input type="text" id="student_name" name="student_name" placeholder="Enter your name" required>
    </div>
    <div class="form-group">
        <label for="student_email">Your Email</label>
        <input type="email" id="student_email" name="student_email" placeholder="Enter your email" required>
    </div>
    <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="Enter your phone number">
    </div>
    <div class="form-group">
        <label for="institution">Institution/College</label>
        <input type="text" id="institution" name="institution" placeholder="Your college or school">
    </div>
    <div class="form-group">
        <label for="course">Course/Branch</label>
        <input type="text" id="course" name="course" placeholder="e.g. B.Tech CSE, B.Sc Physics">
    </div>
    <div class="form-group">
        <label for="query">How can I help you?</label>
        <textarea id="query" name="query" placeholder="Describe your question or project..." rows="5" required></textarea>
    </div>
    <button type="submit">Send</button>
</form>
    """
    left_col, right_col = st.columns((2, 1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
        st_lottie(lottie_contact, height=300, key="contact")
        st.markdown('</div>', unsafe_allow_html=True)