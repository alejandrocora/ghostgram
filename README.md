<img src="ghostgram.jpeg" width="75px" height="75px" align="right">

[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)]()
[![Python](https://img.shields.io/badge/python-3.13.7-blue.svg)](https://www.python.org/)
![Selenium](https://img.shields.io/badge/Selenium-4.32.0-blue.svg?logo=selenium&logoColor=white)
![Security](https://img.shields.io/badge/security-identity_check-blue)
[![License: GPL v3](https://img.shields.io/badge/license-GPLv3-lightgray.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-beta-orange.svg)]()

# Ghostgram - Instagram Comment Deleter (Beta)

Ghostgram automates the process of deleting all your Instagram comments, since Instagram does not provide an option to do this instantly.

<img src="ghostgram_screenshot.png" width="600px">

---

## ⚠️ Note

Instagram ToS prohibits the use of bots or automation. Use this tool at your own risk. This tool is **not official** and **not affiliated** with Instagram.

---

## Before Using

You will need a **WebDriver** installed for the browser you plan to use:  

- **Firefox** (GeckoDriver)  
- **Chrome** (ChromeDriver)  

---

## Installation

```
$ git clone https://github.com/yourusername/ghostgram
$ cd ghostgram
$ pip3 install . --break-system-packages
```

---

## Usage

Run Ghostgram with the following command:  

```
ghostgram --firefox --visual --username YOUR_USERNAME --password YOUR_PASSWORD
```

### Options

```
usage: ghostgram [-h] [--firefox] [--chrome] [--visual] --username USERNAME --password PASSWORD

options:
  -h, --help           show this help message and exit
  --firefox            Use Firefox.
  --chrome             Use Chrome.
  --visual             Show browser UI.
  --username USERNAME  Instagram username.
  --password PASSWORD  Instagram password.
```

---

## Disclaimer

The author is **not responsible** for misuse, account bans, or any errors caused by this tool. Always follow **legal and privacy guidelines**.  

---

## Author

**Alejandro Cora**  
<https://github.com/alejandrocora>