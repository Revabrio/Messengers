import random
import socket

def client(ip, port):
    try:
        sock = socket.socket()
        sock.connect((str(ip), int(port)))
        sock.send('Hello!'.encode('UTF-8'))
        while True:
            try:
                data = sock.recv(1024)
                print('User: ' + data.decode('UTF-8'))
                message = input('Me: ')
                if message == 'quit':
                    sock.close()
                else:
                    sock.send(message.encode('UTF-8'))
            except:
                pass
    except Exception as _ex :
        if _ex == 'an integer is required (got type str)':
            print('Port in wrong type, use only numbers')

def server(ip, port):
    sock = socket.socket()
    sock.bind((str(ip), port))
    sock.listen(1)
    conn, addr = sock.accept()
    print(f'User {addr} has connected')
    data = conn.recv(1024)
    print('User: ' + data.decode('UTF-8'))
    while True:
        message = input('Me: ')
        if message == 'quit':
            conn.close()
        else:
            conn.send(message.encode('UTF-8'))
        data = conn.recv(1024)
        if data:
            print('User: ' + data.decode('UTF-8'))

def main():
    print('Simple Messenger')
    print('Please, choose:')
    print('1 - You will connect')
    print('2 - Will connect to you')
    type = int(input('Enter you choise: '))
    while type != 1 and type != 2:
        print('Error!!!')
        print('Please, choose:')
        print('1 - You will connect')
        print('2 - Will connect to you')
        type = int(input('Enter you choise: '))
    if type == 1:
        print('Please, enter ip and port')
        ip = input('Enter ip: ')
        port = input('Enter port: ')
        client(ip, port)
    if type == 2:
        ip = socket.gethostbyname(socket.gethostname())
        port = random.randint(1111,9999)
        print(f'Your ip - {ip}')
        print(f'Your port - {port}')
        server(ip, port)


if __name__ == "__main__":
    main()