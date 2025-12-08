import socket

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
            syn = conn.recv(1024).decode()
            print("[CLIENT → SERVER]", syn)

            if syn == "SYN":
                conn.sendall("SYN-ACK".encode())
                print("[SERVER → CLIENT] SYN-ACK")

            ack = conn.recv(1024).decode()
            print("[CLIENT → SERVER]", ack)

            if ack == "ACK":
                print("\n[SERVER] Connection Established Successfully!\n")

            conn.sendall(
                b"Connection established. This is a demo TCP simulation message from server."
            )
            print("[SERVER → CLIENT] Sent demo message to client.")

            fin1 = conn.recv(1024).decode()
            print("\n[CLIENT → SERVER]", fin1)

            if fin1 == "FIN":
                conn.sendall("ACK".encode())
                print("[SERVER → CLIENT] ACK")
                conn.sendall("FIN".encode())
                print("[SERVER → CLIENT] FIN")

            fin_ack = conn.recv(1024).decode()
            print("[CLIENT → SERVER]", fin_ack)

            if fin_ack == "ACK":
                print("\n[SERVER] Connection Terminated Successfully!")

    print("\n[SERVER] Server shutting down.")

if __name__ == "__main__":
    main()
