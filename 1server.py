import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5555))
server.listen()
print("[*] Waiting for connection..........")
client, address = server.accept()
print("Client detail is: "+str(client))
print("Client ip address and port are: "+str(address))
print("[*] Connection established.")

while True:
    try:
        data = client.recv(1024).decode()
        print("[*] Received command:", data)
        if data.strip().lower() == "exit":
            break
        output = os.popen(data).read()
        if output:
            client.send(output.encode())
        else:
            client.send("No output".encode())  # Sending a message indicating no output
    except Exception as e:
        print("[*] Error:", e)
        client.send(str(e).encode())  # Sending the error message to the client
        break

print("[*] Connection closed.")
server.close()
