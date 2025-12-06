import socket

HOST = "127.0.0.1"
PORT = 6000  # separate port from file-transfer project


def main():
    print(f"[SERVER] Starting TCP Simulation Server on {HOST}:{PORT}")

    # Create TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # Allow immediate reuse of the port if you restart quickly
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server.bind((HOST, PORT))
        server.listen()

        print("[SERVER] Waiting for client connection...\n")

        # Wait for one client connection
        conn, addr = server.accept()
        print(f"[SERVER] Connected to {addr}")

        with conn:
            # -------------------------------
            # 1) TCP 3-WAY HANDSHAKE SIMULATION
            # -------------------------------
            syn = conn.recv(1024).decode()
            print("[CLIENT → SERVER]", syn)

            if syn == "SYN":
                conn.sendall("SYN-ACK".encode())
                print("[SERVER → CLIENT] SYN-ACK")

            ack = conn.recv(1024).decode()
            print("[CLIENT → SERVER]", ack)

            if ack == "ACK":
                print("\n[SERVER] Connection Established Successfully!\n")

            # -------------------------------
            # Do some communication (optional)
            # -------------------------------
            conn.sendall(b"Connection established. You can now communicate.")

            # -------------------------------
            # 2) TCP CONNECTION TERMINATION SIMULATION
            # -------------------------------
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


# 🔴 This was missing earlier – without this, main() never runs
if __name__ == "__main__":
    main()
