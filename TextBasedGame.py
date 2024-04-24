# Tiffany Sill

# room dictionary & variables
rooms = {
    'Greenhouse': {'East': 'Forest', 'Item': 'Herbs'},
    'Living Room': {'North': 'Greenhouse', 'East': 'Kitchen', 'West': 'Menagerie', 'South': 'Library'},
    'Forest': {'West': 'Greenhouse'},
    'Menagerie': {'East': 'Living Room', 'Item': 'Owl Feather'},
    'Kitchen': {'West': 'Living Room', 'North': 'Apothecary Cabinet', 'Item': 'Cauldron'},
    'Apothecary Cabinet': {'South': 'Kitchen', 'Item': 'Potion Oil'},
    'Library': {'North': 'Living Room', 'East': 'Study', 'Item': 'Grimoire'},
    'Study': {'West': 'Library', 'Item': 'Crystals'}
}

current_room = 'Living Room'
player_inventory = []
boss_room = 'Forest'


# Define get_new_state function
def get_new_state(direction_from_user, current_room):
    global player_inventory
    global rooms

    if direction_from_user in rooms[current_room]:
        new_room = rooms[current_room][direction_from_user]
        print("You are in the", new_room)

        # Check if room has an item
        if 'Item' in rooms[new_room]:
            item = rooms[new_room]['Item']
            print("You found:", item)

        return new_room
    else:
        print("You can't go that way.")
        return current_room


# Define game instructions function
def show_instructions():
    instructions = (
        "La Lechuza's Revenge\n"
        "Collect the 6 potion ingredients needed to banish La Lechuza before she takes her revenge.\n"
        "Movement commands: go North, go South, go East, go West\n"
        "Add to inventory command: get [item name]\n"
        "Check status command: status"
    )
    print(instructions)


# Define player status function
def display_status():
    global current_room
    print("Current Room:", current_room)

    if 'Item' in rooms[current_room]:
        print("Item in Room:", rooms[current_room]['Item'])
    else:
        print("No item in this room.")

    print("Inventory:", player_inventory)

    print("Valid Directions:")
    valid_directions = rooms[current_room].keys()
    valid_directions = [direction for direction in valid_directions if direction != 'Item']
    print(", ".join(valid_directions))


# Main gameplay function
def main():
    show_instructions()

    current_room = 'Living Room'  # starter room
    while True:
        command = input('Enter a command: ').lower()
        action, *kwargs = command.split()

        if action == 'go':
            direction = kwargs[0].capitalize()
            if direction in rooms[current_room]:
                current_room = get_new_state(direction, current_room)
            else:
                print('Invalid command')
        elif action == 'get':
            if len(kwargs) == 0:
                print('Please specify item name.')
            else:
                item_name = ' '.join(kwargs).lower()  # lowercase
                # Check for item
                if 'Item' in rooms[current_room]:
                    room_item = rooms[current_room]['Item']
                    if item_name.lower() == room_item.lower():
                        player_inventory.append(room_item)
                        del rooms[current_room]['Item']
                        print(f'You have obtained {room_item} .')
                    else:
                        print('Item not here.')
                else:
                    print('No item in this room.')
        elif action == 'status':
            display_status()  # display_status function
        elif action == 'quit':
            break
        else:
            print('Invalid command.')

        # Winning
        if len(player_inventory) == 6 and current_room == boss_room:
            print('Congratulations!\n'
                  'You have finished the potion and defeated La Lucheza!\n'
                  'You win!\n')
            break

        # Losing
        if current_room == boss_room and len(player_inventory) < 6:
            print("La Lucheza stalks you from the trees. She gets closer, and closer, and closer...\n"
                  "She will have her revenge\n"
                  'You lose.')
            break


if __name__ == "__main__":
    main()

