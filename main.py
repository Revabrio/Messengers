from v1 import client

def main():
    print('Simple Messenger')
    print('Please, choose:')
    print('1 - Simple v1 messenger')
    type = int(input('Enter you choise: '))
    while type != 1:
        print('Error!!!')
        print('Please, choose:')
        print('1 - Simple client-client messenger')
        type = int(input('Enter you choise: '))
    if type == 1:
        print('\n'*1000)
        client.main()


if __name__ == "__main__":
    main()