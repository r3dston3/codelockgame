import random

def print_chest(user_input):
    print('---------------')
    print(f'|  {{{user_input[0]}}}{{{user_input[1]}}}{{{user_input[2]}}}  |')
    print('---------------')

def selector(wheel,user_input):
    sel = input("+/-")
    if sel == '+':
        user_input[wheel] += 1
    if sel == '-':
        user_input[wheel] -= 1
    if user_input[wheel] == 10:
        user_input[wheel] = 0
    elif user_input[wheel] == -1:
        user_input[wheel] = 9


def flag():
    print("flag{sup3r_s3cr3t_fl4g}")
def game():
    while True:
        print_chest(user_input)
        choise = int(input("Choose wheel (1-3) : ")) - 1
        if choise > -1 and choise < 3:
            selector(choise, user_input)

        if code == user_input:
            print("You win")
            flag()
            exit(0)
        else:
            print("Nothing happend")


code = [random.randrange(0,9),random.randrange(0,9),random.randrange(0,9)]
user_input = [0,0,0]

#print(code) #uncomment if you want see a code

game()
