import socket
from openai_api import llm_call

LISTEN_ADDR = "127.0.0.1"
PORT = 5005
BUFFER = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_ADDR, PORT))
print(f"LLM_Listener: Listening on {LISTEN_ADDR}:{PORT}")

try:
    while True:
        data, addr = sock.recvfrom(BUFFER)
        text = data.decode('utf-8', errors='replace')
        print(f"[{addr[0]}:{addr[1]}] {text}")
        
        print("Calling gpt-5-nano...")
        llm_call(text)
        
except KeyboardInterrupt:
    print("Shutting down.")
finally:
    sock.close()
