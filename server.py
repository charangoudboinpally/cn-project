import socket
import json
import random

HOST = "127.0.0.1"
PORT = 6000

def main():
    print(f"[SERVER] Starting TCP Simulation Server on {HOST}:{PORT}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print("[SERVER] Waiting for client connection...\n")

        conn, addr = server.accept()
        print(f"[SERVER] Connected to {addr}")

        with conn:
            # RECEIVE JSON SYN PACKET
            data = conn.recv(1024).decode()
            syn_packet = json.loads(data)
            print("[CLIENT → SERVER] RECEIVED SYN PACKET:", syn_packet)

            if syn_packet.get("SYN") == 1:
                server_seq = random.randint(5000, 9000)

                syn_ack_packet = {
                    "SYN": 1,
                    "ACK": 1,
                    "SEQ": server_seq,
                    "ACK_NUM": syn_packet["SEQ"] + 1,
                    "WINDOW": 1000,
                    "MSS": 200
                }

                conn.sendall(json.dumps(syn_ack_packet).encode())
                print("[SERVER → CLIENT] SENT SYN-ACK:", syn_ack_packet)

            # RECEIVE ACK
            ack_data = conn.recv(1024).decode()
            ack_packet = json.loads(ack_data)
            print("[CLIENT → SERVER] RECEIVED ACK PACKET:", ack_packet)

            if ack_packet.get("ACK") == 1:
                print("\n[SERVER] Connection Established Successfully!\n")

if __name__ == "__main__":
    main()
