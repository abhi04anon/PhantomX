## ⚠️ Disclaimer
This tool is for educational and authorized penetration testing only.
The author is not responsible for misuse or damage caused.

##⚡ PhantomX Offensive Toolkit ⚡
``
PhantomX is an all-in-one, command-line penetration testing toolkit designed for security professionals and ethical hackers.
It streamlines reconnaissance, vulnerability scanning, and exploitation enumeration into a single, easy-to-use interface, providing organized outputs and modular workflow for efficient testing.
``
---
## 📸 Screenshot
<img width="1070" height="640" alt="Screenshot 2025-08-29 121314" src="https://github.com/user-attachments/assets/f0c0c15a-1201-4262-bc98-06b3e5103966" />

---
# 📂 Repository Structure
```
PhantomX/
│── phantomx.py          # Main executable script
│── config.yaml       # Tool configurations & wordlists
│── requirements.txt  # Python dependencies
│── README.md         # Documentation
│── LICENSE           # MIT license
```
---
## 🚀 Installation
```bash
git clone https://github.com/abhi04anon/PhantomX.git
cd PhantomX
pip install -r requirements.txt
chmod +x phantomx.py
```
---
## 📦 Modules

1.Recon → whois, gobuster, theHarvester, sublist3r, whatweb, amass, ffuf, nmap, wafw00f, massscan

2.Vuln → nikto, enum4linux, searchsploit

3.Full → Runs Recon + Vuln

---

## 🛠 Usage
```bash
1.Recon scan- ./phantomx.py -t <target> -m recon
2.Vuln scan- ./phantomx.py -t <target> -m vuln -w {wordlists}
3.Recon+Vuln scan- ./phantomx.py -t <target> -m full -w {wordlists}
```
---
---

## 👨‍💻 Author
```
Created with ❤️ by **Abhirup Sarkar (@abhi04anon)**  

- GitHub: [abhi04anon] (https://github.com/abhi04anon)    
- LinkedIn: [Abhirup Sarkar] (https://www.linkedin.com/in/abhirup-sarkar-/)
```
---



