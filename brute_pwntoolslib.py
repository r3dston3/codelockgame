import pwn


r = pwn.remote('localhost', 1234)

while True:
    for number1 in range(0, 10):
        for number2 in range(0, 10):
            for number3 in range(0, 10):
                r.sendline('3')
                r.sendline('+')
                print(r.recvuntil("Choose wheel (1-3) : "))
            r.sendline('2')
            r.sendline('+')
            print(r.recvuntil("Choose wheel (1-3) : "))
        r.sendline('1')
        r.sendline('+')
        print(r.recvuntil("Choose wheel (1-3) : "))
