import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import os
import subprocess
from wakeonlan import send_magic_packet
from PIL import Image, ImageTk

# -----------------------------
# CONFIG
# -----------------------------
LOGO_PATH = "C:\\Users\\itsupport\\Desktop\\Shadesphere_logo1.png"

# -----------------------------
# APP CLASS
# -----------------------------
class WOLShutdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WOL & Remote Shutdown Utility")
        self.root.configure(bg="#1e1e1e")

        self.admin_user = ""
        self.admin_pass = ""
        self.computers = []

        self.setup_ui()

    # -----------------------------
    # UI SETUP
    # -----------------------------
    def setup_ui(self):
        # Logo
        try:
            img = Image.open(LOGO_PATH)
            img = img.resize((100, 100))
            self.logo = ImageTk.PhotoImage(img)
            tk.Label(self.root, image=self.logo, bg="#1e1e1e").pack(pady=5)
        except Exception as e:
            print(f"Logo not loaded: {e}")

        # Buttons Frame
        frame = tk.Frame(self.root, bg="#1e1e1e")
        frame.pack(pady=5)

        tk.Button(frame, text="Load CSV", command=self.load_csv, width=12, bg="#444", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Save CSV", command=self.save_csv, width=12, bg="#444", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Enter Admin Creds", command=self.enter_admin_creds, width=18, bg="#5555aa", fg="white").grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Select All", command=self.select_all, width=12, bg="#444", fg="white").grid(row=0, column=3, padx=5)
        tk.Button(frame, text="Deselect All", command=self.deselect_all, width=12, bg="#444", fg="white").grid(row=0, column=4, padx=5)
        tk.Button(frame, text="Ping Selected", command=self.ping_selected, width=14, bg="#ffaa00", fg="black").grid(row=0, column=5, padx=5)

        # Treeview
        columns = ("Hostname", "IP Address", "MAC", "Subnet", "Broadcast")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", selectmode="extended", height=8)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=140, anchor="center")
        self.tree.pack(padx=10, pady=10)

        # Style
        style = ttk.Style()
        style.configure("Treeview", background="#2d2d2d", fieldbackground="#2d2d2d", foreground="white")
        style.map('Treeview', background=[('selected', '#0078d7')])

        # Action Buttons
        btn_frame = tk.Frame(self.root, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Wake Selected", command=self.wake_selected, width=16, bg="#228b22", fg="white", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Shutdown Selected", command=self.shutdown_selected, width=16, bg="#ff6b6b", fg="white", font=("Segoe UI", 10, "bold")).grid(row=0, column=1, padx=10)

        # Status Log
        self.status_text = tk.Text(self.root, height=8, width=80, bg="#111", fg="lime", wrap="word")
        self.status_text.pack(padx=10, pady=10)
        self.log("No computers loaded. Please import a CSV file.")

    # -----------------------------
    # LOG
    # -----------------------------
    def log(self, msg):
        self.status_text.insert(tk.END, msg + "\n")
        self.status_text.see(tk.END)

    # -----------------------------
    # CSV HANDLERS
    # -----------------------------
    def load_csv(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
            if not file_path:
                return

            with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                required = {'hostname', 'ipaddress', 'macid', 'subnet', 'broadcast'}
                if not required.issubset(reader.fieldnames):
                    messagebox.showerror("Error", f"CSV missing required columns: {', '.join(required)}")
                    return

                self.computers = [row for row in reader]
                self.update_treeview()
                self.log(f"Loaded {len(self.computers)} computers from {os.path.basename(file_path)}.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV:\n{e}")

    def save_csv(self):
        if not self.computers:
            messagebox.showwarning("Warning", "No data to save.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['hostname', 'ipaddress', 'macid', 'subnet', 'broadcast', 'admin_user', 'admin_pass']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for comp in self.computers:
                    comp_copy = comp.copy()
                    comp_copy['admin_user'] = self.admin_user
                    comp_copy['admin_pass'] = self.admin_pass
                    writer.writerow(comp_copy)
            self.log(f"Saved computer list with credentials to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save CSV:\n{e}")

    # -----------------------------
    # UPDATE TREEVIEW
    # -----------------------------
    def update_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for comp in self.computers:
            self.tree.insert("", tk.END, values=(comp['hostname'], comp['ipaddress'], comp['macid'], comp['subnet'], comp['broadcast']))

    # -----------------------------
    # ADMIN CREDS
    # -----------------------------
    def enter_admin_creds(self):
        cred_win = tk.Toplevel(self.root)
        cred_win.title("Enter Admin Credentials")
        cred_win.configure(bg="#1e1e1e")
        tk.Label(cred_win, text="Username:", bg="#1e1e1e", fg="white").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(cred_win, text="Password:", bg="#1e1e1e", fg="white").grid(row=1, column=0, padx=5, pady=5)
        user_entry = tk.Entry(cred_win)
        pass_entry = tk.Entry(cred_win, show="*")
        user_entry.grid(row=0, column=1, padx=5, pady=5)
        pass_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Button(cred_win, text="Save", bg="#228b22", fg="white", command=lambda: self.save_admin_creds(user_entry.get(), pass_entry.get(), cred_win)).grid(row=2, column=0, columnspan=2, pady=10)

    def save_admin_creds(self, user, password, window):
        self.admin_user = user
        self.admin_pass = password
        window.destroy()
        self.log("Admin credentials saved.")

    # -----------------------------
    # ACTIONS
    # -----------------------------
    def select_all(self):
        for item in self.tree.get_children():
            self.tree.selection_add(item)

    def deselect_all(self):
        for item in self.tree.selection():
            self.tree.selection_remove(item)

    def ping_selected(self):
        for item in self.tree.selection():
            ip = self.tree.item(item, 'values')[1]
            response = subprocess.run(["ping", "-n", "1", ip], stdout=subprocess.PIPE)
            if response.returncode == 0:
                self.log(f"{ip} is reachable.")
            else:
                self.log(f"{ip} is NOT reachable.")

    def wake_selected(self):
        for item in self.tree.selection():
            mac = self.tree.item(item, 'values')[2]
            try:
                send_magic_packet(mac)
                self.log(f"Sent WOL packet to {mac}")
            except Exception as e:
                self.log(f"Failed to send WOL to {mac}: {e}")

    def shutdown_selected(self):
        for item in self.tree.selection():
            ip = self.tree.item(item, 'values')[1]
            try:
                cmd = f"shutdown /s /m \\\\{ip} /t 0 /f"
                subprocess.run(cmd, shell=True)
                self.log(f"Sent shutdown to {ip}")
            except Exception as e:
                self.log(f"Failed to shutdown {ip}: {e}")

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = WOLShutdownApp(root)
    root.mainloop()
