import socket

client = socket.socket()

friend_ip = input("Enter friend's IP: ")

client.connect((friend_ip, 5000))

while True:
    msg = input("You: ")
    client.send(msg.encode())

    reply = client.recv(1024).decode()
    print("Friend:", reply)