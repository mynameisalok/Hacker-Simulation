import streamlit as st
import time
import random
import string

st.set_page_config(page_title="Advanced Hacker Simulator", page_icon="🕵️", layout="wide", initial_sidebar_state="collapsed")

# Enhanced CSS for a more intimidating look
st.markdown("""
<style>
body {
    background-color: #000;
    color: #0F0;
    font-family: 'Courier New', monospace;
}
.stApp {
    background-image: linear-gradient(rgba(0, 255, 0, 0.1) 1px, transparent 1px),
                      linear-gradient(90deg, rgba(0, 255, 0, 0.1) 1px, transparent 1px);
    background-size: 20px 20px;
}
.main {
    background-color: rgba(0, 0, 0, 0.7);
    padding: 2rem;
    border-radius: 10px;
    border: 1px solid #0F0;
}
.hacker-text {
    color: #0F0;
    font-size: 14px;
    white-space: pre-wrap;
    word-wrap: break-word;
    text-shadow: 0 0 5px #0F0;
}
.stButton>button {
    background-color: #000;
    color: #0F0;
    border: 1px solid #0F0;
}
.stButton>button:hover {
    background-color: #0F0;
    color: #000;
}
.warning {
    color: #FF0000;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    animation: blink 1s infinite;
}
@keyframes blink {
    0% {opacity: 0;}
    50% {opacity: 1;}
    100% {opacity: 0;}
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #0F0;'>🕵️ ADVANCED HACKER SIMULATOR 🕵️</h1>", unsafe_allow_html=True)

# Create columns for layout
col1, col2 = st.columns(2)

# 1. Enhanced Matrix Rain Effect
def matrix_rain():
    placeholder = col1.empty()
    chars = string.ascii_letters + string.digits + string.punctuation
    lines = ["" for _ in range(20)]
    for _ in range(100):
        for i in range(20):
            if random.random() < 0.1:
                lines[i] = ''.join(random.choice(chars) for _ in range(60))
            else:
                lines[i] = lines[i][1:] + random.choice(chars)
        placeholder.markdown(f"<div class='hacker-text'>{'<br>'.join(lines)}</div>", unsafe_allow_html=True)
        time.sleep(0.05)
    placeholder.empty()

# 2. Advanced Network Scanner
def network_scanner():
    col2.markdown("<h3 class='hacker-text'>🌐 Network Scanner</h3>", unsafe_allow_html=True)
    progress = col2.progress(0)
    ips = [f"192.168.1.{i}" for i in range(1, 255)]
    open_ports = [21, 22, 80, 443, 3306, 5432]
    for i, ip in enumerate(ips):
        if random.random() < 0.1:
            ports = random.sample(open_ports, k=random.randint(1, 3))
            col2.markdown(f"<p class='hacker-text'>[+] {ip} - Open ports: {', '.join(map(str, ports))}</p>", unsafe_allow_html=True)
        progress.progress((i + 1) / len(ips))
        time.sleep(0.01)
    col2.markdown("<p class='hacker-text'>[✓] Network scan completed</p>", unsafe_allow_html=True)

# 3. Brute Force Password Cracker
def password_cracker():
    col2.markdown("<h3 class='hacker-text'>🔓 Password Cracker</h3>", unsafe_allow_html=True)
    target = "admin@example.com"
    col2.markdown(f"<p class='hacker-text'>[*] Target: {target}</p>", unsafe_allow_html=True)
    progress = col2.progress(0)
    for i in range(100):
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        col2.markdown(f"<p class='hacker-text'>[*] Trying: {password}</p>", unsafe_allow_html=True)
        progress.progress(i + 1)
        time.sleep(0.05)
    col2.markdown(f"<p class='hacker-text'>[✓] Password cracked: {''.join(random.choices(string.ascii_letters + string.digits, k=12))}</p>", unsafe_allow_html=True)

# 4. Data Exfiltration Simulator
def data_exfiltration():
    col2.markdown("<h3 class='hacker-text'>📤 Data Exfiltration</h3>", unsafe_allow_html=True)
    files = ["user_data.db", "financial_records.xlsx", "passwords.txt", "confidential_report.pdf", "emails.pst"]
    total_size = sum(random.randint(100, 1000) for _ in files)
    progress = col2.progress(0)
    for file in files:
        size = random.randint(100, 1000)
        col2.markdown(f"<p class='hacker-text'>[*] Extracting: {file} ({size} MB)</p>", unsafe_allow_html=True)
        for i in range(size):
            progress.progress((i + 1) / total_size)
            time.sleep(0.01)
    col2.markdown("<p class='hacker-text'>[✓] Data exfiltration complete</p>", unsafe_allow_html=True)

# 5. System Backdoor Installation
def install_backdoor():
    col2.markdown("<h3 class='hacker-text'>🚪 Backdoor Installation</h3>", unsafe_allow_html=True)
    stages = ["Creating payload", "Bypassing antivirus", "Exploiting vulnerability", "Elevating privileges", "Establishing persistence"]
    progress = col2.progress(0)
    for i, stage in enumerate(stages):
        col2.markdown(f"<p class='hacker-text'>[*] {stage}...</p>", unsafe_allow_html=True)
        for j in range(20):
            progress.progress((i * 20 + j + 1) / 100)
            time.sleep(0.05)
    col2.markdown("<p class='hacker-text'>[✓] Backdoor successfully installed</p>", unsafe_allow_html=True)

# 6. Simulated System Takeover
def system_takeover():
    col1.markdown("<h3 class='hacker-text'>🖥️ System Takeover</h3>", unsafe_allow_html=True)
    services = ["Firewall", "Antivirus", "User Authentication", "File System", "Network Services"]
    for service in services:
        col1.markdown(f"<p class='hacker-text'>[*] Disabling {service}...</p>", unsafe_allow_html=True)
        time.sleep(1)
        col1.markdown(f"<p class='hacker-text'>[✓] {service} disabled</p>", unsafe_allow_html=True)
    time.sleep(1)
    col1.markdown("<p class='warning'>⚠️ SYSTEM COMPROMISED ⚠️</p>", unsafe_allow_html=True)
    col1.markdown("<p class='hacker-text'>[✓] Full system control achieved</p>", unsafe_allow_html=True)

# Sidebar with options
st.sidebar.markdown("<h2 style='color: #0F0;'>Hacker's Toolkit</h2>", unsafe_allow_html=True)

if st.sidebar.button("1. Start Matrix Rain"):
    matrix_rain()

if st.sidebar.button("2. Scan Network"):
    network_scanner()

if st.sidebar.button("3. Crack Passwords"):
    password_cracker()

if st.sidebar.button("4. Exfiltrate Data"):
    data_exfiltration()

if st.sidebar.button("5. Install Backdoor"):
    install_backdoor()

if st.sidebar.button("6. Take Over System"):
    system_takeover()

# Disclaimer
st.markdown("<p style='text-align: center; color: #FF0000; font-size: 12px;'>⚠️ This is a simulation for educational purposes only. Unauthorized hacking is illegal. ⚠️</p>", unsafe_allow_html=True)
