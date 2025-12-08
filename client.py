import socket

HOST = "127.0.0.1"
PORT = 6000

def main():
    print("TCP Connection Establishment & Termination Client\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print(f"[CLIENT] Connected to server at {HOST}:{PORT}\n")

        client.sendall("SYN".encode())
        print("[CLIENT → SERVER] SYN")

        syn_ack = client.recv(1024).decode()
        print("[SERVER → CLIENT]", syn_ack)

        if syn_ack == "SYN-ACK":
            client.sendall("ACK".encode())
            print("[CLIENT → SERVER] ACK")
            print("\n[CLIENT] Connection Established!\n")

        msg = client.recv(1024).decode()
        print("[SERVER → CLIENT]", msg)

        print("\n[CLIENT] Initiating connection termination...")

        client.sendall("FIN".encode())
        print("[CLIENT → SERVER] FIN")

        ack = client.recv(1024).decode()
        print("[SERVER → CLIENT]", ack)

        fin2 = client.recv(1024).decode()
        print("[SERVER → CLIENT]", fin2)

        if fin2 == "FIN":
            client.sendall("ACK".encode())
            print("[CLIENT → SERVER] ACK")
            print("\n[CLIENT] Connection closed successfully!")

if __name__ == "__main__":
    main()
