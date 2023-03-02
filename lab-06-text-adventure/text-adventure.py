class room:
    """name str, active boolean"""

    def __init__(self, description, north, south, east, west ):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

def main():
    bedroom_2 = room("south bedroom", 3, None, 1, None)
    south_hall = room("south hall", 4, None, 2, 0)
    dining_room = room("dining room", 5, None, None, 1)
    bedroom_1 = room("north bedroom", None, 0, 4, None)
    north_hall = room("north hall", 6, 1, 5, 3)
    kitchen = room("kitchen", None, 2, None, 4)
    balcony = room("balcony", None, 4, None, None)
    room_list = [bedroom_2,south_hall,dining_room,bedroom_1,north_hall,kitchen,balcony]
    current_room = 0
    done = True
    while(done):
        print('You are in the', room_list[current_room].description)
        direction=''
        if (room_list[current_room].north != None):
            direction += 'north, '
        if (room_list[current_room].south != None):
            direction += 'south, '
        if (room_list[current_room].east != None):
            direction += 'east, '
        if (room_list[current_room].west != None):
            direction += 'west, '
        direction=direction[:(len(direction)-2)]
        print('you can go', direction, 'or stay here!')
        next_direction = input('Choose a way to go: ')
        while (next_direction not in ('north','south','east','west','jump')):
                if next_direction=='stay here':
                    print("\nSo you really want to stay here... that's ok with me, take your time and type north, south, east, west or jump whenever you feel ready ;)")
                else: print('\nType north, south, east or west')
                next_direction = input('Choose a way to go: ')
        if next_direction == 'jump':
            if current_room == 6:
                print("\nAnd so... you die by jumping off the balcony, you absolute disgrace... you do not only deserve to die, you don't deserve to play this game, gtfo out here")
                done = False
            else:
                print("\nAnd you jump... Just don't try it in the balcony...")
        old_current_room = current_room
        if next_direction == 'north':
            current_room = room_list[current_room].north
        elif next_direction == 'south':
            current_room = room_list[current_room].south
        elif next_direction == 'east':
            current_room = room_list[current_room].east
        elif next_direction == 'west':
            current_room = room_list[current_room].west
        if current_room == None:
            current_room = old_current_room
            print('\nIt seems there is a wall in the way...')
            print('Allow me to explain the drill to you again')
        print('')

main()