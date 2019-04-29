#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():

    # Open and read hashes.txt
    with open("hashes.txt", "r") as h:
        hashes = h.read().splitlines()

    # Open and read passwords.txt
    with open("passwords.txt", "r") as p:
        passwords = p.read().splitlines()

    # ASCII Lowercase letters
    characters = string.ascii_lowercase

    # Server information
    server_ip = "134.209.128.58"
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    
    # Parse data and crack 3 times
    i = 0
    while i < 3:
        
        data = s.recv(1024)

        # Prepend lowercase letter to a word in passwords
        for c in characters:
            for p in passwords:
            
                # crack hashes
                value = c + p
                hkey = hashlib.sha256(value).hexdigest()
            
                if hkey in data:
                    print value,":",hkey
                    s.send(value+"\n")
        i = i + 1

    data = s.recv(1024)
    print data
                    
if __name__ == "__main__":
    server_crack()