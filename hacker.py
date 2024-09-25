import streamlit as st
import time
import random
import numpy as np

st.set_page_config(
    page_title="Hacker Simulator",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add CSS for matrix effect and styling
st.markdown("""
    <style>
    body {
        background-color: black;
        color: #00FF00;
        overflow: hidden;
        font-family: 'Courier', monospace;
    }
    .hacker-text {
        color: #00FF00;
        font-size: 16px;
        white-space: pre-wrap;
        word-wrap: break-word;
    }
    #header {
        text-align: center;
    }
    #control-panel {
        margin-top: 20px;
    }
    .stProgress > div > div > div > div {
        background-color: #00FF00;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("<h1 id='header' class='hacker-text'>💻 HACKER SIMULATOR 💻</h1>", unsafe_allow_html=True)

# Create columns for layout
col1, col2 = st.columns(2)

# Function to generate matrix effect
def generate_matrix_lines():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>/?"
    return ''.join(random.choices(chars, k=60))

def matrix_stream():
    placeholder = col1.empty()
    for _ in range(100):
        lines = "\n".join([generate_matrix_lines() for _ in range(20)])
        placeholder.markdown(f"<div class='hacker-text'>{lines}</div>", unsafe_allow_html=True)
        time.sleep(0.1)
    placeholder.empty()

# Fake terminal with interactive commands
def terminal():
    placeholder = col1.empty()
    terminal_history = []
    while True:
        cmd = col1.text_input("Enter Command:", key=str(random.randint(0, 1000000)))
        if cmd:
            response = random.choice([
                "Command not found",
                f"Executed {cmd} successfully",
                "Error: Access Denied",
                f"Output of {cmd}:\n" + generate_matrix_lines()
            ])
            terminal_history.append(f"$ {cmd}\n{response}\n")
            history = "\n".join(terminal_history[-5:])  # Show last 5 commands
            placeholder.markdown(f"<div class='hacker-text'>{history}</div>", unsafe_allow_html=True)
            time.sleep(1)
        else:
            break

# Progress bar for "hacking"
def hacking_progress_bar(task, duration):
    col2.markdown(f"<p class='hacker-text'>[+] {task}</p>", unsafe_allow_html=True)
    progress = col2.progress(0)
    for percent in range(100):
        time.sleep(duration)
        progress.progress(percent + 1)
    col2.markdown(f"<p class='hacker-text'>[+] {task} - Completed</p>", unsafe_allow_html=True)

# Fake Password Decryption
def fake_password_decryption():
    col2.markdown("<p class='hacker-text'>[*] Decrypting Passwords...</p>", unsafe_allow_html=True)
    passwords = ["admin", "root", "123456", "letmein", "password", "hunter2"]
    for password in passwords:
        time.sleep(1)
        col2.markdown(f"<p class='hacker-text'>[+] Decrypted Password: {password}</p>", unsafe_allow_html=True)
    col2.markdown("<p class='hacker-text'>[*] Password Decryption Completed!</p>", unsafe_allow_html=True)

# Fake File System Navigation
def file_system_navigation():
    col2.markdown("<p class='hacker-text'>[*] Navigating File System...</p>", unsafe_allow_html=True)
    directories = ["/", "/home", "/home/user", "/home/user/documents", "/var/log", "/etc", "/etc/ssh"]
    for directory in directories:
        time.sleep(0.5)
        col2.markdown(f"<p class='hacker-text'>cd {directory}</p>", unsafe_allow_html=True)
        files = ["config.txt", "data.bin", "notes.md", "passwd", "shadow"]
        for file in files:
            time.sleep(0.1)
            col2.markdown(f"<p class='hacker-text'>-rw-r--r-- 1 user user 4096 Jan 1 12:00 {file}</p>", unsafe_allow_html=True)

# Fake Email Hacking Simulation
def email_hacking():
    col2.markdown("<p class='hacker-text'>[*] Accessing Email Server...</p>", unsafe_allow_html=True)
    for _ in range(5):
        email = f"user{random.randint(1, 100)}@example.com"
        time.sleep(0.5)
        col2.markdown(f"<p class='hacker-text'>[+] Found Email: {email}</p>", unsafe_allow_html=True)
    col2.markdown("<p class='hacker-text'>[*] Extracting Emails...</p>", unsafe_allow_html=True)
    for _ in range(10):
        subject = f"Subject: {generate_matrix_lines()[:20]}"
        time.sleep(0.3)
        col2.markdown(f"<p class='hacker-text'>{subject}</p>", unsafe_allow_html=True)
    col2.markdown("<p class='hacker-text'>[*] Email Extraction Completed!</p>", unsafe_allow_html=True)

# Sidebar with options
st.sidebar.markdown("<h2 id='control-panel' class='hacker-text'>Control Panel</h2>", unsafe_allow_html=True)

if st.sidebar.button("Start Matrix"):
    matrix_stream()

if st.sidebar.button("Interactive Terminal"):
    terminal()

if st.sidebar.button("Start Hack"):
    hacking_progress_bar("Scanning network", 0.01)
    hacking_progress_bar("Exploiting vulnerability", 0.03)
    hacking_progress_bar("Extracting data", 0.02)

if st.sidebar.button("Decrypt Passwords"):
    fake_password_decryption()

if st.sidebar.button("Navigate File System"):
    file_system_navigation()

if st.sidebar.button("Email Hack"):
    email_hacking()

# Conclusion
st.markdown("<p class='hacker-text'>[*] Operation Completed!</p>", unsafe_allow_html=True)

# Extra Fun: Show a Random Fake Warning
if st.sidebar.button("Show Warning"):
    st.markdown("<h1 style='color:red;'>⚠️ SYSTEM BREACH DETECTED ⚠️</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hacker-text'>Immediate action required! The system is compromised!</p>", unsafe_allow_html=True)