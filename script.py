import random

def create_numbers_list(start_val):
    req_step = 4
    max_val = 1000
    return [item for item in range(start_val, max_val, req_step)]

print('How many pencils would you like to use:')
pos_values = {1, 2, 3}
validation = True

while validation:
    try:
        pencils = int(input())
        validation = False
    except ValueError:
        print('The number of pencils should be numeric')

while pencils <= 0:
    try:
        print('The number of pencils should be positive')
        pencils = int(input())
    except ValueError:
        print('The number of pencils should be numeric')

name = input('Who will be the first (John, Jack):\n')
while True:
    if name == 'John':
        break
    elif name == 'Jack':
        break
    else:
        print("Choose between 'John' and 'Jack'")
        name = input()

print(pencils * '|' + '\n')

while pencils != 0:
    print(f'{name}\'s turn:')
    if name == 'Jack':
        pencil_amount = len(pencils)
        if pencil_amount in create_numbers_list(2):
            pencils_num = 1
            print(pencils_num)
        elif pencil_amount in create_numbers_list(3):
            pencils_num = 2
            print(pencils_num)
        elif pencil_amount in create_numbers_list(4):
            pencils_num = 3
            print(pencils_num)
        elif pencil_amount in create_numbers_list(5):
            pencils_num = random.randint(1, 3)
            print(pencils_num)
        elif pencil_amount == 1:
            pencils_num = 1
            print(pencils_num)
        else:
            continue
    else:
        pencils_num = input()

        while True:
            try:
                pencils_num = int(pencils_num)
                if pencils_num not in pos_values:
                    print("Possible values: '1', '2' or '3'")
                    pencils_num = input()
                elif pencils_num > len(pencils):
                    print('Too many pencils were taken')
                    pencils_num = input()
                else:
                    break
            except ValueError:
                print("Possible values: '1', '2' or '3'")
                pencils_num = input()

    pencils = pencils.replace(pencils_num * '|', '', 1)
    print(pencils)

    name = 'John' if name == 'Jack' else 'Jack'

    if not pencils:
        print(f"{name} won!")
        break
