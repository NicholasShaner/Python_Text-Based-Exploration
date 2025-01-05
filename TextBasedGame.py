# Nicholas Shaner IT-140
import time  # import time module for dramatic pause on WIN/LOSE notification :)

# dictionary of rooms
rooms = {
    'Service Drive': {'North': 'Dispatch Desk', 'Item': 'VEHICLE'},
    'Dispatch Desk': {'South': 'Service Drive', 'East': 'Service Counter', 'Item': 'PAPERWORK'},
    'Service Counter': {'West': 'Dispatch Desk', 'South': 'Parts Department'},
    'Parts Department': {'North': 'Service Counter', 'South': 'Fluids Room', 'East': 'Service Bay', 'Item': 'FILTER'},
    'Fluids Room': {'North': 'Parts Department', 'Item': 'OIL'},
    'Service Bay': {'West': 'Parts Department', 'East': 'Break Room', 'North': 'Waiting Room', 'Item': 'TOOLS'},
    'Break Room': {'West': 'Service Bay', 'Item': 'COFFEE'},
    'Waiting Room': {'South': 'Service Bay'}
}

print()
user_name = input('Enter name: ').capitalize()  # personalization
print()


# player stat funtion
def player_stat():
    print(f'{user_name}, you are at the {current_room}.')  # simple 'this is where you are'
    if len(inventory) == 0:  # loop for starting inventory/personalization
        print('Inventory: Find all the items before running into the unruly customer.')
        print()
    else:
        print('Inventory: ', inventory)  # prints current inventory for user
        print()


# move function
def get_move():
    global current_room, move  # imports global variables to allow modification within function
    # user input for a direction to move
    your_move = input('Enter a direction to go (North/South/East/West) or Exit to leave: ').capitalize().strip()
    if your_move not in ('North', 'South', 'East', 'West', 'Exit'):  # input validation
        print()
        print('Sorry, that\'s not an option.')
        get_move()  # restart get move

    else:  # if move input is valid
        move = your_move
        return move


# get items function
def get_items():
    global inventory, rooms  # imports global variables
    if 'Item' in rooms[current_room].keys():  # first loop, verify if current room has 'Item' available
        if rooms[current_room]['Item'] not in inventory:  # nested loop, verify if item already retrieved
            print('You see the', rooms[current_room]['Item'])
            print()
            print('You should grab that.')
            grabit = input('Type \"get (item name)\" or \"Pass\" to leave it:')  # input to get item
            invt = grabit.upper().split()  # uppercase and splits input for verification
            print()
            if len(invt) == 2 and invt[1] == rooms[current_room]['Item'] and invt[0] == 'GET':  # verification loop
                inventory.append(invt[1])  # add item to inventory list
                print('You grabbed the ', invt[1])
                print('New inventory:', inventory)
                print()
            elif len(invt) == 1 and invt[0] == 'PASS':  # option to forgo item (for whatever reason)
                pass
            else:
                print('I didn\'t get that,')  # input verification for spelling and command
                get_items()  # restart function

        elif rooms[current_room]['Item'] in inventory:  # nested loop for addressing item already in inventory list
            print('This is where you got the ', rooms[current_room]['Item'])  # user notified
    else:  # else of outer loop, if no item available in room
        pass


print()
print('-' * 80)
print(f'Welcome {user_name}, to the Service Drive Showdown text-based game! Good luck.')

with open('storyboard.txt', 'r') as story:  # open storyboard text file
    readme = [line.rstrip() for line in story.readlines()]  # reads file lines and strips whitespace and '\n'
    for lines in readme:  # iteration loop
        print(lines)  # prints storyboard
    print()

print('-' * 80)

move = ''  # blank string for function and validation
current_room = 'Service Counter'  # current room string
inventory = []  # empty list for appending retrieved inventory


# gameplay function
def play():
    global current_room, move, inventory  # imports global var to allow modification and validation

    while True:  # endless loop until exit
        print('-' * 25)
        player_stat()  # function call to display player_stat
        get_items()
        get_move()  # function call to get_move

        if move == 'Exit':  # termination statement allowing for game exit
            print()
            print('Thanks for playing {}!'.format(user_name))
            print('Please come back and try your luck again soon!')
            print()
            print('Goodbye!')
            break  # breaks program to exit

        if move != 'Exit':  # loop body statement for continuing gameplay
            if move in rooms[current_room].keys():  # if move request is valid to rooms dictionary
                current_room = rooms[current_room][move]  # rewrites current room value

                if current_room == 'Waiting Room' and len(inventory) < 6:
                    print()
                    print('OH NO! You ran into the unruly customer and they are NOT HAPPY!')
                    print('After a harsh verbal beating, you hand over their keys.')
                    print('The unruly customer peels away leaving nothing behind but...\n')
                    time.sleep(7)
                    print('A FAILED CUSTOMER SERVICE REVIEW!!\n')
                    time.sleep(3)
                    print('Oh well, you can\'t win them all. Better Luck Next Time {}!'.format(user_name))
                    break
                elif current_room == 'Waiting Room' and len(inventory) == 6:
                    print()
                    print('-' * 35)
                    print('You did it! You got the service done and left the unruly customer')
                    print('ecstatic with nothing to complain about! You take your perfect customer')
                    print('service review and freshen up...')
                    time.sleep(7)
                    print()
                    print('The next battle is walking through the door.')
                    print('-' * 35)
                    break
                else:
                    continue  # restarts while loop
            elif move not in rooms[current_room].keys():  # validation loop for invalid or move request
                print('Sorry, Cant go that way.')


play()  # function call to initiate gameplay
