# necrochopics/utils.py

import os
import time
from datetime import datetime
from rich.progress import track

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def progress_bar(text="Loading..."):
    for _ in track(range(100), description=text):
        time.sleep(0.01)

def log_error(error_msg):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{waktu}] {error_msg}\n"
    with open("error_log.txt", "a") as f:
        f.write(log_entry)

def bersihkan_jawaban(teks):
    return teks.strip().replace("\n\n", "\n")

def autocorrect(teks):
    return (
        teks.replace("gmn", "gimana")
            .replace("knp", "kenapa")
            .replace("tp", "tapi")
            .replace("yg", "yang")
            .replace("dgn", "dengan")
            .replace("sm", "sama")
    )
