import socket
import threading
import time
import requests
import os 

# Список фейковых портов
FAKE_PORTS = [3389, 3306, 8080]

# Данные Telegram бота
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
HOST_IP = os.getenv("HOST_IP")

def send_telegram_alert(client_ip, target_port):
    message = f"Alert! Connection attempt from IP: {client_ip} on port {target_port} (host IP: {HOST_IP}) at {time.strftime('%Y-%m-%d %H:%M:%S')}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        requests.get(url, params=params)
    except Exception as e:
        print(f"Error sending message: {e}")

def listen_on_port(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"Listening on port {port}...")
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            client_ip, _ = client_address
            print(f"Connection attempt from {client_ip} on port {port}")
            send_telegram_alert(client_ip, port)  # отправляем правильный порт
            client_socket.close()
        except Exception as e:
            print(f"Error: {e}")

def start_listening():
    threads = []
    for port in FAKE_PORTS:
        thread = threading.Thread(target=listen_on_port, args=(port,))
        thread.daemon = True
        threads.append(thread)
        thread.start()

    while True:
        time.sleep(10)

if __name__ == "__main__":
    start_listening()
