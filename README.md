# ⚡ WakeOnLAN and Shutdown App

A lightweight Python desktop tool to remotely **Wake Up** or **Shut Down** multiple computers over your local network using WOL (Wake-on-LAN) and Windows remote shutdown commands.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)
![License](https://img.shields.io/badge/License-GPL--3.0-green)
![Status](https://img.shields.io/badge/Status-Stable-success)

---

## 🚀 Features
- 🖥️ Wake up multiple PCs using MAC addresses.
- 🔌 Remotely shut down PCs by hostname or IP.
- 📂 Import systems list from a CSV file.
- 🪟 Simple and clean GUI with icons and logo.
- 💾 Build as `.exe` for easy deployment.
- 🧩 No third-party dependencies — uses only Python standard libraries.
- 🪄 Works on **Windows 10/11**.

---

## 🗂️ Repository Contents

| File | Description |
|------|--------------|
| `WOL_Shutdown_Final_01.py` | Main Python app for Wake-on-LAN & Shutdown operations |
| `computers.csv` | Example system list (hostname, MAC, IP) |
| `logo.ico` / `logo.png` | App icons |
| `LICENSE` | GPL-3.0 license file |
| `README.md` | This documentation file |

---

## ⚙️ Requirements

- Python **3.10 or newer**
- Works out of the box with:
  - `tkinter`
  - `csv`
  - `os`, `socket`, `subprocess`, `platform`  
  *(All part of Python’s standard library)*

Folder structure (VERY important)

Put all files in one folder, for example:

C:\WOL_Shutdown_App\

C:\WOL_Shutdown_App\WOL_Shutdown_Final.py
C:\WOL_Shutdown_App\logo.png                     ← your  logo
C:\WOL_Shutdown_App\computers.csv                ← your CSV (optional)


🖼️ Screenshots
Main Interface

(Example UI view — replace with your actual image later)


CSV Example

🎥 Demo (Optional GIF)

Add a short demo GIF to show how the app works:

![Demo GIF](https://via.placeholder.com/800x400?text=App+Demo)


You can record one using:

Windows Xbox Game Bar (Win + G)

or ScreenToGif (https://www.screentogif.com/
)

🧩 Step 1 — Install PyInstaller

Run this command in Command Prompt (cmd):

pip install pyinstaller wakeonlan pillow


If pip isn’t recognized, try:

python -m ensurepip
python -m pip install pyinstaller

🧩 Step 2 — Verify Installation

Check that it’s installed correctly:

python -m pyinstaller --version


You should see a version number (e.g., 6.10.0).

🧩 Step 3 — Create EXE

Now rerun your build command:

pyinstaller --onefile --noconsole WOL_Shutdown_Final.py


After a few minutes, your .exe will appear in:

C:\WOL_Shutdown_App\dist\WOL_Shutdown_Final.exe


✅ Optional tip:
If you’ll create .exe files often, install PyInstaller globally for all users:

pip install pyinstaller --upgrade --user

📜 License

Licensed under the GNU GPL-3.0 License — see the LICENSE file for more information.

👤 Author

Nagendra Prasad
💼 Designed for internal IT automation and efficient power management.
