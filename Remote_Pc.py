import socket


def receive_command(connection):
	while True:
    	command = input("Enter command: ")
    	if command.strip():
        	connection.send(command.encode())
        	print(f"Command '{command}' sent successfully.")
        	break

	data = connection.recv(1024)
	if data:
    	print("Command received and executed successfully.")
    	print(data.decode())


if __name__ == "__main__":
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	host = socket.gethostname()
	port = 8080
	server_socket.bind((host, port))
	print(f"Waiting for connections on {host}:{port}...")
	server_socket.listen(1)
	conn, addr = server_socket.accept()
	print(f"Connection established from {addr}")

	receive_command(conn)

	conn.close()
	server_socket.close()