
### 2. Python Script (`main.py`) with GUI and Dependency Checks
```python
import tkinter as tk
from tkinter import scrolledtext
import subprocess
import pkg_resources
import sys

def install_dependencies():
    required_packages = {'mitmproxy': 'mitmproxy'}
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    missing_packages = required_packages.keys() - installed_packages
    
    for package in missing_packages:
        try:
            text_area.insert(tk.END, f"Installing {package}...\n")
            text_area.update()
            subprocess.check_call([sys.executable, "-m", "pip", "install", required_packages[package]])
            text_area.insert(tk.END, f"{package} installed successfully.\n")
        except subprocess.CalledProcessError:
            text_area.insert(tk.END, f"Failed to install {package}.\n")

    if not missing_packages:
        text_area.insert(tk.END, "All required packages are already installed.\n")
    text_area.yview(tk.END)

def run_proxy():
    text_area.insert(tk.END, "Proxy started...\n")
    text_area.yview(tk.END)

def stop_proxy():
    text_area.insert(tk.END, "Proxy stopped...\n")
    text_area.yview(tk.END)

def run_proxy_with_dependencies_check():
    text_area.insert(tk.END, "Checking for required packages...\n")
    install_dependencies()
    run_proxy()

root = tk.Tk()
root.title("IOSDiagnostics MITM Tool")

frame = tk.Frame(root)
frame.pack(pady=20)

text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=10, font=("Times New Roman", 12))
text_area.pack(padx=10, pady=10)

start_button = tk.Button(frame, text="Start Proxy", command=run_proxy_with_dependencies_check)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(frame, text="Stop Proxy", command=stop_proxy)
stop_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
