import socket
import sys

host = "176.10.154.198"
port = 5500

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    soc.bind((host, port))
except socket.error as error:
    print(f"Bind failed. error code: {error}")
    sys.exit()

print("Socket bound...")

soc.listen(9)

conn, address = soc.accept()
print(f"Connected with {address[0]}:{address[1]}")
