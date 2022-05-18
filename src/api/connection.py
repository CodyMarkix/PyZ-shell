import socket
import threading
import api
import shell.shell as shell

HEADER = 64
PORT = 23465
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"


connected = None

def handle_client(conn, addr):

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False # could also be "break", both are possible
            
            if msg.__contains__("pyzchprompt"):
                msgarr = msg.split()
                msgarr.pop(0)
                api.pyzprompt.chPrompt(" ".join(msgarr))

            if msg.__contains__("gtprompt"):
                api.pyzprompt.getPrompt()

            if msg.__contains__("setalias"):
                api.pyzshell.setAlias(msg.split(" ")[1], msg.split(" ")[2])



def stop():
    connected = False

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    while True:
        conn, addr = server.accept()
        handlethread = threading.Thread(target=handle_client, args=(conn, addr))
        handlethread.start()