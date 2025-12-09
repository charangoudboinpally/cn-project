import socket
import json
import random

HOST = "127.0.0.1"
PORT = 6000

def main():
    print("TCP Connection Establishment & Termination Client\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print(f"[CLIENT] Connected to server at {HOST}:{PORT}\n")

        # Pick random sequence number x
        seq = random.randint(1000, 5000)

        syn_packet = {
            "SYN": 1,
            "ACK": 0,
            "SEQ": seq,
            "ACK_NUM": 0,
            "WINDOW": 1000,
            "MSS": 200
        }

        client.sendall(json.dumps(syn_packet).encode())
        print("[CLIENT → SERVER] SENT SYN PACKET:", syn_packet)

        # Receive SYN-ACK
        syn_ack = json.loads(client.recv(1024).decode())
        print("[SERVER → CLIENT] RECEIVED SYN-ACK:", syn_ack)

        # ACK = 1, SEQ = x+1, ACK=y+1
        ack_packet = {
            "SYN": 0,
            "ACK": 1,
            "SEQ": seq + 1,
            "ACK_NUM": syn_ack["SEQ"] + 1
        }

        client.sendall(json.dumps(ack_packet).encode())
        print("[CLIENT → SERVER] SENT ACK PACKET:", ack_packet)

        print("\n[CLIENT] Connection Established!\n")

if __name__ == "__main__":
    main()
