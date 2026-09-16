import os
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
PORT = int(os.getenv("PORT", 10000))

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Radar Prime Active")

def run_health_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    server.serve_forever()

def scan_loop():
    print("[RADAR] Radar Prime iniciado. Escaneando pares en Frankfurt...")
    while True:
        # Lógica de escaneo continuo
        time.sleep(60)

if __name__ == "__main__":
    # Servidor de salud para Render
    t = threading.Thread(target=run_health_server, daemon=True)
    t.start()
    scan_loop()
