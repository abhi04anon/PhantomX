## ⚠️ Disclaimer
This tool is for educational and authorized penetration testing only.
The author is not responsible for misuse or damage caused.

# ⚡ PhantomX Offensive Toolkit ⚡

A custom **multi-tool wrapper** for penetration testers.  
Run recon, vuln, and exploitation helpers from a single CLI.

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

- GitHub: [abhi04anon](https://github.com/abhi04anon)    
- LinkedIn: [Abhirup Sarkar]<a id='https://www.linkedin.com/in/abhirup-sarkar-/'</a>
```
---



