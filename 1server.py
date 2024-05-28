import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5555))
server.listen()
print("[*] Waiting for connection..........")
client, address = server.accept()
print("[*] Connection established.")

while True:
    try:
        data = client.recv(1024).decode()
        print("[*] Received command:", data)
        if data.strip().lower() == "exit":
            break
        output = os.popen(data).read()
        client.send(output.encode())
    except Exception as e:
        print("[*] Error:", e)
        break

print("[*] Connection closed.")
server.close()
