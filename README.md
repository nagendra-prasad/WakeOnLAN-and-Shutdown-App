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

Optional for EXE build:
```bash
pip install pyinstaller

🧰 Installation & Usage
1️⃣ Edit the CSV file

Add your computer details in computers.csv:

hostname,mac_address,ip
PC01,00:1A:2B:3C:4D:5E,192.168.1.10
PC02,00:1A:2B:3C:4D:5F,192.168.1.11

2️⃣ Run the App
python WOL_Shutdown_Final_01.py

3️⃣ Convert to Executable (Optional)
pyinstaller --onefile --noconsole --icon=logo.ico WOL_Shutdown_Final_01.py

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

⚙️ Build the EXE

Once saved as WOL_Shutdown_Final.py, open Command Prompt in the same folder and run:

pip install pyinstaller wakeonlan pillow


Then create your .exe:

pyinstaller --onefile --noconsole WOL_Shutdown_Final.py

🪄 Notes

Make sure Wake-on-LAN is enabled in your BIOS and NIC settings.

For remote shutdown, the target PC must allow remote shutdowns or share proper credentials.

computers.csv should remain in the same directory as the .py or .exe.

📜 License

Licensed under the GNU GPL-3.0 License — see the LICENSE file for more information.

👤 Author

Nagendra Prasad
💼 Designed for internal IT automation and efficient power management.
