# AI SECSCAN

AI SECSCAN is a Python-based tool that leverages **Google's Gemini AI** to analyze network security scans, detect vulnerabilities, and provide technical insights. It automates **Nmap** and **Gobuster** scans, generating a professional vulnerability report for security professionals and IT students.

## Features
- **AI-Driven Analysis**: Uses **Gemini AI** to analyze scan results and provide security insights.
- **Automated Vulnerability Scanning**: Runs **Nmap** to detect open ports, services, and potential vulnerabilities.
- **Directory Enumeration**: Uses **Gobuster** to discover hidden directories and files.
- **Professional Security Reports**: Generates AI-enhanced reports with attack vectors and mitigation strategies.

## Requirements
- Python 3.12.x
- Google Generative AI (`google-generativeai`)
- Nmap
- Gobuster

## Installation

### 1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/AI-SECSCAN.git
```

### 2\. Navigate to the project folder:

```
cd ai-secscan
```

### 3\. Install system dependencies (Nmap & Gobuster)

AI SECSCAN relies on **Nmap** and **Gobuster**, so install them before proceeding:

**For Debian-based systems (Kali, Ubuntu, ParrotOS):**

```
sudo apt update
sudo apt install nmap gobuster -y
```

**For Arch-based systems (Manjaro, BlackArch):**

```
sudo pacman -S nmap gobuster
```

**For RHEL-based systems (Fedora, CentOS):**

```
sudo dnf install nmap gobuster -y
```

### 4\. Get the Gemini API Key

-   Go to [Google AI Studio](https://aistudio.google.com/apikey) and sign in.
-   Navigate to the API Keys section.
-   Generate a new API key and copy it.
-   Now modify with your actual API key:

    ```
    nano config.py
    ```

-   Replace `api_key` with your actual API key in `config.py`:

    ```
    GEMINI_API_KEY="aaddxxxxx"
    ```

-   Save and exit: `CTRL + X`, press `Y`, then `ENTER`.

### 5\. Install Python dependencies:

```
pip install -r requirements.txt --break-system-packages
```

Usage
-----

-   Run the script:

    ```
    python scanner.py
    ```

```
     \    _ _|       ___|                ___|                      
    _ \     |      \___ \    _ \   __| \___ \    __|   _` |  __ \  
   ___ \    |            |   __/  (          |  (     (   |  |   | 
 _/    _\ ___|     _____/  \___| \___| _____/  \___| \__,_| _|  _| 

 + -- --=[ AI-powered security scanning tool ]--  
 + -- --=[ Automated Nmap & Gobuster scans with AI analysis ]  
 + -- --=[ Generates professional vulnerability reports for IT security ]


Enter the target IP or URL: 
```

-   Enter the target system when prompted.
-   Review the AI-generated vulnerability report in real time.

Contributing
------------

Contributions are welcome! Feel free to open an issue or submit a pull request.

```
