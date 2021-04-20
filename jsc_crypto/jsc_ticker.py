#!/usr/bin/pyhton

import socket
import time

from ticker import get_data

def listen(host, port):
    header = "HTTP/1.1 200 OK\n"
    header = header + "Server: nginx\n"
    header = header + "Content-Type: text/plain; charset=UTF-8\n"

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                result = get_data()
                response = header + "Content-Length: " + str(len(result)) + "\n"
                response = response + "Connection: close\n"
                response = response + "\n"
                response = response + result
                response = bytes(response, "UTF-8")
                conn.sendall(bytes(response))
            s.close()
            time.sleep(10)


listen("127.0.0.1", 8888)
