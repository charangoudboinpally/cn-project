# cn-project

📡 TCP Connection Establishment & Disconnection Simulation
Computer Networks – Python Socket Programming Project
📘 Project Description

This project simulates the TCP Three-Way Handshake and TCP Connection Termination using Python sockets.

Since Python does not expose low-level TCP flags (SYN, ACK, FIN), this project imitates the entire TCP process using custom messages, allowing students to understand how TCP establishes and terminates connections.


# project members

Balaji Tinety

Charan Boinpally


Rohan Goud Bairu

🔥 Features
✅ Simulated TCP 3-Way Handshake

Client → sends SYN

Server → replies SYN-ACK

Client → replies ACK

Connection becomes ESTABLISHED

✅ Simulated TCP Connection Termination

Client → sends FIN

Server → replies ACK

Server → sends FIN

Client → replies ACK

Connection is CLOSED

📂 Project Files
File	Description
server.py	Simulates TCP server performing handshake & termination
client.py	Simulates TCP client performing handshake & termination
README.md	Instructions & explanation


How to Run
1️⃣ Start the Server
python server.py

2️⃣ Run the Client
python client.py

<img width="841" height="528" alt="Screenshot 2025-12-06 154139" src="https://github.com/user-attachments/assets/8863b514-14ca-4e53-b9ac-9d274b32901b" />
<img width="861" height="599" alt="Screenshot 2025-12-06 154127" src="https://github.com/user-attachments/assets/e037f5ee-6356-41a0-95f9-bee2f5c6c1ef" />



