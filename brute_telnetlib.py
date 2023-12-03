import telnetlib

def check_for_win(response):
    if b'flag' in response:
        print(response)
        exit()


connection = telnetlib.Telnet('localhost', 1234)

while True:
    for number1 in range(0, 10):
        for number2 in range(0, 10):
            for number3 in range(0, 10):
                connection.write(b'3\n')
                connection.write(b'+\n')
                check_for_win(connection.read_until(b'Choose wheel (1-3) : '))
            connection.write(b'2\n')
            connection.write(b'+\n')
            check_for_win(connection.read_until(b'Choose wheel (1-3) : '))
        connection.write(b'1\n')
        connection.write(b'+\n')
        check_for_win(connection.read_until(b'Choose wheel (1-3) : '))
