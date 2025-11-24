# A tiny program that wil restart explorer.exe in Windows 

import os
import subprocess
import time

def restart_explorer():
    # Kill explorer.exe

    os.system("taskkill /f /im explorer.exe")
    time.sleep(1) # Lite pustepause

    # Start explorer.exe

    subprocess.Popen("explorer")

if __name__ == "__main__":
    restart_explorer()

