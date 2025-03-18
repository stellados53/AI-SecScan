import subprocess
import os
import time
import google.generativeai as genai
import config

# Initialize Gemini AI
genai.configure(api_key=config.GEMINI_API_KEY)


def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)  # Adjust speed of typing effect
    print("\n")


# Function to verify if the target is reachable
def verify_target(target):
    response = subprocess.run(["ping", "-c", "1", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return response.returncode == 0

# Get and verify target IP/URL
while True:
    print(r"""
    
     \    _ _|       ___|                ___|                      
    _ \     |      \___ \    _ \   __| \___ \    __|   _` |  __ \  
   ___ \    |            |   __/  (          |  (     (   |  |   | 
 _/    _\ ___|     _____/  \___| \___| _____/  \___| \__,_| _|  _| 

 + -- --=[ AI-powered security scanning tool ]--  
 + -- --=[ Automated Nmap & Gobuster scans with AI analysis ]  
 + -- --=[ Generates professional vulnerability reports for IT security ]  

 """)
    target = input("Enter the target IP or URL: ").strip()
    if verify_target(target):
        print(f"✅ Target {target} is reachable.")
        break
    else:
        print("❌ Target is not reachable. Please re-enter a valid IP/URL.")

# Run Nmap with full port scan and vulnerability scripts
typing_effect("\n🚀 Running Nmap scan...")
nmap_command = ["nmap", "-p", "--script", "vuln", target]
nmap_result = subprocess.run(nmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
nmap_output = nmap_result.stdout

# Run Gobuster with default wordlist
wordlist = "wordlists/common.txt"
typing_effect("\n🚀 Running Gobuster scan...")
gobuster_command = ["gobuster", "dir", "-u", target, "-w", wordlist]
gobuster_result = subprocess.run(gobuster_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
gobuster_output = gobuster_result.stdout

# Generate AI Report using Gemini
def analyze_results(nmap_output, gobuster_output):
    prompt = f"""
    Analyze the following vulnerability scan results from Nmap and Gobuster.
    Provide a professional security report with insights, attack vectors.

    Nmap Results:
    {nmap_output}

    Gobuster Results:
    {gobuster_output}

    don't use bold text ever.  this has to be strictly followed
    Structure the report in a technical manner suitable for an IT security professional. Don't give unwanted stuff.
    """
    
    model = genai.GenerativeModel("gemini-1.5-pro")  
    response = model.generate_content(prompt)  
    return response.text

# Get AI-generated security report
typing_effect("\n🤖 Generating AI security analysis...\n")
report = analyze_results(nmap_output, gobuster_output)



# Typing Effect for AI Response
def typing_effect1(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.002)  # Adjust speed of typing effect
    print("\n")

typing_effect1(report)


