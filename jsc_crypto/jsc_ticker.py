#!/usr/bin/pyhton3

import socket
import time
import sys

from ticker import get_data

def listen(host, port, data):
    print("Connection received.")
    header = "HTTP/1.1 200 OK\n"
    header = header + "Server: nginx\n"
    header = header + "Content-Type: text/html; charset=UTF-8\n"

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                result = get_data(data) + "\n"
                response = header + "Content-Length: " + str(len(result)) + "\n"
                response = response + "Connection: close\n"
                response = response + "\n"
                response = response + result
                response = bytes(response, "UTF-8")
                conn.sendall(bytes(response))
            s.close()
            time.sleep(10)

if __name__ == "__main__":
    data = "data"
    print(f"Starting application with data in {data}")
    if len(sys.argv) > 1:
        data = sys.argv[1] 
    listen("0.0.0.0", 8888, data)
