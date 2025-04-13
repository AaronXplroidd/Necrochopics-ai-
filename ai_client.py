# necrochopics/ai_client.py

import requests
import time
from necrochopics.config import MODEL, ENDPOINT, HEADERS, SYSTEM_PROMPT, TEMPERATURE, MAX_RETRY
from necrochopics.utils import log_error, bersihkan_jawaban

def kirim_ke_ai(chat_history):
    payload = {
        "model": MODEL,
        "messages": [SYSTEM_PROMPT] + chat_history,
        "temperature": TEMPERATURE
    }

    attempt = 0
    while attempt < MAX_RETRY:
        try:
            start = time.time()
            response = requests.post(ENDPOINT, headers=HEADERS, json=payload, timeout=10)
            response.raise_for_status()
            hasil = response.json()
            content = hasil["choices"][0]["message"]["content"]
            if not content.strip():
                raise ValueError("Respons kosong.")
            end = time.time()
            print(f"[INFO] Waktu respon: {round(end - start, 2)} detik")
            return bersihkan_jawaban(content)
        except (requests.exceptions.Timeout, ValueError, KeyError) as err:
            attempt += 1
            log_error(f"Percobaan {attempt}: {err}")
            print(f"[ERROR] Terjadi error: {err}")
            print(f"[INFO] Mencoba ulang... ({attempt}/{MAX_RETRY})")
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            log_error(f"RequestException: {e}")
            return f"[!] Gagal koneksi ke API: {e}"
        except Exception as e:
            log_error(f"Unknown error: {e}")
            return f"[!] Kesalahan tidak terduga: {e}"

    log_error("Gagal mendapatkan balasan setelah beberapa kali percobaan.")
    return "[!] Aku lagi sibuk, coba lagi nanti ya..."
