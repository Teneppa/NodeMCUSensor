import socket
import time
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)

def writeFile(msg):
    with open('temp.txt', 'w') as f:
        f.write(str(msg))

try:
    sock.connect(('10.0.0.109', 8421))
except Exception as e:
    print("Cannot initialize socket!")
    writeFile("Can't open socket! -> EXIT")
    sock.close()
    sys.exit(0)

try:
    while True:

        try:
            sock.send("1;".encode())
            data = sock.recv(20)

            stripped = data.decode().strip().replace('\n', '').split('\r')[0]
            if stripped:
                print("STRIPPED: "+stripped)
                #breakpoint()
                try:
                    temp = float(stripped)
                except:
                    breakpoint()
                print(temp)

                try:
                    writeFile(temp)
                except:
                    print("Can't write to file!")

            time.sleep(2)
        except Exception as e:
            if e == KeyboardInterrupt:
                break

            print("Connection error!")

            with open('temp.txt', 'w') as f:
                f.write("ERR: CONNECTION")

            connected = False
            while not connected:
                sock.close()
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect(('10.0.0.109', 8421))
                    connected = True
                except Exception as e:
                    print(e)
                    print("Can't connect, trying again in 10s")
                    time.sleep(10)

            
            
except KeyboardInterrupt:
    print("EXITING")
    with open('temp.txt', 'w') as f:
        f.write("ERR: CLOSED")

sock.close()

