<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Type-Security%20Scanner-red.svg" alt="Type">
</p>

<h1 align="center">🔍 VulnScanAI</h1>

<p align="center">
  <strong>Automated Web Vulnerability Scanner</strong>
</p>

<p align="center">
  An intelligent web vulnerability scanner that automatically detects common<br>
  security vulnerabilities including XSS, SQL Injection, and more.
</p>

---

## ✨ Features

- **XSS Detection** - Cross-Site Scripting vulnerability scanning
- **SQL Injection** - Database injection vulnerability detection
- **Form Analysis** - Automatic form discovery and testing
- **Multiple Payloads** - Tests with various attack vectors
- **Error Detection** - Identifies SQL error messages
- **Easy to Use** - Simple command-line interface

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/BlackOussema/VulnScanAI.git
cd VulnScanAI

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Scan a website
python main.py http://example.com

# Scan a specific page
python main.py http://example.com/login.php
```

---

## 📖 Usage

```
usage: main.py [-h] url

VulnScanAI: Automated Vulnerability Scanner

positional arguments:
  url         URL to scan for vulnerabilities

options:
  -h, --help  show this help message and exit
```

---

## 🔍 Vulnerability Checks

### Cross-Site Scripting (XSS)

Tests for reflected XSS vulnerabilities using payloads:
- `<script>alert('XSS')</script>`
- `<img src=x onerror=alert('XSS')>`

### SQL Injection

Tests for SQL injection vulnerabilities using payloads:
- `' OR 1=1 --`
- `' OR '1'='1`

Detects SQL error messages indicating vulnerability.

---

## 📊 Sample Output

```
[*] Scanning http://vulnerable-site.com...
    [*] Checking for XSS on http://vulnerable-site.com
    [*] Checking for SQL Injection on http://vulnerable-site.com
[+] Vulnerabilities found:
  - XSS:
    Potential XSS found in form on http://vulnerable-site.com/search with payload: <script>alert('XSS')</script>
  - SQL Injection:
    Potential SQL Injection found in form on http://vulnerable-site.com/login with payload: ' OR 1=1 --
```

---

## 🔧 How It Works

1. **Form Discovery** - Parses HTML to find all forms
2. **Input Analysis** - Identifies input fields in forms
3. **Payload Injection** - Submits forms with test payloads
4. **Response Analysis** - Checks responses for vulnerability indicators
5. **Report Generation** - Outputs findings to console

---

## 📁 Project Structure

```
VulnScanAI/
├── main.py           # Entry point
├── scanner.py        # Vulnerability scanning logic
├── requirements.txt  # Python dependencies
└── README.md
```

---

## 📋 Requirements

```
requests>=2.28.0
beautifulsoup4>=4.11.0
```

---

## ⚠️ Legal Disclaimer

**This tool is for authorized security testing only.**

- Only scan websites you own or have explicit permission to test
- Unauthorized scanning is illegal and unethical
- The author is not responsible for misuse
- Always follow responsible disclosure practices

### Ethical Usage Guidelines

1. Get written permission before scanning
2. Test in controlled environments first
3. Report vulnerabilities responsibly
4. Do not exploit discovered vulnerabilities
5. Respect rate limits and server resources

---

## 🔮 Future Enhancements

- [ ] CSRF detection
- [ ] Directory traversal scanning
- [ ] Command injection testing
- [ ] Header security analysis
- [ ] AI-powered payload generation
- [ ] HTML/PDF report generation
- [ ] API scanning support

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add your vulnerability checks
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Ghariani Oussema**
- GitHub: [@BlackOussema](https://github.com/BlackOussema)
- Role: Cyber Security Researcher & Full-Stack Developer
- Location: Tunisia 🇹🇳

---

<p align="center">
  Made with ❤️ in Tunisia 🇹🇳
</p>
