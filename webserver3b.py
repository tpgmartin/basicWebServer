# Iterative server with sleep

import socket
import time

SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5

def handle_request(client_connection):
  request = client_connection.recv(1024)
  print(request.decode())
  http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""

  client_connection.sendall(http_response)
  time.sleep(60)

def server_forever():
  # Create TCP/IP socket
  listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Set some socket options - this is optional
  listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  # Bind address - assign local IP address and port number
  listen_socket.bind(SERVER_ADDRESS)
  # Set as a listening socket
  listen_socket.listen(REQUEST_QUEUE_SIZE)
  print('Serving HTTP on port {port} ...'.format(port=PORT))

  while True:
    client_connection, client_address = listen_socket.accept()
    handle_request(client_connection)
    client_connection.close()

if __name__ == '__main__':
  server_forever()