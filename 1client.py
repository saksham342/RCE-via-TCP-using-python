import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5555))

while True:
    data = input("Enter your command (type 'exit' to quit): ")
    try:
        client.send(data.encode())
        if data.strip().lower() == "exit":
            break
        received_data = client.recv(4096).decode()
        print("[*] Output:", received_data)
    except Exception as e:
        print("[*] Error:", e)
        break

client.close()
